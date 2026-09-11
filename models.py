class Student:
    school_name = "Melsoft Academy"
    total_students = 0


    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score
        Student.total_students += 1

    def get_grade(self):
        if self.score < 50:
            return "Fail"
        elif self.score < 80:
            return "Pass"
        else:
            return "Distinction" 

    def has_passed(self):
        if self.score >= 50:
            return True
        else:
            return False

    def __str__(self):
        return (f" Name: {self.name} | Student ID: {self.student_id} | Score: {self.score} | Grade: {self.get_grade()}")
    
class HonoursStudent(Student):
    def __init__(self, name, student_id, score, research_topic):
        super().__init__(name, student_id, score)
        self.research_topic = research_topic

    def get_grade(self):
        if self.score >= 75:
            return "Distinction (Honours)"
        else:
            return super().get_grade()

    def __str__(self):
        return(f"{super().__str__()} | Research Topic: {self.research_topic}")

          

    