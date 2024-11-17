# Program that teaches the importance of functions by making pasta
import random
import sys
import time

# Ingredients dictionary to track available ingredients
ingredients = {
    "flour": 10.0,
    "eggs": 4.0,
    "tomatoes": 3.0,
    "sauce": 3.0,
    "pepper": 5.0,
    "water": 66.0,
    "pasta": 1.0  
}

print("We are about to make pasta")

def print_ingredient_status(ingredient):
    """Prints the current amount of a specified ingredient."""
    if ingredient in ingredients:
        print(f"Current amount of {ingredient}: {ingredients[ingredient]}.")

def make_pasta():
    """Main function to make pasta by calling other functions."""
    add_flour()
    add_eggs() 
    add_water()
    boil_water() 
    cut_noodles()
    cook_pasta()
    add_sauce()
    add_seasoning()
    plate_pasta()
    wine_suggestion()
    tips() 

def add_flour():
    """Function to add flour to the pasta."""
    open_flour_bag()
    pour_flour()
    print("Adding flour...")
    print_ingredient_status("flour")

def add_eggs():
    """Function to add eggs to the pasta."""
    while True:
        try:
            amount = float(input("Enter the amount of eggs to pour (in pieces): "))
            if amount <= 0:
                print("Please enter a positive number.")
                continue
            if amount > 2:
                print("Usually the best amount is 2 eggs, but let's try your suggestion! 😁")
            print(f"Cracking {amount} eggs...")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    for i in range(3):  # Simulate cracking eggs for 3 seconds
        print("🥚" * (i + 1))  # Show increasing eggs
        time.sleep(1)  # Wait for 1 second

    ingredients["eggs"] -= amount
    print_ingredient_status("eggs")
    print("Eggs are poured in the cup!")

def add_water():
    """Function to add water to the pasta."""
    print("Adding water...")
    ingredients["water"] -= 0.5
    print_ingredient_status("water")
    time.sleep(1)  # Simulate time to add water
    print("Water is added to the cup!")
    print("Now we have to wait for the water to boil...")
    time.sleep(5)  # Simulate time to boil water

def boil_water():
    """Function to simulate boiling water with ASCII art."""
    print("Boiling water...")
    for i in range(5):  # Simulate boiling for 5 seconds
        print("💧" * (i + 1))  # Show increasing water droplets
        time.sleep(1)  # Wait for 1 second
    print("Water is boiled!")

def cut_noodles():
    """Function to cut the cooked pasta into noodles."""
    noodle_shape = input("What shape do you want for your noodles? (e.g., fettuccine, spaghetti, penne): ").strip().lower()
    
    valid_shapes = ["fettuccine", "spaghetti", "penne", "linguine", "macaroni", "rotini", "tagliatelle"]
    
    if noodle_shape in valid_shapes:
        print(f"Cutting {noodle_shape} noodles...")
        time.sleep(1)  # Simulate time to cut noodles
        print(f"Noodles are cut into {noodle_shape} shape!")
    else:
        print("That's not a common noodle shape, but we'll cut it however you like! 😊")
        print(f"Cutting the pasta into {noodle_shape} shape...")
        time.sleep(1)  # Simulate time to cut noodles
        print(f"Noodles are cut into {noodle_shape} shape!")

def cook_pasta():
    """Function to cook the pasta."""
    cooking_time = 10  # Simulated cooking time in seconds
    print(f"Cooking pasta for {cooking_time} seconds...")
    for i in range(cooking_time):
        print("🍝" * (i + 1))  # Show increasing pasta
        time.sleep(1)  # Wait for 1 second
    print("Pasta is cooked!")

def add_sauce():
    """Function to add sauce to the pasta."""
    mash_tomatoes()
    print("Adding sauce...")
    ingredients["sauce"] -= 0.2
    print_ingredient_status("sauce")

def open_flour_bag():
    """Function to open the flour bag if it's not already open."""
    if flour_bag_open():
        print("Flour bag is already open.")
    else:
        print("Opening flour bag...")

def flour_bag_open():
    """Check if the flour bag is open."""
    return False  # Change this to True if the bag is open

def pour_flour():
    """Function to pour a specified amount of flour."""
    while True:
        try:
            amount = float(input("Enter the amount of flour to pour (in cups): "))
            if amount <= 0:
                print("Please enter a positive number.")
                continue
            if amount > 2:
                print("Usually the best amount is 2, but let's try your suggestion! 😁")
            print(f"Pouring {amount} cups of flour...")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    print_ingredient_status("flour")

def mash_tomatoes():
    """Function to mash tomatoes for the sauce."""
    get_tomatoes()
    get_hammer()
    print("Mashing tomatoes...")
    print("Tomatoes are mashed...")

def get_tomatoes():
    """Function to get tomatoes from the bag."""
    if bag_is_opened():
        print("Tomatoes are taken out...")
        ingredients["tomatoes"] -= 0.5
        print_ingredient_status("tomatoes")
    else:
        print("Cannot get tomatoes; bag is closed.")

def get_hammer():
    """Function to get a hammer for mashing tomatoes."""
    while True: 
        hammer_size = input("Do you want to use a big hammer or a small hammer? (small/big): ").strip().lower()
        if hammer_size in ['small', 'big']:
            print(f"{hammer_size.capitalize()} hammer is taken out of the drawer...")
            break
        else:
            print("Invalid input. Please enter 'small' or 'big'.")
        
    if hammer_is_not_found():
        print("Hammer not found; cannot proceed. Exiting program.")
        sys.exit()  # Exit the program if the hammer is not found
    else:
        print("Using hammer...")

def bag_is_opened():
    """Check if the tomato bag is opened."""
    return True  # Change this to False if the bag is closed

def hammer_is_not_found():
    """Check if the hammer is found."""
    return False  # Change this to True if the hammer is not found

def add_seasoning():
    """Function to add seasoning to the pasta."""
    print("We got all the seasonings you like!")
    seasoning = input("Enter the type of seasoning to add: ")
    print(f"Adding {seasoning} seasoning...")

def plate_pasta():
    """Function to describe how to plate the pasta."""
    print("Plating the pasta...")
    print("1. Use a large, shallow bowl or plate.")
    print("2. Twirl the pasta with a fork and place it in the center of the plate.")
    print("3. Gently drizzle some sauce over the top.")
    print("4. Garnish with freshly grated Parmesan cheese and a sprinkle of black pepper.")
    print("5. Add a few basil leaves for a pop of color.")
    print("6. Serve with a glass of your favorite wine.")
    print("Your pasta is beautifully plated and ready to be enjoyed!")

def wine_suggestion():
    """Function to suggest wine."""
    if input("Do you want a wine suggestion? (yes/no): ") == "yes":
        print("We have some types of wines... red, white, or sparkling!")
        wine = input("Enter the type of wine you like: ")
        print(f"{wine.capitalize()} is an excellent choice! It pairs wonderfully with pasta.")
        print(f"Enjoy your {wine} wine with the delicious pasta we made!")
    else:
        print("No wine suggestion provided.")

def tips():
    """Function to provide cooking tips."""
    tips_list = [
        "PRO TIP: Use a good quality pasta for the best taste.",
        "PRO TIP: Don't overcook the pasta; it should be al dente.",
        "PRO TIP: Add a bit of olive oil to the pasta for extra flavor.",
        "PRO TIP: Try different types of seasonings to find your favorite.",
        "PRO TIP: Pair your pasta with a good wine for a complete meal.",
    ]
    random_tip = random.choice(tips_list)
    print(random_tip)

# Start the pasta-making process
make_pasta()