print("🧮 Rectangle Area Calculator")
print("This program calculates the area of a rectangle,")
print("allowing you to enter width and height in different units.")
print("You can also choose the unit in which to display the result.\n")

print("🔧 Steps:")
print("1. Choose a unit for the width")
print("2. Enter the width value")
print("3. Choose a unit for the height")
print("4. Enter the height value")
print("5. Choose a unit for the result\n")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid number (e.g., 8.9)")

# 🔧 Conversion factors to meters
unit_to_meter = {
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "in": 0.0254
}

# 🧠 Unit selection for width
print("Choose the unit for width:")
for i, unit in enumerate(unit_to_meter.keys(), start=1):
    print(f"{i} - {unit}")

unit_list = list(unit_to_meter.keys())
unit_choice = input("Enter unit number: ")

if unit_choice.isdigit() and 1 <= int(unit_choice) <= len(unit_list):
    width_unit = unit_list[int(unit_choice) - 1]
else:
    print("❌ Invalid choice. Defaulting to meters.")
    width_unit = "m"

# 📏 Input width
width_raw = get_positive_float(f"Enter width ({width_unit}): ")
width_meters = width_raw * unit_to_meter[width_unit]

# 🧠 Unit selection for height
print("\nChoose the unit for height:")
for i, unit in enumerate(unit_to_meter.keys(), start=1):
    print(f"{i} - {unit}")

unit_choice = input("Enter unit number: ")

if unit_choice.isdigit() and 1 <= int(unit_choice) <= len(unit_list):
    height_unit = unit_list[int(unit_choice) - 1]
else:
    print("❌ Invalid choice. Defaulting to meters.")
    height_unit = "m"

# 📏 Input height
height_raw = get_positive_float(f"Enter height ({height_unit}): ")
height_meters = height_raw * unit_to_meter[height_unit]

# 🔧 Conversion factors from square meters
area_unit_map = {
    "m²": 1,
    "cm²": 10_000,
    "mm²": 1_000_000,
    "in²": 1550.0031  # approximate value
}

# 🧠 Unit selection for result
print("\nChoose the unit for the result:")
for i, unit in enumerate(area_unit_map.keys(), start=1):
    print(f"{i} - {unit}")

area_unit_list = list(area_unit_map.keys())
area_choice = input("Enter unit number: ")

if area_choice.isdigit() and 1 <= int(area_choice) <= len(area_unit_list):
    result_unit = area_unit_list[int(area_choice) - 1]
else:
    print("❌ Invalid choice. Defaulting to m².")
    result_unit = "m²"

# 📐 Area calculation
area_m2 = width_meters * height_meters
area_converted = area_m2 * area_unit_map[result_unit]

# 🖨️ Output result
print("\n✅ Calculation complete.")
print(f"Rectangle area: {area_converted:.2f} {result_unit}")