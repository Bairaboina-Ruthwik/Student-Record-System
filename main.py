class Student :
    def __init__ (self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

def load_students():
    students = []

    try :
        file = open("students.txt","r")
        for line in file :  
            # another logic can be [ name, roll, marks = line.strip().split(",") ] instead of line 14-17 
            data = line.strip().split(",")
            name = data[0]
            roll = data[1]
            marks = data[2]
            # below two lines can be written as  [ students.append(Student(name, roll, marks)) ]
            student = Student(name,roll,marks)   
            students.append(student)
        file.close()
    except FileNotFoundError:
        return students
    return students

def save_student(students):
    file = open("students.txt","w")
    for student in students :
        name = student.name
        roll = student.roll
        marks = student.marks

        file.write(f"{name},{roll},{marks}\n")
    file.close()


def add_student():
    name = input("Enter Student Name :")
    roll = input("Enter Student Roll :")
    marks = input("Enter Student Marks :")
    students = load_students()
    student = Student(name,roll,marks)
    students.append(student)
    save_student(students)
    print("Student Successfully added")

def view_student():
    students = load_students()
    if(len(students)) == 0 :
        print("No Student Found")
        return
    print("\nStudent Records")
    for student in students:
        name = student.name
        roll = student.roll
        marks = student.marks

        print(f"Name : {name} ,Roll : {roll} ,Marks = {marks}")

def delete_student():
    roll_no = input("Enter Student Roll you want to delete :")

    students = load_students()
    new_students = []
    for student in students :
        if student.roll != roll_no:
            new_students.append(student)
        
    save_student(new_students)
    print("Student Successfully deleted")

def update_marks():
    roll_no = input("Enter Roll you want to update marks")
    new_marks = input("Enter NewMarks")
    students = load_students()
    for student in students :
        if roll_no == student.roll :
            student.marks = new_marks

    save_student(students)
    print("Student Marks Successfully Updated")

while True :
    print("\n-----Student Marks Record System-----\n")
    print("1. Add Students")
    print("2. View Students")
    print("3. Delete Students")
    print("4. Update Marks")
    print("5. Exit")
    choice = input("Enter your choice")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        print("program ended")  
        break
    else:
        print("Invalid Choice")

    



