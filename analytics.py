def passing_students(students):
    for name, score in students:
        if score >= 50:
            yield name, score

def make_grader(pass_mark):
    def grade(score):
        if score >= pass_mark:
            return True
        else:
            return False
    return grade 
grade_50 = make_grader(50)
grade_80 = make_grader(80)

def class_average(students):
    if len(students) == 0:
        return "No scores available"
    sum_scores = 0
    scores_count = 0 
    for name, score in students:
        sum_scores += score 
        scores_count += 1
    return sum_scores / scores_count

def highest(students):
    if len(students) == 0:
        return "No student available"
    student_iterator = iter(students)
    first_student = next(student_iterator)
    name, score = first_student
    highest_score = score
    highest_student = first_student
    for name, score in student_iterator:
        if score > highest_score:
            highest_score = score
            highest_student = (name, score)
    return highest_student

def lowest(students):
    if len(students) == 0:
        return "No students"
    student_iterator = iter(students)
    first_student = next(student_iterator)
    name, score = first_student
    lowest_score = score
    lowest_student = first_student
    for name, score in student_iterator:
        if score < lowest_score:
            lowest_score = score
            lowest_student = (name, score)
    return lowest_student         

def pass_rate(students):
    if len(students) == 0:
        return "No students available"
    total_students = 0
    passed_students = 0
    for name, score in students:
        total_students += 1
        if score >= 50:
            passed_students += 1
    return passed_students / total_students * 100 
        



    


