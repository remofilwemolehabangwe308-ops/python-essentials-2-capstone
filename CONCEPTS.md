 1. The code in models.py is primarly created using concepts from PE2 Module 3. This code includes the Student and HonoursStudent classes and demonstrates how to use OOP constructors, class variables, method(get_grade) oveerriding and super() wich is used to assist the HonoursStudents in inheriting some of the trait from the Student class.
• data_tools.py makes use of concepts from PE2 Modules 2 and 4. It generates students data using random then after load a cleaned data, which I cleaned using string methods such as strip(), title(), and int().
• analytics.py makes use of concepts from PE2 Module 4. It uses generators for example passing_students(students), closure which is an inner function(grade(score)) that is able to remember its surrounding even after the outer function(make_grader(pass_mark)) is done and functions that calcutes the class statistics such as average, highest, lowest, and pass rate.
• reporting.py makes use of concepts from PE2 Modules 1 and 4. It makes use of standard library modules such as platform, datetime, calendar, and os to provide imformation about environment and dates.
• main.py brings all the modules together. It imports the classes and functions from the other files and provides the menu through which the user interacts with the program.

2. Splitting a program into multiple files helps keep everything more organized. It also makes the code easier to read and update when needed. Each file can handle one main task like generating reports, handling students classes, working with files, and performing calculations.This approach makes it easier for me to find and test specific parts of the program.If the program ws in one big file it would have been difficult to read and modify.

3. A class is a blueprint used to create objects. An object is a the actual instance created from the class.In this project I have two claases called Student class and HonoursStudent class.
• The difference between a normal function and a generator is that a normal function uses return to send results and stop the function while generators uses yield to pause the function and continues when the user uses next() to ask for the next data/number. A nexample of generator from this project is passing_students(students) and of a normal function is class_average(students)
• A closure is an inner functiion that is able to remember values from its outer function even after the outer function is done.An example of a closure could be grade(score).
• The difference between "w" and "a" modes is the "w" stands for write and is used when opening/writing a file or when replacing the existing content inside the file while "a" stands for append and is used to add new information at the end of the existing file.

4. Honestly speaking it was hard cause at first I thought it will be the same as what I have done on similar previous projects but I realised that this one requires more connections.I worked around this by splitting the project into smaller chunks. The first thing I did was think through what I wanted the program to do in plain English, without any coding, and then translate each step into Python. It was still challenging to put it all together, but breaking it down into smaller pieces made it easier for me to comprehend and build the final project. 
        


 