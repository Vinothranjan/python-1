# Employee Payroll Management without using list, dictionary or tuple

def calculate_pay(basic, hra, da, deductions):
    gross = basic + hra + da
    net = gross - deductions
    return gross, net

print("=== Employee Payroll Management ===\n")

# Input for one employee
emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")

basic = float(input("Enter Basic Salary: "))

# Explain HRA and DA before input
print("\nHRA House Rent Allowance")
hra = float(input("Enter HRA amount: "))

print("\nDA Dearness Allowance")
da = float(input("Enter DA amount: "))

deductions = float(input("\nEnter Deductions: "))

# Calculate
gross, net = calculate_pay(basic, hra, da, deductions)

# Output
print("\n-------EMPLOYEE PAYROLL--------")
print("Employee ID   :", emp_id)
print("Employee Name :", emp_name)
print("Basic Salary  :", basic)
print("HRA (House Rent Allowance)           :", hra)
print("DA (Dearness Allowance)              :", da)
print("Deductions    :", deductions)
print("Gross Salary  :", gross)
print("Net Salary    :", net)
print("-------------------------------")
