from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json


def main():
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.
    session = AmunSession()
    lat = 40
    lon = -80
    year = 2016
    dataset = "Era5"  # "Era5" | "Merra2" | "NEWA"

    print(f"Getting wind {dataset}")
    windData = session.get_wind(lat=lat, lon=lon, year=year, dataset=dataset)
    file = f"wind/{year}_{dataset}_{lat}_{lon}.json"
    save_to_json(file, windData)
    print(f"Saved wind to {file}")
    print("Done")


if __name__ == "__main__":
    main()
