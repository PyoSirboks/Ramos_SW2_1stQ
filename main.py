from pyscript import display

#string
restaurant_name = "Niko fat cakes and eatery"
owner_name = "Pio Ramos"

#integer
year_since = 2025

#float
tax_rate = 0.08

#boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#list
product_names = ["Caldereta", "Lechon", "Pancit Canton", "Juicy Cake", "Fruity Cake"]
beverages = ["1.5 Liter Royal", "1.5 Liter Coke"]

#tuple
business_hours = ("11:00 AM", "11:00 PM")

#dictionary
menu = {
    "Caldereta": 110,
    "Lechon": 2000,
    "Pancit Canton": 35,
    "Juicy Cake": 550,
    "Fruity Cake": 600,
    "1.5 Liter Royal": 80,
    "1.5 Liter Coke": 80 
}

#set
common_allergens = {"nuts", "dairy", "gluten"}

#display restaurant info
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

#display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Caldereta']}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Lechon']}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Pancit Canton']}", target="price3")
display(product_names[3], target="prod4")
display(f"₱{menu['Juicy Cake']}", target="price4")
display(product_names[4], target="prod5")
display(f"₱{menu['Fruity Cake']}", target="price5")
display(beverages[0], target="prod6")
display(f"₱{menu['1.5 Liter Royal']}", target="price6")
display(beverages[1], target="prod7")
display(f"₱{menu['1.5 Liter Coke']}", target="price7")

#display additional info
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openinghours")

#display order type
display(f"Dine-in Available", target="orderType")