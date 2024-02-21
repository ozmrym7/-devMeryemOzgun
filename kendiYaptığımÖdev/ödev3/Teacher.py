class Teacher:
  def __init__(self,name ,surname,branch, teacher_no,working_day):
    self.name=name
    self.surname=surname
    self.branch=branch
    self.teacher_no=teacher_no
    self.working_day=working_day

  def showInfo(self):
    print(f"Ad:{self.name} Soyad:{self.surname} Brans: {self.branch} öğrentmenNumarasi:{self.teacher_no} CalismaGünleri{self.working_day}")

  def inTheSchool(self):
    print(f"{self.name} öğretmen, {self.working_day} günü okulda bulunuyor.")

   
#experiment
    
# tchr1=Teacher("Kadir","Güler","Matematik",100,"Sali,Carsamba")
# tchr1.showInfoTeacher()
# tchr1.inTheSchool()



    

