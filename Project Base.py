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
                         "6. Delete all data in the file\n"
                         "7. Save and Exit\n\nChoice: "))
    
    if menu == 1:
        name=input("Enter Name of Student:")
        try:
            roll = int(input("Enter roll no of the Student: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        try:
            marks = int(input("Enter marks of the student: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        print("\nStudent added in file")
        s=Student(name,marks,roll)
        student.append(s)
        print(f"\nStudent '{name}' added successfully!")

    elif menu == 2:
        if not student:
            print("No student added yet ")
        else:
            for i in student:
                print(i.display())

    elif menu == 3:
        try:
            search=int(input("Enter the roll number of student you want to search:"))
        except ValueError:
            print("Invalid input. Enter a valid number")
            continue
        result=search_by_roll(search)
        if result:
            print(" Student found:",result.name)
        else:
            print("Student Not Found")

    elif menu == 4:
        try:
            delete=int(input("Enter the roll no of student you want to delete:"))
        except ValueError:
            print("Invalid input. enter a valid number")
            continue
        result=search_by_roll(delete)
        if result:
            print(f"{result.name}has been deleted.")
            student.remove(result)
        else:
            print("Student Not Found")
    elif menu == 5:
        try:
            update=int(input("Enter the roll number to update marks: "))
        except ValueError:
            print("Invalid input.Please enter a valid number")
            continue
        result=search_by_roll(update)
        if result:
            result.marks=int(input(f"Enter new marks for {result.name}: "))
            print("Marks updated for", result.name)
        else:
            print("Student not found")
    elif menu == 6:
        with open('student.txt','w') as f:
            pass
        student.clear()
        print("All student data has been deleted from memory and file")
    elif menu == 7:
        save_to_file()
        print("Records saved. Exiting...")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")