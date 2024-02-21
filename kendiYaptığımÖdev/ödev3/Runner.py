from Student import Student
from Teacher import Teacher

#listeleree ekleme yapabilmek için methodlar
def add_student(student_list, student):
    student_list.append(student)

def add_teacher(teacher_list, teacher):
    teacher_list.append(teacher)

#eklenen  öğrencileri listeye depoladım
student_list = []
student1=Student("Meryem","Ozgun",10,"Basarili",90,95)
student2=Student("Gökhan","Ozgun",11,"Iyi",80,60)
student3=Student("Hacer","Eslem",12,"Orta",40,70)

add_student(student_list,student1)
add_student(student_list,student2)
add_student(student_list,student3)

#eklenen  öğretmenleri listeye depoladım
teacher_list = []
tchr1=Teacher("Kadir","Güler","SQL",100,"Sali,Carsamba")
tchr2=Teacher("Zeynep","Yilmaz","SELENİUM",101,"Pazartesi,Persembe")
tchr3=Teacher("Gül","Diken","API",102,"Cuma")


add_teacher(teacher_list, tchr1)
add_teacher(teacher_list, tchr2)
add_teacher(teacher_list, tchr3)

#olusturulan öğretmen ve öğrencileri console da görelim
def showInfoStudent(student_list):
    for student in student_list:
        student.showInfo()

def showInfoTeacher(teacher_list):
    for teacher in teacher_list:
        teacher.showInfo()

print("      OGRENCİLER    ")
showInfoStudent(student_list)
print("      OGRETMENLER   ")
showInfoTeacher(teacher_list)