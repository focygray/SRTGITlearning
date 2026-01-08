class StudentManager:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.score = 0.0
        self.course_unit = None
        self.cgpa = 0.0

    def compute_CGPA(self, unit, score):
        self.cgpa = score / unit
    
    def get_cgpa(self):
        return self.cgpa