from django.db import models

# Create your models here.
class Record_cust(models.Model):
	
	created_at = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=20)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	city =  models.CharField(max_length=50)
	
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	
class Record_host(models.Model):
	
	created_at = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=20)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	city =  models.CharField(max_length=50)
	organisation = models.CharField(max_length=50)
	university =  models.CharField(max_length=50)

	
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	
class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    venue = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date = models.DateField()
    timing = models.TimeField()
    capacity = models.PositiveIntegerField()  # Renamed from attendees to capacity
    organisation = models.CharField(max_length=100)
    host = models.ForeignKey(Record_host, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
	


class TicketInformation(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
	location = models.CharField(max_length=50)
	contact = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	lastdate = models.IntegerField()

	def __str__(self):
		return f"{self.event}"
	



