import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

# Ingredients dictionary to track available ingredients
ingredients = {
    "flour": 10.0,
    "eggs": 4.0,
    "water": 66.0,
    "sauce": 3.0,
}

# Pasta recipes
recipes = {
    "Basic Pasta": {"flour": 2, "eggs": 2, "water": 0.5, "sauce": 0.2},
    "Tomato Pasta": {"flour": 2, "eggs": 2, "water": 0.5, "sauce": 0.3},
}

class PastaMakerApp:
    def __init__(self, master):
        self.master = master
        master.title("Pasta Maker")

        # Welcome label
        self.label = tk.Label(master, text="Welcome to the Pasta Maker!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Recipe selection
        self.recipe_label = tk.Label(master, text="Select a Recipe:")
        self.recipe_label.pack()
        self.recipe_var = tk.StringVar(value="Basic Pasta")
        self.recipe_dropdown = tk.OptionMenu(master, self.recipe_var, *recipes.keys())
        self.recipe_dropdown.pack(pady=5)

        # Status label
        self.status_text = tk.StringVar()
        self.status_label = tk.Label(master, textvariable=self.status_text, font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(master, length=300, mode='determinate')
        self.progress.pack(pady=10)

        # Buttons
        self.make_pasta_button = tk.Button(master, text="Make Pasta", command=self.make_pasta)
        self.make_pasta_button.pack(pady=5)

        self.ingredient_status_button = tk.Button(master, text="Check Ingredients", command=self.check_ingredients)
        self.ingredient_status_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def check_ingredients(self):
        """Display the current status of ingredients."""
        status = "\n".join([f"{ingredient}: {amount} cups" for ingredient, amount in ingredients.items()])
        messagebox.showinfo("Ingredient Status", status)

    def make_pasta(self):
        """Simulate the process of making pasta."""
        selected_recipe = recipes[self.recipe_var.get()]
        if not self.check_recipe_ingredients(selected_recipe):
            return
        
        self.status_text.set("Starting to make pasta...")
        self.master.update()
        self.progress['value'] = 0

        self.add_ingredient("flour", selected_recipe["flour"])
        self.add_ingredient("eggs", selected_recipe["eggs"])
        self.add_ingredient("water", selected_recipe["water"])
        self.boil_water()
        self.cut_noodles()
        self.cook_pasta()
        self.add_sauce(selected_recipe["sauce"])
        self.plate_pasta()
        self.suggest_wine()
        self.give_tips()
        self.status_text.set("Pasta is ready!")

    def check_recipe_ingredients(self, recipe):
        """Check if enough ingredients are available for the selected recipe."""
        for ingredient, amount in recipe.items():
            if ingredients.get(ingredient, 0) < amount:
                messagebox.showerror("Insufficient Ingredients", f"Not enough {ingredient}! Required: {amount}, Available: {ingredients[ingredient]}")
                return False
        return True

    def add_ingredient(self, ingredient, amount):
        """Add ingredient to the pasta."""
        self.status_text.set(f"Adding {ingredient}...")
        self.master.update()
        time.sleep(1)
        ingredients[ingredient] -= amount  # Deduct the ingredient
        self.status_text.set(f"{ingredient.capitalize()} added. Remaining: {ingredients[ingredient]} cups.")
        self.update_progress()

    def boil_water(self):
        """Simulate boiling water."""
        self.status_text.set("Boiling water...")
        self.master.update()
        time.sleep(3)  # Simulate boiling time
        self.status_text.set("Water boiled.")
        self.update_progress()

    def cut_noodles(self):
        """Simulate cutting noodles."""
        self.status_text.set("Cutting noodles...")
        self.master.update()
        time.sleep(2)  # Simulate cutting time
        self.status_text.set("Noodles cut.")
        self.update_progress()

    def cook_pasta(self):
        """Simulate cooking pasta."""
        self.status_text.set("Cooking pasta...")
        self.master.update()
        time.sleep(4)  # Simulate cooking time
        self.status_text.set("Pasta cooked.")
        self.update_progress()

    def add_sauce(self, amount):
        """Simulate adding sauce."""
        self.status_text.set(f"Adding sauce ({amount} cups)...")
        self.master.update()
        time.sleep(1)  # Simulate time for adding sauce
        ingredients["sauce"] -= amount  # Deduct the sauce
        self.status_text.set(f"Sauce added. Remaining: {ingredients['sauce']} cups.")
        self.update_progress()

    def plate_pasta(self):
        """Simulate plating the pasta."""
        self.status_text.set("Plating pasta...")
        self.master.update()
        time.sleep(1)  # Simulate time for plating
        self.status_text.set("Pasta plated.")
        self.update_progress()

    def suggest_wine(self):
        """Suggest a wine to pair with the pasta."""
        wines = ["Chianti", "Sangiovese", "Pinot Grigio", "Barbera"]
        suggested_wine = random.choice(wines)
        self.status_text.set(f"Suggested wine: {suggested_wine}")

    def give_tips(self):
        """Provide cooking tips."""
        tips_list = [
            "Always use fresh ingredients for the best flavor.",
            "Let the pasta rest for a few minutes before serving.",
            "Pair your pasta with a good wine for a complete meal.",
            "Experiment with herbs and spices to enhance the flavor."
        ]
        random_tip = random.choice(tips_list)
        self.status_text.set(f"Tip: {random_tip}")

    def update_progress(self):
        """Update the progress bar."""
        self.progress['value'] += (100 / 7)  # Assuming 7 steps in total
        if self.progress['value'] >= 100:
            self.progress['value'] = 100

if __name__ == "__main__":
    root = tk.Tk()
    app = PastaMakerApp(root)
    root.mainloop()