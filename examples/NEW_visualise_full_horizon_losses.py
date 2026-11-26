"""Step 5: visualise the full-horizon files to check the time-varying losses were applied.

Reads out/<valuation id>/full_horizon/*.csv (downloading them first if missing) and
writes a self-contained interactive report to out/<valuation id>/loss_report_<id>.html.

Only valuations run with a loss template are supported (they include loss_schedule.csv).

Charts:
1. Loss schedule over the forecast window (wake, external, combined).
2. Implied monthly loss, 1 - net LF / gross LF of the same calendar month, vs scheduled loss.
3. Monthly mean load factor, net vs gross central year.
4. Daily mean net load factor across the full horizon.
5. Hourly vs granular net load factor over a zoom window.

Extra requirements (not installed with the SDK): `pip install pandas plotly`
"""
import logging
import os
import re
import sys

try:
    import pandas as pd
    import plotly.graph_objects as go
except ImportError as error:
    sys.exit(
        f"Missing dependency ({error.name}). Install with: pip install pandas plotly"
    )

from aurora.amun.client.session import AmunSession

from NEW_full_horizon_steps import (
    OUT_DIR,
    download_full_horizon_files,
    load_local_env,
    setup_file_and_console_loggers,
)

# --- EDIT ME -----------------------------------------------------------------
VALUATION_ID = 88067  # id from run_full_horizon_valuation.py
ZOOM_START = None  # local time, e.g. "2030-01-01"; None = start of the forecast
ZOOM_DAYS = 14
# -----------------------------------------------------------------------------

log = logging.getLogger(__name__)

TIME_UTC = "Time (UTC)"
TIME_LOCAL = "Time (Local)"
LOAD_FACTOR = "Load factor"
PRODUCTION_FILES = [
    "central_year_hourly.csv",
    "site_out_hourly.csv",
    "site_out_granular.csv",
]
LOSS_SCHEDULE_FILE = "loss_schedule.csv"
WAKE_NOTE = (
    "Wake losses are applied to wind speed through a Weibull-fitted speed multiplier, "
    "so the implied loss of an individual month can differ slightly from the scheduled "
    "wake loss (it matches on an annual average). External losses are applied directly "
    "to power and should match closely."
)


def ensure_files(valuation_id):
    files_dir = os.path.join(OUT_DIR, str(valuation_id), "full_horizon")
    expected = PRODUCTION_FILES + [LOSS_SCHEDULE_FILE]
    if not all(os.path.exists(os.path.join(files_dir, name)) for name in expected):
        log.info(f"Full-horizon files not found in {files_dir}, downloading them")
        download_full_horizon_files(AmunSession(), valuation_id)
    if not os.path.exists(os.path.join(files_dir, LOSS_SCHEDULE_FILE)):
        sys.exit(
            f"Valuation {valuation_id} has no {LOSS_SCHEDULE_FILE} - "
            "not a template-mode valuation"
        )
    return files_dir


def read_local_offset(site_out_hourly_path):
    """The units row of the 'Time (Local)' column holds the offset, e.g. 'UTC+01:00'."""
    units = pd.read_csv(site_out_hourly_path, nrows=1)
    match = re.fullmatch(r"UTC(?:([+-])(\d{2}):(\d{2}))?", units[TIME_LOCAL][0].strip())
    if match is None:
        raise ValueError(f"Unexpected local time offset: {units[TIME_LOCAL][0]}")
    sign, hours, minutes = match.groups()
    if sign is None:
        return pd.Timedelta(0)
    offset = pd.Timedelta(hours=int(hours), minutes=int(minutes))
    return offset if sign == "+" else -offset


def read_production(path, columns):
    frame = pd.read_csv(path, skiprows=[1], usecols=columns)
    for column in columns:
        if column.startswith("Time"):
            frame[column] = pd.to_datetime(frame[column], format="%Y-%m-%d %H:%M:%S")
    return frame


def load_data(files_dir):
    hourly_path = os.path.join(files_dir, "site_out_hourly.csv")
    offset = read_local_offset(hourly_path)
    log.info(f"Local time offset: {offset}")

    central = read_production(
        os.path.join(files_dir, "central_year_hourly.csv"), [TIME_UTC, LOAD_FACTOR]
    )
    central[TIME_LOCAL] = central[TIME_UTC] + offset
    hourly = read_production(hourly_path, [TIME_LOCAL, LOAD_FACTOR])
    granular = read_production(
        os.path.join(files_dir, "site_out_granular.csv"), [TIME_LOCAL, LOAD_FACTOR]
    )
    schedule = pd.read_csv(os.path.join(files_dir, LOSS_SCHEDULE_FILE))
    return central, hourly, granular, schedule


