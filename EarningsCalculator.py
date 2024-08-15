save = int(input("How much money do you want to save in a year?"))
month = round(save/12, 2)
week = round(save/52, 2)
day = round(save/365, 2)

print(f"To save up {save} dollars in one year, you will need to save {month} per month.")
print(f"To save up {save} dollars in one year, you will need to save {week} per week.")
print(f"To save up {save} dollars in one year, you will need to save {day} per day.")
