#School class
class School:
  max_population = 100
  grade_levels = ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6"]
  def __init__(self, name, student_gender, population, is_boarding, is_bilingual, is_intl = True):
    self.name = name
    self.student_gender = student_gender
    self.population = population
    self.is_bilingual = is_bilingual
    self.is_boarding = is_boarding
    self.is_intl = is_intl
    self.additional_students_enrolled = {}
    self.expelled_students = {}
    self.children_gender = []
    self.graduate_students = {}
  
#simple function to output gender type enrolled
  def gender_enrolled(self):
    if self.student_gender == "only boys":
      self.children_gender.append("Male")
    elif self.student_gender == "only girls":
      self.children_gender.append("Female")
    else:
      self.children_gender.append("Male")
      self.children_gender.append("Female")
    return self.children_gender

#School methods - enrolls, expels and promotes students.
  def enroll(self, student):
    if self.population < School.max_population and student.gender in self.gender_enrolled():
      self.additional_students_enrolled[student.name] = student.age, student.grade
      self.population += 1
      return "Congratulations! {student_name} has been enrolled at {school_name}!".format(student_name=student.name, school_name = self.name)
    else:
      return "Sorry, {student_name} cannot be enrolled at {school_name}!".format(student_name=student.name, school_name=self.name)

  def promote(self, student):
    grade_index = School.grade_levels.index(student.grade)
    next_grade_index = grade_index + 1
    if student.name in self.additional_students_enrolled and next_grade_index < len(School.grade_levels):
      next_grade=School.grade_levels[next_grade_index]
  #create attribute called self.grade in student class
      student.grade = next_grade
      return "You have now been promoted to {next_grade}. Well done, {student_name}!".format(next_grade=student.grade, student_name=student.name)
    elif student.name not in self.additional_students_enrolled:
      return "Sorry, {student_name} is not enrolled at {school_name}, and so cannot be promoted.".format(student_name = student.name, school_name = self.name)
    else:
      student.grade = "graduate"
      self.graduate_students[student.name] = student.age, student.grade
      return "You have successfully graduated from {school_name}. Well done, {student_name}!".format(school_name=self.name, student_name=student.name)

  def expel(self, student):
#reate attribute called self.score in student class
    if student.name not in self.additional_students_enrolled:
      return "{student_name} is not enrolled at {school_name}.".format(student_name = student.name, school_name=self.name)
    else:
      if student.score < 40 and student.is_naughty == False:
        self.additional_students_enrolled.pop(student.name)
        self.expelled_students[student.name] = student.age, student.grade, "for poor grades"
        self.population -= 1
        return "{student_name} has been expelled from {school_name} due to poor grades.".format(student_name = student.name, school_name=self.name)
      elif student.score >= 40 and student.is_naughty == True:
        self.additional_students_enrolled.pop(student.name)
        self.population -= 1
        self.expelled_students[student.name] = student.age, student.grade, "for being naughty"
        return "{student_name} has been expelled from {school_name} for being so naughty.".format(student_name = student.name, school_name=self.name)
      else:
        self.additional_students_enrolled.pop(student.name)
        self.population -= 1
        self.expelled_students[student.name] = student.age, student.grade, "for being naughty and having bad grades"
        return "{student_name} has been expelled from {school_name} for being so naughty and having poor grades.".format(student_name = student.name, school_name=self.name)

  def __repr__(self):
    description = "Welcome to {name}, the citadel of Knowledge. ".format(name=self.name)
#gender added
    if self.gender_enrolled() == "Female only":
      gender_description = "We are admit girls only "
      description += gender_description
    elif self.gender_enrolled() == "Male only":
      gender_description = "We are admit boys only "
      description += gender_description
    else:
      gender_description = "We are admit both girls and boys "
      description += gender_description
