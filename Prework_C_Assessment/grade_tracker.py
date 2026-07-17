"""
Project: Student Grade Tracker
Pre-Work Section C — Python Fundamentals
Estimated time: 45-60 minutes

Objective: Build a data processing script that reads student grades from
a CSV, calculates averages, assigns letter grades, and writes a summary report.

Your job: implement all the functions marked with # TODO.
Do NOT modify the function signatures or the main() function.
"""

import csv #uses CSV module to read CSV files


# ============================================================
# FUNCTION 1: Load data from CSV
# ============================================================

def load_students(filepath: str) -> list[dict]:
    students = []
    try:
        with open(filepath) as f: #Opens file
            reader = csv.DictReader(f)
            for row in reader:
                row["student_name"] = row["student_name"]
                row["math"] = (row["math"])
                row["science"] = (row["science"])
                row["english"] = (row["english"])
                row["history"] = (row["history"])
                students.append(row)
    except FileNotFoundError:#handles file not found
        print(f"Error: The file {filepath} was not found.")#gives a message if the file isnt found
    return students #returns the students as a list of dictionaries


# ============================================================
# FUNCTION 2: Calculate average, handling missing values
# ============================================================

def calculate_average(grades: list) -> float | None:

    valid_grades = []

    for grade in grades:
        try:
            # Ignore None and empty strings
            if grade is None or str(grade).strip() == "":
                continue

            numeric_grade = float(grade)#makes sure the grade is a float
            valid_grades.append(numeric_grade)

        except (ValueError, TypeError):
            # Ignore values that cannot be converted to a number
            continue

    if not valid_grades:
        return None #returns none if there are no valid grades

    average = sum(valid_grades) / len(valid_grades)
    return round(average, 1) #returns grades

   

# # ============================================================
# # FUNCTION 3: Assign letter grade
# # ============================================================

def get_letter_grade(average: float | None) -> str:   #converts the grade to a letter grade based on the average
   
    if average is None:
        return "N/A - no grades available"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
   


# # ============================================================
# # FUNCTION 4: Generate summary report
# # ============================================================

def generate_report(students: list[dict]) -> dict:
    student_summaries = []
    grade_distribution = {}
    all_averages = []#creates the lists and dictionaries needed

    subject_names = ["math", "science", "english", "history"]#notes the subjects to be used

    for student in students:
        grades = [student.get(subject) for subject in subject_names]#gets the students subject grade

        average = calculate_average(grades)#caluclates students average
        letter_grade = get_letter_grade(average)#assigns letter grade

        student_summary = {
            "name": student.get("student_name", "Unknown Student"),
            "average": average,
            "grade": letter_grade
        }#makes a summary 

        student_summaries.append(student_summary)

        grade_distribution[letter_grade] = (
            grade_distribution.get(letter_grade, 0) + 1
        )#counts and gives grade distribution 

        if average is not None:#handles none
            all_averages.append(average)

    if all_averages:#handles average levels
        class_average = round(
            sum(all_averages) / len(all_averages),
            1
        )
        highest_average = max(all_averages)
        lowest_average = min(all_averages)
    else:
        class_average = None
        highest_average = None
        lowest_average = None

    return {
        "total_students": len(students),
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "grade_distribution": grade_distribution,
        "students": student_summaries #returns all created
    }
   


# # ============================================================
# # FUNCTION 5: Write report to a file
# # ============================================================

def write_report(report: dict, filepath: str) -> None:
    
    def format_average(value: float | None) -> str:
        
        if value is None:
            return "N/A"

        return f"{value:.1f}"

    with open(filepath, "w", encoding="utf-8") as file:
        file.write("=" * 45 + "\n")
        file.write("STUDENT GRADE REPORT\n")
        file.write("=" * 45 + "\n\n")#header

        file.write(
            f"Total students:   {report['total_students']}\n"
        )#writes total students
        file.write(
            f"Class average:    "
            f"{format_average(report['class_average'])}\n"
        )#writes class average
        file.write(
            f"Highest average:  "
            f"{format_average(report['highest_average'])}\n"
        )#writes highest average
        file.write(
            f"Lowest average:   "
            f"{format_average(report['lowest_average'])}\n"
        )#writes lowest average

        file.write("\nGrade Distribution:\n")

        grade_order = ["A", "B", "C", "D", "F", "N/A"]

        for grade in grade_order:
            count = report["grade_distribution"].get(grade, 0)
            file.write(f"  {grade}: {count}\n")
            #writes grade distribution

        file.write("\nIndividual Results:\n")#writes individual results for students

        for student in report["students"]:
            name = student["name"]
            average = format_average(student["average"])
            grade = student["grade"]

            file.write(
                f"  {name:<20} "
                f"Avg: {average:>5}  "
                f"Grade: {grade}\n"
            )


# # ============================================================
# # MAIN — do not modify
# # ============================================================

def main():#main unaltered
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")

    print("Generating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")
    for grade, count in sorted(report["grade_distribution"].items()):
        print(f"  {grade}: {count}")

    print("\nTop 5 students:")
    sorted_students = sorted(
        [s for s in report["students"] if s["average"] is not None],
        key=lambda s: s["average"],
        reverse=True
    )
    for s in sorted_students[:5]:
        print(f"  {s['name']:<20} {s['average']:.1f}  ({s['grade']})")

    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
    main()