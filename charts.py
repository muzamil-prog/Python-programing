import matplotlib.pyplot as plt


class Charts:

    def showStudentAverageChart(self, students):

        names = []
        averages = []

        for student in students:

            names.append(student.name)
            averages.append(student.calculateAverage())

        plt.figure(figsize=(8, 5))

        plt.bar(names, averages)

        plt.title("Student Average Marks")

        plt.xlabel("Students")

        plt.ylabel("Average Marks")

        plt.show()
    def showGradeDistributionChart(self, students):

         grades = ["A", "B", "C", "D", "F"]
         counts = [0, 0, 0, 0, 0]

         for student in students:

             grade = student.calculateGrade()

             if grade == "A":
                 counts[0] += 1

             elif grade == "B":
                 counts[1] += 1

             elif grade == "C":
                 counts[2] += 1

             elif grade == "D":
                 counts[3] += 1

             else:
                 counts[4] += 1

         plt.figure(figsize=(8, 5))

         plt.bar(grades, counts)

         plt.title("Grade Distribution")

         plt.xlabel("Grades")

         plt.ylabel("Number of Students")

         plt.show()        
    def showPassFailChart(self, students):

         pass_count = 0
         fail_count = 0

         for student in students:

             if student.isPasss():
                 pass_count += 1
             else:
                 fail_count += 1

         labels = ["Pass", "Fail"]
         values = [pass_count, fail_count]

         plt.figure(figsize=(6, 6))

         plt.pie(values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90)

         plt.title("Pass vs Fail Analysis")

         plt.show()    