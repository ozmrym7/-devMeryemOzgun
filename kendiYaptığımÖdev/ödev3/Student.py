"""


---Bir okul kayıt sistemi kodlayalım---

Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.

Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım.
 Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım.
"""

class Student:
  def __init__(self,name ,surname,number, description ,vize,final):
    self.name=name
    self.surname=surname
    self.number=number
    self.description=description
    self.average=self.average(vize,final)

  def average (self,vize,final):
      return (vize*0.4)+(final*0.6)

  def showInfo(self):
    print(f"Ad:{self.name} Soyad:{self.surname} Numara: {self.number} Acıklama:{self.description} Ortalama:{self.average}")



#experiment

# student1=Student("Meryem","Ozgun",10,"Basarili",90,95)
# student2=Student("Gökhan","Ozgun",11,"Iyi",80,60)
# student3=Student("Hacer","Eslem",12,"Orta",40,70)



# student1.showInfoStudent()
# student2.showInfoStudent()
# student3.showInfoStudent()