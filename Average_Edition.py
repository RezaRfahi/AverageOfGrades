# تابعی که  میانگین نمرات را حساب میکند
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

# تابع اصلی برنامه
def calculate_student_grades():
    # دیکشنری  برای ذخیره اسامی دانش آموزان و نمرات آنها
    student_grades = {}

    # لیست درس ها
    subjects = ["Math", "English", "Science"]

    # دریافت تعداد دانش آموزان را از کاربر
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # وارد کردن نمره برای هر دانش آموز
    for i in range(1, num_students + 1):
        student_name = input(f"Enter the name of student {i}: ")
        grades = []

        # وارد کردن نمره برای هر درس
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"Enter the {subject} grade (between 0 and 20): "))
                    if 0 <= grade <= 20:
                        grades.append(grade)
                        break
                    else:
                        print("Please enter a grade between 0 and 20.")
                except ValueError:
                    print("Please enter a valid numeric grade.")

        # محاسبه میانگین نمرات
        average_grade = calculate_average(grades)

        # ذخیره اطلاعات دانشجو در دیکشنری
        student_grades[student_name] = {subject: grade for subject, grade in zip(subjects, grades)}
        student_grades[student_name]["Average"] = average_grade

    # چاپ نمرات و معدل هر دانش آموز
    print("\nStudent Grades:")
    for student, grades_info in student_grades.items():
        print(f"\n{student}'s Grades:")
        for subject, grade in grades_info.items():
            print(f"{subject}: {grade}")
        print(f"Average: {grades_info['Average']:.2f}")

# تابع اصلی رو صدا میزنیم
calculate_student_grades()
