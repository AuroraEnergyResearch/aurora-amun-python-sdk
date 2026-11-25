---
title: Full-horizon valuations and loss templates
---

A valuation can model production over its **full forecast horizon** rather than repeating a single typical year, and can apply **time-varying losses** from an Excel loss template (based on the Amun Loss Template) instead of the static scalar losses.

:::note
Full-horizon mode is not supported for historic scenarios, scenarios with weather years, or the uploaded generation wind types. Loss templates require full-horizon mode. The scenario must cover whole months between 01/2019 and 12/2070.
:::

Runnable versions of these examples are in the `examples/` folder of the [Amun Python SDK repository](https://github.com/AuroraEnergyResearch/aurora-amun-python-sdk): `upload_loss_template.py`, `run_full_horizon_valuation.py`, `download_valuation_outputs.py`, `download_full_horizon_files.py` and `full_horizon_loss_template_e2e.py`.

### Upload a loss template

```python
from aurora.amun.client.session import AmunSession

session = AmunSession()
loss_template = session.upload_loss_template("Amun Loss Template.xlsx", "My loss template")
print(loss_template["id"])

# List or delete templates
session.get_loss_templates()
# session.delete_loss_template(loss_template["id"])  # valuations using it can no longer run
```

The template's content is checked when a valuation using it runs, so a problem in the workbook shows up as a valuation error.

### Create a full-horizon valuation using the template

```python
valuation = session.create_valuation({
    "windType": "era5",
    "name": "Full horizon wind farm",
    "description": "Created by Api",
    "longitude": "9",
    "latitude": "51",
    "turbineModelId": turbine_id,
    "numberOfTurbines": 10,
    "hubHeight": 90,
    "scenarioId": scenario_id,
    "fullHorizonMode": True,
    "lossSource": "template",
    "lossFileId": loss_template["id"],
})
```

### Download the outputs

The JSON output and the Excel databook are downloaded as usual. Requesting them runs the valuation. In loss template mode, the typical-year hourly and granular data are not included.

```python
session.get_valuation_results(valuation["id"], format="json", should_return_hourly_data=False,
                              save_to="out/valuation.json")
session.get_valuation_results(valuation["id"], format="excel", should_return_hourly_data=False,
                              save_to="out/valuation.xlsx")
```

### Download the additional full-horizon files

Once the valuation has been calculated, you can download the files produced by the wind output model: `site_out_granular.csv`, `site_out_hourly.csv`, `central_year_hourly.csv`, `central_year_granular.csv` and, in loss template mode, `loss_schedule.csv`. The production CSVs have two header rows; the second holds the units.

```python
files = session.get_valuation_files(valuation["id"])  # [{"name": ..., "s3link": ...}], links valid for 90 seconds
session.download_valuation_files(valuation["id"], "out/full_horizon")
```
