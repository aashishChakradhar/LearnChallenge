from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
from datetime import date

# Create your models here.

class BaseModel(models.Model):
    uid = models.AutoField(primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add = True)
    modified = models.DateField(auto_now= True)
    class Meta:
        abstract = True

class NepaliYear(BaseModel):
    year = models.DecimalField(decimal_places=0, default=2080,max_digits =4,validators=[MinValueValidator(2080),MaxValueValidator(3000)])
    current = models.BooleanField(default=True)    

class NepaliMonth(BaseModel):    
    month = models.CharField(max_length=20,default=" Unknown")
    def __str__(self):
        return self.month

class Room(BaseModel):
    roomName = models.CharField(max_length=20,default="none")
    floor = models.DecimalField(max_digits=1,decimal_places=0,default=0)
    occupied = models.BooleanField(default=False)
    rent = models.DecimalField(max_digits=6,decimal_places=2,validators=[MinValueValidator(0.00),MaxValueValidator(10000.00)],default=00.00)
    def __str__(self):
        return self.roomName

class Person(BaseModel):
    roomId = models.ForeignKey(Room,on_delete = models.CASCADE,default = 0)
    personName = models.CharField(max_length=50, default='unknown')
    phone = models.CharField(max_length=10,validators=[RegexValidator(r'^9[0-9]{9}$')])
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.personName

class RentHistory(BaseModel):
    roomId = models.ForeignKey(Room,on_delete = models.CASCADE,default = 0)
    personId = models.ForeignKey(Person,on_delete = models.CASCADE,default = 0)
    totalRequired = models.DecimalField(max_digits=8,decimal_places=2,validators=[MinValueValidator(0.00),MaxValueValidator(999999.99)])
    totalRemaining = models.DecimalField(max_digits=8,decimal_places=2,validators=[MinValueValidator(0.00),MaxValueValidator(999999.99)])
    def __str__(self):
        return self.remaining

class RentPayment(BaseModel):
    roomId = models.ForeignKey(Room,on_delete = models.CASCADE,default = 0)
    personId = models.ForeignKey(Person,on_delete = models.CASCADE,default = 0)
    RentHistoryId = models.ForeignKey(RentHistory,on_delete = models.CASCADE,default = 0)
    dateId = models.ForeignKey(NepaliYear,on_delete = models.CASCADE,default = 0)
    dateId = models.ForeignKey(NepaliMonth,on_delete = models.CASCADE,default = 0)
    paid = models.DecimalField(max_digits=6,decimal_places=2,validators=[MinValueValidator(0.00),MaxValueValidator(9999.99)])
    comment = models.CharField(max_length=100,default="No Comments")
    def __str__(self):
        return self.rentMonth