#boarding added    
    if self.is_boarding:
      boarding_description = "and we are fully boarding. "
      description += boarding_description
    else:
      boarding_description = "and we are non-boarding. "
      description += boarding_description
 #bilingual added   
    if self.is_bilingual:
      lang_description = "And yes, we teach French and English languages at our school. "
      description += lang_description
 #international added   
    if self.is_intl:
      global_description = "Did I forget to add that we are also globally recognized? "
      description += global_description
 #compelling suffix added 
    suffix = "What more? Enroll your child with {name} now!".format(name=self.name)
    description += suffix
    return description

#student class - can write exams, can be naughty, and can register for exams.

class Student:

  def __init__(self, name, age, gender, grade):
    self.score = 0
    self.is_naughty = False
    self.name = name
    self.age = age
    self.gender = gender
    self.grade = grade
    self.subjects = []
  
  def write_exams(self):
    score = input("What score did you have in your final exams? Score should be a number between 0 - 100: ")
    if len(score) == 2 and "%" in score:
      score = int(score[:1])
    elif len(score) == 3 and "%" in score:
      score = int(score[:2])
    elif len(score) == 4 and "%" in score:
      score = int(score[:3])
    else:
      score = int(score)
    self.score = self.score + score
    return self.score
  
  def be_naughty(self):
    self.is_naughty = True
    return self.is_naughty
  
  def register_subjects(self, subjects):
    for subject in range(0, len(subjects)):
      self.subjects.append(subjects[subject])
    description = "{student_name}, you have successfully registered for the following subjects: ".format(student_name = self.name)
    for subject in subjects:
      description += subject + ", "
    return description

  def __repr__(self):
    return "My name is {name}, I am {age} years old, a {gender} child, and I am in {grade}.".format(name=self.name, age=self.age, gender=self.gender.lower(), grade=self.grade)


# Three school objects instantiated
grange = School('Grange International Schools', 'mixed', 85, False, True)
baptist_boys = School('Baptist Boys Grammar School', 'only boys', 80, True, False, False)
queens_college = School("Queens Girls College", 'only girls', 92, True, True, False)

# print(grange)
# print()
# print(baptist_boys)
# print()
# print(queens_college)

sarah_jones = Student("Sarah Jones", 6, "Female", "Grade 2")
arian_luke = Student("Arian Luke", 9, "Male", "Grade 1")
mary_brian = Student("Mary Brian", 10, "Female", "Grade 4")
henry_paul = Student("Henry Paul", 12, "Male", "Grade 6")

print(sarah_jones)
print(arian_luke)
print(mary_brian)
print(henry_paul)
print()
print(grange.enroll(henry_paul))
print(baptist_boys.enroll(arian_luke))
print(queens_college.enroll(mary_brian))
print(grange.enroll(sarah_jones))
print()
print(grange.additional_students_enrolled)
print(baptist_boys.additional_students_enrolled)
print(queens_college.additional_students_enrolled)
print()
print(grange.promote(henry_paul))
print(grange.promote(sarah_jones))
print(baptist_boys.promote(mary_brian))
print(baptist_boys.promote(arian_luke))
print(queens_college.promote(mary_brian))
print()
print(henry_paul.grade)
print(grange.graduate_students)
print(queens_college.expel(sarah_jones))
print(queens_college.additional_students_enrolled)
print(queens_college.expel(mary_brian))
print(queens_college.additional_students_enrolled)
print(queens_college.expelled_students)
print()
print(mary_brian.score)
print(mary_brian.write_exams())
print(grange.enroll(mary_brian))
print(arian_luke.write_exams())
print(sarah_jones.write_exams())
print()
print(sarah_jones.is_naughty)
print(sarah_jones.be_naughty())
print(grange.additional_students_enrolled)
print(grange.expel(sarah_jones))
print(grange.additional_students_enrolled)
print(grange.expelled_students)
print()
print(arian_luke.register_subjects(["Maths", "English", "Music", "French", "Fine Arts"]))
print(arian_luke.subjects)