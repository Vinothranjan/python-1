# Student Mark Statement using lists, dictionaries, and tuples

# Step 1: Define subjects as a tuple (fixed set)
subjects = ("Maths", "Science", "English", "History")

# Step 2: Ask how many students
num_students = int(input("Enter number of students: "))

# Step 3: Collect student marks into a dictionary
students = {}  # name -> list of marks
for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []  # list to store marks for this student
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)
    students[name] = marks

# Step 4: Function to calculate total, average, and grade
def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"
    return total, average, grade

# Step 5: Print mark statement
print("\n" + "STUDENT MARK STATEMENT".center(60, "-"))
header = f"{'Name':<12}" + "".join([f"{sub:<10}" for sub in subjects]) + f"{'Total':<8}{'Avg':<8}{'Grade':<6}"
print(header)
print("-" * 60)

for name, marks in students.items():
    total, avg, grade = calculate_result(marks)
    marks_str = "".join([f"{m:<10}" for m in marks])
    print(f"{name:<12}{marks_str}{total:<8}{avg:<8.2f}{grade:<6}")

print("-" * 60)
