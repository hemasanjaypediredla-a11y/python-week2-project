def calculate_grade(marks):

    if marks >= 90:
        return "A", "Excellent Work! 🌟"

    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"

    elif marks >= 70:
        return "C", "Good Job 🙂"

    elif marks >= 60:
        return "D", "You can improve 💪"

    else:
        return "F", "Keep practicing and try again ❌"


name = input("Enter student name: ")

while True:

    marks = int(input("Enter marks (0-100): "))

    if marks >= 0 and marks <= 100:
        break

    else:
        print("Invalid input! Please enter marks between 0 and 100.")


grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)