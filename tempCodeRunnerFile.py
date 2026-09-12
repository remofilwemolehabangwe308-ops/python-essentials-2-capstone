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

print(grade_50(45))
print(grade_50(51))
print(grade_50(78))
print(grade_50(93))

print(grade_80(45))
print(grade_80(51))
print(grade_80(78))
print(grade_80(93))