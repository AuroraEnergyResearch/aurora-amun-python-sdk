from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json


def main():
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.
    session = AmunSession()
    lat = 51.771239
    lon = -1.284330
    year = 2016
    dataset = "NEWA"  # "Era5" | "Merra2" | "NEWA"

    print(f"Getting wind {dataset}")
    windData = session.get_wind(lat=lat, lon=lon, year=year, dataset=dataset)
    save_to_json(f"wind/{year}_{dataset}_{lat}_{lon}.json", windData)

    print("Done")


if __name__ == "__main__":
    main()
