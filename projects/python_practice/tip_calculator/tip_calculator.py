print("Welcome to the Tip Calculator!")

bill = float(input("What is your total bill?: $"))
user_Tip_Percentage = int(input("What % tip are you wanting to give?: %"))
tip_Percentage = bill * (user_Tip_Percentage / 100)

final_Bill = bill + tip_Percentage
print(f"your tip is {tip_Percentage} and your final bill is ${final_Bill}")