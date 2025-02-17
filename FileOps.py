FILE_NAME = "students.txt"

def load_data():
    try:
        with open(FILE_NAME) as file:
            return [dict(zip(["name", "age", "grade"], line.strip().split(','))) for line in file]
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_NAME, 'w') as file:
        file.writelines(f"{s['name']},{s['age']},{s['grade']}\n" for s in data)

def add_student():
    data = load_data()
    data.append({k: input(f"{k.capitalize()}: ") for k in ["name", "age", "grade"]})
    save_data(data)
    print("Student added!")

def view_students():
    students = load_data()
    print("No students found." if not students else "\n".join(map(str, students)))

# Run the program
print("Adding a new student:")
add_student()
print("\nViewing all students:")
view_students()



