name = "Karim"
age = 20

def age_calculator(age):
    if age < 18:
        return "You are a minor."
    elif age >= 18 and age < 65:
        return "You are an adult."
    else:
        return "You are a senior citizen."

"""class Person:
    age_calculator = age_calculator
    print(age_calculator(age))"""

