gallons = float(input("Enter volume in gallons: "))

fluid_ounces = float(input("Enter volume in fluid ounces:  "))

#Convert fluid ounces to gallons and add to total gallonn
total_gallons = gallons + (fluid_ounces/128)

#Convert total gallons to liters
liters = total_gallons/0.264172

print(f"Volume in liters:  {liters:.2f}")