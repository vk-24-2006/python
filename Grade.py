def calculate_total(marks):
    return sum(marks)

def calculate_average(total, num_subjects):
    return total / num_subjects

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def display_results(students):
    print("\n----- Student Results -----")
    print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "Name", "Sub1", "Sub2", "Sub3", "Total", "Average", "Grade"
    ))
    for student in students:
        name, marks, total, avg, grade = student
        print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10.2f} {:<10}".format(
            name, marks[0], marks[1], marks[2], total, avg, grade
        ))
