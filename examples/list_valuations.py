from aurora.amun.client.session import AmunSession


def main():
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.
    session = AmunSession()
    print("Getting Valuations")

    valuations = session.get_valuations()

    numToShow = 5
    print(f"found {len(valuations)} valuations print first {numToShow}")
    for val in valuations[:numToShow]:
        print(val)

    # filters valuations through the name, description and author
    # (includes MySQL avanced search query functionalities)
    filtered_valuations = session.get_valuations(searchText="test")
    print(f"found {len(filtered_valuations)} with the custom search text.")
    for val in filtered_valuations:
        print(val)

    print("Done")


if __name__ == "__main__":
    main()
