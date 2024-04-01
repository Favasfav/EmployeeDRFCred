from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Address(models.Model):
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)    
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    address = models.TextField()
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)

    
class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100)
    percentage = models.FloatField()
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='project_photos/',blank=True,null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)


