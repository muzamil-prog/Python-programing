students = [

    {
        "name": "Ali",
        "marks": 430
    },

    {
        "name": "Ahmed",
        "marks": 390
    },

    {
        "name": "Muzammil",
        "marks": 460
    },

    {
        "name": "Hamza",
        "marks": 410
    }

]


students.sort(
    key=lambda student: student["marks"],
    reverse=True
)


print("Student Ranking\n")


for index, student in enumerate(
    students,
    start=1
):

    print(
        "Rank:",
        index,
        "| Name:",
        student["name"],
        "| Marks:",
        student["marks"]
    )