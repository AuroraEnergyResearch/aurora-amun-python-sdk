from aurora.amun.client.session import AmunSession


def copy_valuation(valuation_id, session):
    # Calling with no token in constructor will load one from an environment variable if provided
    # or a file in HOME/.

    print("Copying Valuation")

    response = session.copy_valuation(valuation_id)
    new_valuation_id = response["id"]

    print(f"Valuation copied with id {new_valuation_id}")

    print("Done")

    return new_valuation_id


def main():
    session = AmunSession()

    # Get the first valuation and duplicate it
    valuations = session.get_valuations()
    valuation_id = valuations[0]["id"]

    new_valuation_id = copy_valuation(valuation_id, session)


if __name__ == "__main__":
    main()