def monthly_comparison(central, hourly, schedule):
    gross_by_month = central.groupby(central[TIME_LOCAL].dt.month)[LOAD_FACTOR].mean()

    net = hourly.groupby(
        [hourly[TIME_LOCAL].dt.year.rename("year"), hourly[TIME_LOCAL].dt.month.rename("month")]
    )[LOAD_FACTOR].agg(["mean", "count"])
    net = net.rename(columns={"mean": "net_lf", "count": "hours"}).reset_index()
    net["gross_lf"] = net["month"].map(gross_by_month)
    net["implied_loss"] = 1 - net["net_lf"] / net["gross_lf"]

    schedule = schedule.copy()
    schedule["combined"] = 1 - (1 - schedule["wake"]) * (1 - schedule["external"])
    monthly = net.merge(schedule, on=["year", "month"], how="left")
    monthly["date"] = pd.to_datetime(dict(year=monthly["year"], month=monthly["month"], day=1))
    return monthly


def schedule_figure(monthly):
    figure = go.Figure()
    for column, name in [("wake", "Wake"), ("external", "External"), ("combined", "Combined")]:
        figure.add_trace(
            go.Scatter(x=monthly["date"], y=monthly[column], name=name, line_shape="hv")
        )
    figure.update_layout(
        title="1. Loss schedule over the forecast window",
        yaxis=dict(title="Loss", tickformat=".0%"),
    )
    return figure


def implied_loss_figure(monthly):
    figure = go.Figure()
    figure.add_trace(
        go.Scatter(
            x=monthly["date"], y=monthly["combined"], name="Scheduled combined loss",
            line_shape="hv",
        )
    )
    figure.add_trace(
        go.Scatter(
            x=monthly["date"], y=monthly["implied_loss"], name="Implied loss",
            mode="markers", marker=dict(size=4),
        )
    )
    figure.update_layout(
        title="2. Implied monthly loss vs scheduled loss",
        yaxis=dict(title="Loss", tickformat=".0%"),
    )
    return figure


def monthly_lf_figure(monthly):
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=monthly["date"], y=monthly["gross_lf"], name="Gross (central year)"))
    figure.add_trace(go.Scatter(x=monthly["date"], y=monthly["net_lf"], name="Net"))
    figure.update_layout(
        title="3. Monthly mean load factor, net vs gross",
        yaxis=dict(title="Load factor", tickformat=".0%"),
    )
    return figure


def daily_lf_figure(hourly):
    daily = hourly.set_index(TIME_LOCAL)[LOAD_FACTOR].resample("D").mean()
    figure = go.Figure(go.Scatter(x=daily.index, y=daily.values, name="Daily mean net LF"))
    figure.update_layout(
        title="4. Daily mean net load factor across the full horizon",
        yaxis=dict(title="Load factor", tickformat=".0%"),
        xaxis=dict(rangeslider=dict(visible=True)),
    )
    return figure


def zoom_figure(hourly, granular, zoom_start, zoom_days):
    start = pd.Timestamp(zoom_start) if zoom_start is not None else hourly[TIME_LOCAL].min()
    end = start + pd.Timedelta(days=zoom_days)
    figure = go.Figure()
    for frame, name in [(granular, "Granular"), (hourly, "Hourly")]:
        window = frame[(frame[TIME_LOCAL] >= start) & (frame[TIME_LOCAL] < end)]
        figure.add_trace(
            go.Scatter(x=window[TIME_LOCAL], y=window[LOAD_FACTOR], name=name, line_shape="hv")
        )
    figure.update_layout(
        title=f"5. Hourly vs granular net load factor, {start:%Y-%m-%d} + {zoom_days} days (local)",
        yaxis=dict(title="Load factor", tickformat=".0%"),
    )
    return figure


def write_report(path, valuation_id, figures):
    sections = []
    for index, (figure, note) in enumerate(figures):
        figure.update_layout(height=500, hovermode="x unified")
        html = figure.to_html(full_html=False, include_plotlyjs=(index == 0))
        sections.append(html + (f"<p><i>{note}</i></p>" if note else ""))
    with open(path, "w", encoding="utf-8") as report:
        report.write(
            "<html><head><meta charset='utf-8'>"
            f"<title>Loss report - valuation {valuation_id}</title></head>"
            "<body style='font-family: sans-serif'>"
            f"<h1>Full-horizon loss report - valuation {valuation_id}</h1>"
            + "".join(sections)
            + "</body></html>"
        )


def main():
    load_local_env()
    setup_file_and_console_loggers("visualise_full_horizon_losses.log")
    log.setLevel(logging.DEBUG)

    files_dir = ensure_files(VALUATION_ID)
    central, hourly, granular, schedule = load_data(files_dir)
    monthly = monthly_comparison(central, hourly, schedule)

    report_path = os.path.join(OUT_DIR, str(VALUATION_ID), f"loss_report_{VALUATION_ID}.html")
    write_report(
        report_path,
        VALUATION_ID,
        [
            (schedule_figure(monthly), None),
            (implied_loss_figure(monthly), WAKE_NOTE),
            (monthly_lf_figure(monthly), None),
            (daily_lf_figure(hourly), None),
            (zoom_figure(hourly, granular, ZOOM_START, ZOOM_DAYS), None),
        ],
    )
    log.info(f"Loss report written to {os.path.abspath(report_path)}")


if __name__ == "__main__":
    main()
