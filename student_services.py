import pandas as pd
from model.student import Student
class studentServices:
    def load_student(self):
        df=pd.read_csv("data/students.csv")
        students=[]

        for index, row in df.iterrows():
            student=Student(
                row[ "student_id"],
                row["name"],
                row["math"],
                row["computer"],
                row["Ai"]
                
            )
            students.append(student)
        return students  
    def SearchStudent(self, students, student_id):
        
        for student in students:
            if student.student_Id==student_id:
                return student      

        return None    
    def SearchStudentName(self, students, Sname):
        for student in students:
            if student.name.strip().lower()==Sname.strip().lower():
                return student
        return None    
    def getTopper(self, students):
             if len(students) == 0:
                  return None

             topper = students[0]
             for student in students:
                  if student.calculateAverage() > topper.calculateAverage():
                        topper = student 
             
             return topper
    def getFailedStudents(self, students):
         failed_students = []
         for student in students:

             if not student.isPasss():
                 failed_students.append(student)

         return failed_students   
    def getPassedStudents(self, students):

         passed_students = []

         for student in students:

             if student.isPasss():

                 passed_students.append(student)

         return passed_students
    def getClassStatistics(self, students):

         total_students = len(students)
         total_pass = 0
         total_fail = 0
         total_average = 0

         topper = students[0]
         lowest = students[0]

         for student in students:

             average = student.calculateAverage()

             total_average += average

             if student.isPasss():
                 total_pass += 1
             else:
                 total_fail += 1

             if average > topper.calculateAverage():
                 topper = student

             if average < lowest.calculateAverage():
                 lowest = student

         class_average = total_average / total_students

         return {
        "total_students": total_students,
        "total_pass": total_pass,
        "total_fail": total_fail,
        "class_average": class_average,
        "topper": topper,
        "lowest": lowest
         }  

             
    def saveStudents(self, students):

         data = []

         for student in students:

             row = {
            "student_id": student.student_Id,
            "name": student.name,
            "math": student.math,
            "computer": student.computer,
            "Ai": student.Ai
             }

             data.append(row)

         df = pd.DataFrame(data)

         df.to_csv("data/students.csv", index=False)

         print("Students saved successfully.")
    def addStudent(self, students):

         student_id = int(input("Enter Student ID: "))

         if self.SearchStudent(students, student_id):
              print("Student ID already exists.")
              return

         name = input("Enter Name: ")

         math = float(input("Enter Math Marks: "))
         computer = float(input("Enter Computer Marks: "))
         ai = float(input("Enter AI Marks: "))

         new_student = Student(student_id, name,math,computer,ai)

         students.append(new_student)

         self.saveStudents(students)

    def updateStudent(self, students):

         student_id = int(input("Enter Student ID to Update: "))

         student = self.SearchStudent(students, student_id)

         if student is None:
             print("Student not found.")
             return

         print("\nCurrent Student Information")
         print(student)

         student.name = input("Enter New Name: ")
         student.math = float(input("Enter New Math Marks: "))
         student.computer = float(input("Enter New Computer Marks: "))
         student.Ai = float(input("Enter New AI Marks: "))

         self.saveStudents(students)

         print("Student updated successfully.")
    def deleteStudent(self, students):

         student_id = int(input("Enter Student ID to Delete: "))

         student = self.SearchStudent(students, student_id)

         if student is None:
             print("Student not found.")
             return

         print("\nStudent Found")
         print(student)

         confirm = input("Are you sure? (Y/N): ").strip().upper()

         if confirm == "Y":

             students.remove(student)

             self.saveStudents(students)

             print("Student deleted successfully.")

         else:

             print("Delete operation cancelled.") 