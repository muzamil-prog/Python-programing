class Student:
    def __init__(self , student_Id, name, math , computer , Ai):
        self.student_Id=student_Id
        self.name=name
        self.math=math
        self.computer=computer
        self.Ai=Ai
    def __str__(self):
        return f"""
        Student_Id: {self.student_Id}
        Name: {self.name}
        Math: {self.math}
        Computer: {self.computer}
        AI: {self.Ai}
        """
    def calculateTotal(self):
         return self.math+self.computer+self.Ai
    def calculateAverage(self):
         total=self.calculateTotal()
         return total/3  
    def calculateGrade(self):
        average=self.calculateAverage()
        if average>=90:
            return 'A'
        elif average>=80:
            return 'B'
        elif average>=70:
            return 'C'
        elif average>=60:
            return 'D'
        else: 
            return 'F'  
    def isPasss(self):
        average=self.calculateAverage()
        if average>=50:
            return True
        else:
            return False                              