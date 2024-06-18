class PizzaRecipeApp:
    def __init__(self):
        self.crusts = ["Hand-Tossed", "Thin Crust", "Gluten-Free"]
        self.sauces = ["Marinara", "Alfredo", "Barbecue"]
        self.cheeses = ["Mozzarella", "Cheddar", "Feta"]
        self.toppings = ["Pepperoni", "Mushrooms", "Onions", "Bell Peppers", "Olives"]

    def display_menu(self):
        print("Welcome to the Pizza Recipe App!")
        print("Select a crust:")
        for i, crust in enumerate(self.crusts):
            print(f"{i+1}. {crust}")
        print("Select a sauce:")
        for i, sauce in enumerate(self.sauces):
            print(f"{i+1}. {sauce}")
        print("Select a cheese:")
        for i, cheese in enumerate(self.cheeses):
            print(f"{i+1}. {cheese}")
        print("Select toppings (choose up to 3):")
        for i, topping in enumerate(self.toppings):
            print(f"{i+1}. {topping}")

    def get_user_input(self):
        crust = int(input("Enter crust number: ")) - 1
        sauce = int(input("Enter sauce number: ")) - 1
        cheese = int(input("Enter cheese number: ")) - 1
        toppings = []
        for i in range(3):
            topping = int(input(f"Enter topping number {i+1} (or 0 to skip): ")) - 1
            if topping!= -1:
                toppings.append(self.toppings[topping])
        return {
            "crust": self.crusts[crust],
            "sauce": self.sauces[sauce],
            "cheese": self.cheeses[cheese],
            "toppings": toppings
        }

    def display_recipe(self, recipe):
        print("Your Pizza Recipe:")
        print(f"Crust: {recipe['crust']}")
        print(f"Sauce: {recipe['sauce']}")
        print(f"Cheese: {recipe['cheese']}")
        print(f"Toppings: {', '.join(recipe['toppings'])}")
        print("Instructions:")
        print("1. Preheat oven to 425°F (220°C).")
        print("2. Roll out the crust and place on a baking sheet.")
        print("3. Spread the sauce evenly over the crust.")
        print("4. Sprinkle the cheese over the sauce.")
        print("5. Add toppings as desired.")
        print("6. Bake for 12-15 minutes or until crust is golden brown.")
        print("Enjoy your delicious pizza!")

    def run(self):
        self.display_menu()
        recipe = self.get_user_input()
        self.display_recipe(recipe)

if __name__ == "__main__":
    app = PizzaRecipeApp()
    app.run()