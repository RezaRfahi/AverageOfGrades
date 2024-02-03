# تابع برای محاسبه میانگین نمره
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

# تابع اصلی برای ورودی نمرات و محاسبه میانگین
def calculate_student_grades():
    # فرهنگ لغت برای ذخیره اسامی دانش آموزان و نمرات آنها
    student_grades = {}

    # تعداد دانش آموزان را از کاربر دریافت کنید
    try:
        num_students = int(input("Please Enter the number of students: "))
    except ValueError:
        print("Please Enter a Valid Score: ")
        return

    # نمرات ورودی برای هر دانش آموز
    for i in range(1, num_students + 1):
        student_name = input(f"Enter the name of student {i}: ")
        
        # نمرات ورودی برای هر موضوع
        try:
            math_grade = float(input("Enter the math score (between 0 and 20): "))
            if not 0 <= math_grade <= 20:
                print("Please enter a score between 0 and 20.")
                return

            english_grade = float(input("Enter your English score (between 0 and 20): "))
            if not 0 <= english_grade <= 20:
                print("Please enter a score between 0 and 20.")
                return

            science_grade = float(input("Enter your science score (between 0 and 20): "))
            if not 0 <= science_grade <= 20:
                print("Please enter a score between 0 and 20.")
                return
        except ValueError:
            print("Please enter valid numerical grades.")
            return

        # میانگین نمرات دانش آموز را محاسبه کنید
        grades = [math_grade, english_grade, science_grade]
        average_grade = calculate_average(grades)

        # اطلاعات دانش آموز را در فرهنگ لغت ذخیره کنید
        student_grades[student_name] = {
            "Math": math_grade,
            "English": english_grade,
            "Science": science_grade,
            "Average": average_grade
        }
    # نمرات و معدل هر دانش آموز را چاپ کنید
    print("\nStudents' scores: ") 
    for student, grades_info in student_grades.items():
        print(f"\nScores {student}: ")
        for subject, grade in grades_info.items(): 
            print(f"{subject}: {grade}")
        print(f"Average: {grades_info['Average']:.2f}")


# تابع اصلی را فراخوانی کنید
calculate_student_grades()
