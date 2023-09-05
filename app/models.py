from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=50)
    admission_no = models.CharField(max_length=50)
    dob = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
       return self.name + ""
    def __str__(self):
       return self.school + ""
    def __str__(self):
       return self.admission_no + ""
    def __str__(self):
       return self.dob + ""
    def __str__(self):
       return self.email + ""
    def __str__(self):
       return self.address + ""


class Season(models.Model):
    reg_date = models.CharField(max_length=25)
    departure = models.CharField(max_length=25)
    distination = models.CharField(max_length=25)
    route_no = models.CharField(max_length=10)
    month = models.CharField(max_length=15)
    

    def __str__(self):
       return self.issued_date + ""
    def __str__(self):
       return self.reg_date + ""
    def __str__(self):
       return self.departure + ""
    def __str__(self):
       return self.distination + ""
    def __str__(self):
       return self.route_no + ""
    def __str__(self):
       return self.month + ""

class Principal(models.Model):
    school = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    def __str__(self):
       return self.school + ""
    def __str__(self):
       return self.name + ""
    def __str__(self):
       return self.email + ""
   
