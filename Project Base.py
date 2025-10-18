class Student:

    def __init__(self,name,marks,roll):
        self.name=name
        self.marks=marks
        self.roll=roll
    
    def display(self):
        return (f"{self.name} | {self.roll} | {self.marks}")

def search_by_roll(roll):
        for i in student:
            if i.roll == roll:
                return i
        return None

def save_to_file():
     with open("Student.txt","w") as f:
            for s in student:
                f.write(f"{s.name} | {s.roll} | {s.marks}\n")
student=[]

try:
    with open("Student.txt", "r") as f:
        for line in f:
            name, roll, marks = line.strip().split(" | ")
            student.append(Student(name, int(marks), int(roll)))
except FileNotFoundError:
    pass

while True:
    menu = int(input("\nWhat do you want to do?\n"
                         "1. Add student details\n"
                         "2. Display students\n"
                         "3. Search name by roll no\n"
                         "4. Delete student by roll number\n"
                         "5. Update student marks by roll number\n"
                         "6. Save and Exit\nChoice: "))
    
    if menu == 1:
        name=input("Enter Name of Student:")
        try:
            roll = int(input("Enter Roll No of student: "))
        except ValueError:
            print("Invalid input. Please Enter a Number.")
            continue
        try:
            marks = int(input("Enter Marks: "))
        except ValueError:
            print("Invalid input. Please Enter a Number.")
            continue
        print("\nStudent Added in file")
        s=Student(name,marks,roll)
        student.append(s)

    elif menu == 2:
        if not student:
            print("No Student Added Yet ")
        else:
            for i in student:
                print(i.display())

    elif menu == 3:
        try:
            search=int(input("Enter the roll No of student you want to search:"))
        except ValueError:
            print("Invalid input. Enter a Valid Number")
            continue
        result=search_by_roll(search)
        if result:
            print("Found:",result.name)
        else:
            print("Student Not Found")

    elif menu == 4:
        try:
            delete=int(input("Enter the Roll No of Student you want to Delete:"))
        except ValueError:
            print("Invalid input. enter a valid number")
            continue
        result=search_by_roll(delete)
        if result:
            print(f"{result.name} is Deleted!")
            student.remove(result)
        else:
            print("Student Not Found")
    elif menu == 5:
        try:
            update=int(input("Enter Roll No to Update:"))
        except ValueError:
            print("Invalid input. Enter a valid Number")
            continue
        result=search_by_roll(update)
        if result:
            result.marks=int(input("Enter New Marks:"))
            print("Marks updated for", result.name)
        else:
            print("Not found")

    elif menu == 6:
        save_to_file()
        print("Records Auto-saved. Exiting...")
        break