def bmi_calculator(weight, height):
  """Calculates the BMI of a person.

  Args:
    weight: The weight of the person in kilograms.
    height: The height of the person in meters.

  Returns:
    The BMI of the person.
  """

  bmi = weight / height ** 2
  return bmi


if __name__ == "__main__":
  weight = float(input("Enter your weight in kilograms: "))
  height = float(input("Enter your height in meters: "))
  bmi = bmi_calculator(weight, height)
  print("Your BMI is:", bmi)
