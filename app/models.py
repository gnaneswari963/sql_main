from django.db import models

# Create your models here.

class Dept(models.Model):
    dname=models.CharField(max_length=100,primary_key=True)
    loc=models.CharField(max_length=100)
    deptno=models.PositiveIntegerField()

    def __str__(self):
        return self.dname

class Emp(models.Model):
    ename=models.CharField(max_length=100,primary_key=True)
    eid=models.PositiveIntegerField()
    sal=models.PositiveIntegerField()
    deptno=models.OneToOneField(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
    
class Salgrade(models.Model):
    grade=models.PositiveIntegerField()
    lowsal=models.PositiveIntegerField()
    highsal=models.PositiveIntegerField()

   

    
    
class Bonus(models.Model):
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.PositiveIntegerField()
    comm=models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.comm
    

    

    