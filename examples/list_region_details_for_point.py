from aurora.amun.client.session import AmunSession


def show_regions_for_point(latitude, longitude):
    session = AmunSession()
    print(f"Getting details for point ({latitude},{longitude})")
    regions = session.get_region_details(latitude=latitude, longitude=longitude)
    numToShow = 5
    print(f"found {len(regions)} regions print first {numToShow}")
    for val in regions[:numToShow]:
        print(val)

    print("Done")


def main():
    # point within GBR
    show_regions_for_point(latitude=51.753081, longitude=-1.250017)
    # point that has multiple regions
    show_regions_for_point(latitude=50.757310, longitude=1.225665)
    # point that has no regions supported.
    show_regions_for_point(latitude=50.757310, longitude=-50.225665)


if __name__ == "__main__":
    main()
