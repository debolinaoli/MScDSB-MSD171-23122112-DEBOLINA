class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def get_marks(self, subject):
        return self.marks.get(subject, "Subject not found")

    def get_average_marks(self):
        if not self.marks:
            return "No marks available"
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

def main():
    students = {}
    
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Add Marks for a Student")
        print("3. Get Marks for a Student")
        print("4. Get Average Marks for a Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            roll_number = input("Enter student's roll number: ")
            student = Student(name, roll_number)
            students[roll_number] = student
            print(f"Student {name} with roll number {roll_number} added.")

        elif choice == "2":
            roll_number = input("Enter student's roll number: ")
            student = students.get(roll_number)
            if student:
                subject = input("Enter subject name: ")
                mark = float(input("Enter mark for the subject: "))
                student.add_mark(subject, mark)
                print(f"Mark {mark} added for {subject} for {student.name}.")

            else:
                print("Student not found.")

        elif choice == "3":
            roll_number = input("Enter student's roll number: ")
            student = students.get(roll_number)
            if student:
                subject = input("Enter subject name: ")
                mark = student.get_marks(subject)
                print(f"Mark for {subject}: {mark}")

            else:
                print("Student not found.")

        elif choice == "4":
            roll_number = input("Enter student's roll number: ")
            student = students.get(roll_number)
            if student:
                average = student.get_average_marks()
                print(f"Average marks for {student.name}: {average}")

            else:
                print("Student not found.")
        
        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__1":
    main()