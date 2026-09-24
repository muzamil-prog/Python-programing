import pandas as pd

# Define the student data
data = {
    "#": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Name": [
        "Muhammad Haziq Ali", "Hussnain QAMAR", "Muhammad hassam", 
        "Saif ur Rehman", "Azan Javed", "Rana Imran", 
        "Abdullah Zulfiqar", "Ali raza", "Shehryar Fareed", 
        "Hamza Nadeem", "Abdul Samad Nadeem"
    ],
    "Registration No": [
        "2024F-mulug-0557", "2024F-mulug-1702", "2022F-mulbscs-090", 
        "2024F-mulug-0340", "2025F-mulug-0844", "2026S-mulug-05-0036", 
        "2023F-mulbscs-034", "353024585 2209", "2024F-mulug-1424", 
        "20226S-mulug-0314", "20205F-mulug-0045"
    ],
    "Semester": [
        "4th-A", "5th", "8th", "5th", "4th", 
        "6th", "7th", "5th", "5th", "2nd", "3rd"
    ],
    "Department": [
        "Computer Science", "Economics", "Computer Science", 
        "Computer Science", "Computer Science", "Information Technology", 
        "Computer Science", "Chemical Engineering", "BS Mass Comm", 
        "Human Nutrition and Dietetics", "Electrical Engineering"
    ]
}

# Create DataFrame and export to Excel
df = pd.DataFrame(data)
df.to_excel("Student_Registration_Data.xlsx", index=False)

print("Excel file 'Student_Registration_Data.xlsx' created successfully!")