meals = []

def add_meal(name, calories):
    meals.append({"meal": name, "calories": calories})
    print(f"✅ {name} added with {calories} calories")

def show_meals():
    if not meals:
        print("No meals logged yet.")
        return
    total = 0
    print("\nYour Meals:")
    for m in meals:
        print(f"- {m['meal']} : {m['calories']} cal")
        total += m['calories']
    print(f"\n🔥 Total Calories: {total}")

# Demo Run
add_meal("Breakfast - Oats", 250)
add_meal("Lunch - Rice & Dal", 600)
show_meals()
