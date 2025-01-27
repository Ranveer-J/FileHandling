FILE_NAME = "students.txt"

def load_data():
    try:
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            data = []
            for line in lines:
                name, age, grade = line.strip().split(',')
                data.append({"name": name, "age": age, "grade": grade})
            return data
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_NAME, 'w') as file:
        for student in data:
            file.write(f"{student['name']},{student['age']},{student['grade']}\n")

def add_student():
    data = load_data()
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    data.append({"name": name, "age": age, "grade": grade})
    save_data(data)
    print("Student added!")

def view_students():
    data = load_data()
    if not data:
        print("No students found.")
        return
    for student in data:
        print(student)

# Direct execution
print("Adding a new student:")
add_student()

print("\nViewing all students:")
view_students()
