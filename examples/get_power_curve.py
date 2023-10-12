from aurora.amun.client.session import AmunSession

def main():
    session = AmunSession()
    turbine = session.get_turbine_by_name("Siemens SWT-4.0-130")
    power_curve = session.get_power_curve(turbine["id"])

    # Print the first three points of the power curve
    print(power_curve[:3])

if __name__ == "__main__":
    main()