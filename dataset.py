#Function to collect data
def collect_data():
    print("\nCollecting data for cities, k2, and key3...")
    print("-"*32)

    # Collect k1 data
    key1 = []
    k1 = input("Enter the name of the variable that you want to cluster: ").lower()
    while True:
        cities = input(f"Enter a {k1} name (or type 'e' to finish): ")
        if cities.lower() == "e":
            break
        else:
            key1.append(cities)

    # Collect k2 data
    key2 = []
    k2 = input("Enter the name of the first variable that you want analize: ").lower()
    while True:
        num_k2 = input(f"Enter a {k2} value (or type 'e' to finish): ")
        if num_k2.lower() == "e":
            break
        else:
            try:
                num_k2 = int(num_k2)
                key2.append(num_k2)
            except:
                print("Invalid input. Please enter numbers only or type 'e'.")

    # Collect key3 data
    key3 = []
    k3 = input("Enter the name of the second variable that you want analize: ").lower()
    while True:
        num_key3 = input("Enter a key3 value (or type 'e' to finish): ")
        if num_key3.lower() == "e":
            break
        else:
            try:
                num_key3 = int(num_key3)
                key3.append(num_key3)
            except:
                print("Invalid input. Please enter numbers only or type 'e'.")
                
    # Verify that all lists have the same length
    if len(key1) != len(key2) or len(key2) != len(key3):
        print(f"\n{k1}, {k2}, and {k3} lists MUST HAVE the same number of elements.")
        print("Please re-enter the data\n")
        return collect_data()  # Recursively call the function to restart data collection

    # Combine data into a dictionary
    data = {k1: key1, k2: key2, k3: key3}
    return data