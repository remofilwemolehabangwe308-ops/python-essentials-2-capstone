from models import Student 
from models import HonoursStudent

from data_tools import generate_data_file
from data_tools import load_students
from data_tools import export_report
from data_tools import log_event

from analytics import passing_students
from analytics import grade_50
from analytics import grade_80
from analytics import class_average
from analytics import highest
from analytics import lowest
from analytics import pass_rate

from reporting import environment_report
from reporting import date_report

students_data = []

while True:
    print(f"===== STUDENT ANALYTICS TOOLKIT =====\n1.Generate student data\n2.Display all student\n3.Display passing students\n4.Show class average\n5.Show highest score\n6.Show lowest score\n7.Show pass rate\n8.Show reports\n9.Exit")
    try:
        option = int(input("Enter option: ")) 
    except ValueError:
        print("Invalid option")
        continue

    if option == 1:
        generate_data_file()
        print("Student data generated successfully")

    elif option == 2:
        print("=== Class Data ===")
        students_data = load_students()
        for index, (name, score) in enumerate(students_data, start=1):
            student_id = f"S{index}"
            students_info = Student(name, student_id, score)
            print(students_info)
        research_topic = "Statistics"
        honours_class_info= HonoursStudent(name, student_id, score, research_topic)
        print(honours_class_info)

    elif option == 3:
        print("=== Passing Students ===")
        passing_data = passing_students(students_data)
        for name, score in passing_data:
            print(f"{name} | Score: {score}")

    elif option == 4:
        print("=== Class Average ===")
        class_average_data = class_average(students_data)
        print(class_average_data)

    elif option == 5:
        print("=== Highest Score ===")
        highest_score = highest(students_data)
        print(f"Highest score: {highest_score[0]} | Score: {highest_score[1]}")

    elif option == 6:
        print("=== Lowest Score ===")
        lowest_score = lowest(students_data)
        print(f"Lowest score: {lowest_score[0]} | Score: {lowest_score[1]}")

    elif option == 7:
        print("=== Pass Rate ===")
        if not students_data:
            print("No student data available. Please generate and load student data first.")
            continue
        data_pass_rate = pass_rate(students_data)
        print(data_pass_rate)
        print(f"Pass at 50: {grade_50(students_data[0][1])}")
        print(f"Pass at 80: {grade_80(students_data[0][1])}")

    elif option == 8:
        environment_report_data = environment_report()
        report_text = environment_report_data
        date_report_data = date_report()
        report_text = report_text + "\n" + date_report_data
        export_report(report_text)
        log_event("The report was exported")
        print(f'=== Enviroment And Date Report ===\n{report_text}')

    elif option == 9:
        print("Goodbye!!!")
        break

    else:
        print("Invalid option")  