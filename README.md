# Student Analytics Toolkit
## Description
I'm developing Student Analytics Toolkit, which consumes raw student data, performs data cleaning and conversion to Student objects, analysing the resulting objects using statistical calculations, generators and closures, and providing environment, date and export reports through a terminal menu.
**Author:** Remofilwe Molehabangwe 
**Cohort:** Data Science Practitioner, Jan 2026 - Melsoft Academy
## Features
1. Generate sample data file
2. Load & clean records from file
3. View all students
4. Analyse (averages, pass/fail, top student)
5. Filter students (generator)
6. Grade with a custom pass mark (closure)
7. Environment & date report
8. Export results to a file
9. Exit
## How to run
1. Clone the repository.
2. Open the project folder in the terminal.
3. Install the requirements if needed:
   pip install -r requirements.txt
4. Run the program:
   python main.py
## Project Structure
1. models.py - Contains the Student and HonoursStudent classes and demonstrates object-oriented programming and inheritance.
2. data_tools.py - Handles generating, loading, cleaning, exporting, and logging student data.
3. analytics.py - Contains the generator, closures, and statistical functions such as average, highest, lowest, and pass rate.
4. reporting.py - Produces environment and date reports.
5. main.py - Provides the menu and connects all the modules together.
## Concepts demonstrated
This project demonstrates file handling, string cleaning, object-oriented programming, inheritance, generators, closures, exception handling and use of Python Standard Library modules.
## Sample output
===== STUDENT ANALYTICS TOOLKIT =====
1.Generate student data
2.Display all student
3.Display passing students
4.Show class average
5.Show highest score
6.Show lowest score
7.Show pass rate
8.Show reports
9.Exit

Highest score: Lerato | Score: 93
Lowest score: Peter | Score: 15
Pass rate: 87.5

OS name: Windows
Python version: 3.14.5
File exists: True
Current month: September

