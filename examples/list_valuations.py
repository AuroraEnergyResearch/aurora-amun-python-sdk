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

    print("Done")


if __name__ == "__main__":
    main()
