# 🧮 Rectangle Area Calculator

A simple and user-friendly Python program to calculate the **area of a rectangle**.  
Users can enter the **width and height** in different units and choose the **desired output unit** (e.g., square meters, square centimeters, square inches, etc.).

---

## ✅ Features

- Supports multiple units for input:
  - `m` (meters)
  - `cm` (centimeters)
  - `mm` (millimeters)
  - `in` (inches)
- Converts all input to meters for consistent calculations
- Outputs result in chosen unit:
  - `m²`, `cm²`, `mm²`, or `in²`
- Validates input to prevent:
  - negative or zero values
  - non-numeric input
  - invalid unit selections
- Works entirely in the terminal (CLI)

---

## 📦 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/rectangle-area-calculator.git
cd rectangle-area-calculator

2. Run the script:
python3 rectangle_area_calculator_v2.py

🖥️ Example
🧮 Rectangle Area Calculator
This program allows you to calculate the area of a rectangle
with width and height in different units.

🔧 Steps:
1. Choose unit for width
2. Enter width value
3. Choose unit for height
4. Enter height value
5. Choose unit for the result

Choose width unit:
1 - m
2 - cm
3 - mm
4 - in
Enter unit number: 2
Enter width (cm): 150
...

✅ Calculation complete.
Rectangle area: 45000.00 cm²

## 🧪 Tests

This project includes unit tests for the core function `calculate_area()`.

To run the tests:

```bash
python3 -m unittest test_rectangle_area.py
The tests cover:

✅ Valid input
🚫 Zero and negative values
🧨 Non-numeric input types

📄 License
MIT License (optional — can be added later)

🙌 Author
Created by DevJunZero – feel free to fork, star, or contribute!
