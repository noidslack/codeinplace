# This simple program allows us to calculate the equivalent carbon footprint of different IT infrastructure resources in the cloud, 
# to size the impact that our solution designs can have and raise awareness among teams to choose the best options according to their needs, 
# avoiding oversizing.

# It is possible to replace the dictionary of emissions factors by calling an API that allows us to consult the online and updated information.
# It is possible to incorporate more CO2e emission factors from different cloud service providers and instance types
ef_instance = {
    # CO2 emission factors of AWS instances per hour of use
    "aws.t2.micro": 0.5,
    "aws.m5.large": 1.5,
    "aws.m5.2xlarge": 2,

    # CO2 emission factors of AWS storage per hour of use
    "aws.ssd": 0.0000013,
    "aws.hdd": 0.0000027,

    # CO2 emission factors of AWS DB per hour of use
    "aws.db.t2.micro": 0.5,
    "aws.db.m5.2xlarge": 3,

    # CO2 emission factors of GCP instances per hour of use
    "gcp.f1.micro": 0.5,
    "gcp.n1-standard-4": 1.5,
    "gcp.n1-highmem-8": 3,

    # CO2 emission factors of GCP storage per hour of use
    "gcp.ssd": 0.0000013,
    "gcp.hdd": 0.0000027
}

# Inputs for Calculation
def input_calculation():
    instance_type = input("Enter instance type (cloud provider.type instance): ").strip()
    hours = float(input("Enter hours of usage: ").strip())
    emissions = calculate_emissions(instance_type, hours)
    print(f"Estimated CO2e emissions: {emissions:.2f} kg")

# Calculation of emission factors
def calculate_emissions(instance_type, hours):
    if instance_type not in ef_instance:
        raise ValueError(f"Unknown instance type: {instance_type}")
    emissions = ef_instance[instance_type] * hours
    return emissions

# Search for a particular emission factor
def search_emissions():
    instance_search = input("Enter instance type (cloud provider.type instance): ").strip()
    if instance_search not in ef_instance:
        print(f"Unknown instance type: {instance_search}.")
    else:
        value = ef_instance[instance_search]
        print(f"The value for '{instance_search}' is {value} CO2e kg.")

# Show all emission factors from the dictionary
def show_all_emissions():
    for key, value in ef_instance.items():
        print(f"{key}: {value}")

# Add different emission factors of a solution
def add_emission_factors():
    total_emissions = 0.0
    while True:
        instance_type = input("Enter instance type (cloud provider.type instance) or 'F' to finish: ").strip()
        if instance_type == 'F':
            break
        if instance_type not in ef_instance:
            print(f"Unknown instance type: {instance_type}. Please try again.")
            continue
        hours = float(input("Enter hours of usage: ").strip())
        emissions = calculate_emissions(instance_type, hours)
        total_emissions += emissions
        print(f"Current total CO2e emissions: {total_emissions:.2f} kg")
    print(f"Final total CO2e emissions: {total_emissions:.2f} kg")

# Option menu
def main():
    while True:
        print("\nMenu:")
        print("1. Calculate CO2e")
        print("2. Search Emission Factor")
        print("3. Show All Emission Factors")
        print("4. Add Emission Factors")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

        if choice == '1':
            print("\nYou selected Option 1.")
            input_calculation()
        elif choice == '2':
            print("\nYou selected Option 2.")
            search_emissions()
        elif choice == '3':
            print("\nYou selected Option 3.")
            show_all_emissions()
        elif choice == '4':
            print("\nYou selected Option 4.")
            add_emission_factors()
        elif choice == '5':
            print("\nExiting the menu. Thank you for thinking about your carbon footprint!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

#Main Execution
if __name__ == "__main__":
    main()
