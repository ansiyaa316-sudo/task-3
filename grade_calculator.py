def get_marks():
    """Take marks input from the user."""
    try:
        return float(input("Enter marks (0-100): "))
    except ValueError:
        return -1


def calculate_grade(marks):
    """Calculate grade using conditions and business rules."""

    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter marks between 0 and 100."

    if marks >= 90:
        if marks >= 95:
            return "Grade A+ : Outstanding performance!"
        else:
            return "Grade A : Excellent work!"

    elif marks >= 75 and marks < 90:
        return "Grade B : Very good job!"

    elif marks >= 60 and marks < 75:
        return "Grade C : Good, keep improving."

    elif marks >= 40 and marks < 60:
        return "Grade D : Passed, but needs effort."

    else:
        return "Grade F : Failed. Try again."


def main():
    """Main function."""
    marks = get_marks()
    result = calculate_grade(marks)
    print(result)

if __name__ == "__main__":
    main()
