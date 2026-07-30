from model.student import Student
from services.student_services import studentServices
def main():
    print("program are start from here")
    services=studentServices()
    students=services.load_student()
    student1= Student(101, "Ali", 90 , 92, 88)
    student2= Student(102, "Muzammil Hussain", 92, 94, 90)
    student3= Student(103, "Ahmad", 88, 90, 70)
    student4= Student(104, "Sufyan", 44, 45, 49)
    students=[student1, student2, student3, student4]
    for student in students:
     print(student)
     print("Tatal_Marks:", student.calculateTotal())
     print("Average Marks:", student.calculateAverage())
     print("Grade :", student.calculateGrade())
     
     print("Status", student.isPasss())

if __name__=="__main__":
     main()
