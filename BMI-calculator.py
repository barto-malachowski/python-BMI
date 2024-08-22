def calculate_bmi(weight, height):
    bmi = weight / ((height/100) ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        
        if weight <= 0 or height <= 0:
            raise ValueError("Height and weight must be greater than 0.")
        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
