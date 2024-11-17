EMISSION_FACTORS = {
    "diet": {"1": 500, "2": 1000, "3": 2000, "4": 3000},  # kg CO2 per year for different diets
    "clothing": {"1": 720, "2": 2040, "3": 2520, "4": 5040},  # kg CO2 per year for different expense levels
    "electricity": 0.92,  # kg CO2 per kWh
    "gas": 5.3,  # kg CO2 per therm
    "car": 8.887,  # kg CO2 per gallon of gasoline
    "short_flight": 250,  # kg CO2 per short flight
    "long_flight": 1100  # kg CO2 per long flight
}


def carbon_calculator():
    print("Welcome to the Carbon Footprint Calculator!")

    # Collecting values from user input
    while True:
        try:
            electricity = float(input("Enter your average monthly electricity consumption in kWh: "))
            gas = float(input("Enter your average monthly fuel consumption in liters: "))
            car_mileage = float(input("Enter your average yearly car mileage in miles: "))
            fuel_efficiency = float(input("Enter your car's fuel efficiency in kilometers per liter (km/L): "))
            flights = int(input("Enter the number of short flights (<3 hours) you take per year: "))
            long_flights = int(input("Enter the number of long flights (>3 hours) you take per year: "))
            diet = input(
                "Which statement is most accurate for you?\n"
                "1. I follow a vegan diet.\n"
                "2. I am vegetarian.\n"
                "3. I eat meat occasionally.\n"
                "4. I eat meat frequently.\n"
                "Enter the number corresponding to your diet: "
            )
            house_size = float(input("Enter the size of your house or apartment in square meters: "))
            heating_system = input("What type of heating system do you use (e.g., gas, electric, solar)?: ")
            clothing_expenses = int(input(
                "Which statement is most accurate for you?\n"
                "1. I purchase new clothing, devices, and furniture very rarely (60 euros a month).\n"
                "2. I purchase half of my clothing, devices, and furniture second-hand (170 euros a month).\n"
                "3. I occasionally purchase new clothing, devices, and furniture (210 euros a month).\n"
                "4. I frequently purchase new clothing, devices, and furniture (420 euros a month).\n"
                "Enter the number corresponding to your expenses: "
            ))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values where required.")

    # Calculating carbon emissions
    electricity_emissions = calculate_electricity_emissions(electricity, EMISSION_FACTORS["electricity"])
    gas_emissions = calculate_gas_emissions(gas, EMISSION_FACTORS["gas"])
    car_emissions = calculate_car_emissions(car_mileage, fuel_efficiency, EMISSION_FACTORS["car"])
    flight_emissions = calculate_flight_emissions(flights, long_flights, EMISSION_FACTORS["short_flight"],
                                                  EMISSION_FACTORS["long_flight"])
    diet_emissions = calculate_diet_emissions(diet, EMISSION_FACTORS["diet"])
    clothing_emissions = calculate_clothing_emissions(clothing_expenses, EMISSION_FACTORS["clothing"])

    # Total emissions
    total_emissions = calculate_total_emissions(
        electricity_emissions, gas_emissions, car_emissions, flight_emissions, diet_emissions, clothing_emissions
    )

    # Displaying results
    print("""
Your
estimated
annual
carbon
emissions
are:
""")
    print(f"Diet: {diet_emissions:.2f} kg CO2")
    print(f"Clothing and Household Expenses: {clothing_emissions:.2f} kg CO2")
    print(f"Electricity: {electricity_emissions:.2f} kg CO2")
    print(f"Natural Gas: {gas_emissions:.2f} kg CO2")
    print(f"Car Travel: {car_emissions:.2f} kg CO2")
    print(f"Flights: {flight_emissions:.2f} kg CO2")
    print(f"\nTotal Annual Emissions: {total_emissions:.2f} kg CO2")

    # Suggesting ways to reduce emissions
    suggest_reduction(total_emissions)


def calculate_electricity_emissions(electricity, factor):
    return electricity * factor * 12  # annual


def calculate_gas_emissions(gas, factor):
    return gas * factor * 12  # annual


def calculate_car_emissions(mileage, efficiency, factor):
    return (mileage / efficiency) * factor


def calculate_flight_emissions(short_flights, long_flights, short_factor, long_factor):
    return (short_flights * short_factor) + (long_flights * long_factor)


def calculate_diet_emissions(diet, factors):
    return factors.get(diet, 0)


def calculate_clothing_emissions(expenses, factors):
    return factors.get(str(expenses), 0)


def calculate_total_emissions(electricity, gas, car, flight, diet, clothing):
    return electricity + gas + car + flight + diet + clothing


def suggest_reduction(total_emissions):
    message = get_reduction_message(total_emissions)
    print(message)

def get_reduction_message(total_emissions):
    if total_emissions > 10000:
        return "\nYour emissions are above average. Consider reducing your electricity usage, minimizing flights, or switching to a more fuel-efficient vehicle."
    elif total_emissions > 5000:
        return "\nYour emissions are moderate. Look for ways to improve energy efficiency at home and explore alternative travel options."
    else:
        return "\nGreat job! Your carbon emissions are below average. Keep up the eco-friendly habits!"


if __name__ == "__main__":
    carbon_calculator()
