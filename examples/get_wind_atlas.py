from aurora.amun.client.session import AmunSession
from aurora.amun.client.utils import save_to_json
from datetime import datetime


def get_atlas_result(
    session, lat, lon, radius, regionCode, numberOfTurbines, rotorDiameterInMeters
):
    summary = f"{regionCode}_{lat}_{lon}_{numberOfTurbines}_{rotorDiameterInMeters}"
    print(f"Getting average wind speed for {summary}")
    atlasData = session.get_wind_atlas(
        lat=lat,
        lon=lon,
        radius=radius,
        regionCode=regionCode,
        numberOfTurbines=numberOfTurbines,
        rotorDiameterInMeters=rotorDiameterInMeters,
    )
    file_name = f"atlasData/{datetime.now().strftime('%Y%m%d-%H%M%S')}_{summary}.json"
    save_to_json(
        file_name, atlasData,
    )

    print(
        f"Average wind speed is '{atlasData['averageWindSpeed']}' Written {file_name}"
    )
    return atlasData


def main():
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.
    session = AmunSession()
    lat = 51.771239
    lon = -1.28433

    # Use default lookup for 10 trubines
    get_atlas_result(
        session=session,
        lat=lat,
        lon=lon,
        radius=None,
        regionCode="gbr",
        numberOfTurbines=10,
        rotorDiameterInMeters=None,
    )
    # Specific radius lookup
    get_atlas_result(
        session=session,
        lat=lat,
        lon=lon,
        radius=5,
        regionCode="gbr",
        numberOfTurbines=None,
        rotorDiameterInMeters=None,
    )


if __name__ == "__main__":
    main()
