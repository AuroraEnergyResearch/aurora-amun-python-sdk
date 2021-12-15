from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json


def main():
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.
    session = AmunSession()
    lat = 51.771239
    lon = -1.284330
    year = 2016
    radius = 8
    regionCode = "gbr"  # "gbr" | "deu"

    print(f"Getting wind {regionCode}")
    windData = session.get_wind_atlas(
        lat=lat, lon=lon, year=year, radius=radius, regionCode=regionCode
    )
    save_to_json(f"wind/{year}_{regionCode}_{lat}_{lon}.json", windData)

    print("Done")


if __name__ == "__main__":
    main()
