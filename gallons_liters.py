# Get user input for gallons and fluid ounces
gallons = float(input("Enter volume in gallons: "))
fluid_ounces = float(input("Enter volume in fluid ounces: "))

# Convert fluid ounces to gallons and add to total gallons
total_gallons = gallons + (fluid_ounces / 128)

# Convert total gallons to liters (1 gallon = 3.78541 liters)
liters = total_gallons * 3.78541  

# Display the result
print(f"Volume in liters: {liters:.2f}")
