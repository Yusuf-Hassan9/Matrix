def increase_hp(self, amount):
    self.HP += amount
    if self.HP > 100:  # Assuming 100 is the maximum HP cap
        self.HP = 100
    print(f"{self.name}'s HP increased to {self.HP}.\n")

def visit_supermarket(self):
    print("Welcome to the supermarket. Choose food or drink to re-energize:\n")
    supermarket_items = [
        ("Extra Strawberry", 5),
        ("Monster Energy", 10),
        ("Mccoys Flamed Grilled Steak", 3),
        ("Red Bull", 7),
        ("Meal Deal", 15)
    ]

    print(f"{'Item':<25}{'HP Gain'}")
    for idx, (item, hp_increase) in enumerate(supermarket_items, 1):
        print(f"[{idx}] {item:<25}{hp_increase}")

    try:
        choice = int(input("\nChoose an item by entering the number:\n ")) - 1
        if 0 <= choice < len(supermarket_items):
            item_name, hp_increase = supermarket_items[choice]
            print(f"\nYou chose {item_name}, which increases your HP by {hp_increase}.")
            self.increase_hp(hp_increase)
        else:
            print("\nInvalid choice. Please select a valid item number.\n")
    except ValueError:
        print("\nInvalid input. Please enter a number.\n")
