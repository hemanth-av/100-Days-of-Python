print("Welcome to thr Tip Calculator...!!")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage Tip wouldyou like to give?10, 12, 15 \n"))
people = int(input("How many people to split the bill?\n"))

total_bill = bill * (1 + (tip / 100))
final_bill = total_bill / people

print("Total bill : ", final_bill)
