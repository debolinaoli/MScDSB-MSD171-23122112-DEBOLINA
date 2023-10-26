class PetStore:
    def __init__(self):
        self.pets = []

    def store_pet_details(self, pet_name, pet_type, pet_price):
        pet = {
            "Name": pet_name,
            "Type": pet_type,
            "Price": pet_price
        }
        self.pets.append(pet)

    def search_for_pet(self, pet_name):
        for pet in self.pets:
            if pet["Name"] == pet_name:
                return pet
        return None

    def sell_pet(self, pet_name):
        pet = self.search_for_pet(pet_name)
        if pet:
            self.pets.remove(pet)
            return pet
        else:
            return None

    def list_all_pets(self):
        return self.pets

if __name__== "__main__":
    pet_store = PetStore()

    while True:
        print("\nPet Store Menu:")
        print("1. Add a new pet")
        print("2. Search for a pet")
        print("3. Sell a pet")
        print("4. List all pets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet_name = input("Enter pet name: ")
            pet_type = input("Enter pet type: ")
            pet_price = float(input("Enter pet price: "))
            pet_store.store_pet_details(pet_name, pet_type, pet_price)
            print(f"{pet_name} has been added to the store.")

        elif choice == "2":
            pet_name = input("Enter the name of the pet to search: ")
            pet = pet_store.search_for_pet(pet_name)
            if pet:
                print(f"Pet found: {pet['Name']} ({pet['Type']}) - Price: ${pet['Price']}")
            else:
                print("Pet not found in the store.")

        elif choice == "3":
            pet_name = input("Enter the name of the pet to sell: ")
            sold_pet = pet_store.sell_pet(pet_name)
            if sold_pet:
                print(f"{sold_pet['Name']} has been sold for ${sold_pet['Price']}")
            else:
                print("Pet not found in the store.")

        elif choice == "4":
            pets = pet_store.list_all_pets()
            if pets:
                print("List of all pets in the store:")
                for pet in pets:
                    print(f"{pet['Name']} ({pet['Type']}) - Price: ${pet['Price']}")
            else:
                print("No pets available in the store.")

        elif choice == "5":
            print("Exiting the Pet Store. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")