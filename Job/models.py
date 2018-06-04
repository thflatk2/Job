from django.db import models
from Account.models import User
from django.utils import timezone

# Create your models here.

class Job_Apply(models.Model):
	user = models.ForeignKey(User)
	email = models.CharField(max_length = 25)
	country = models.CharField(max_length = 20)
	birth = models.CharField(max_length = 20)
	gender = models.BooleanField()
	address = models.CharField(max_length = 30)
	medical = models.BooleanField()
	family = models.IntegerField()

	TOOL_CHOICES = (
		('BA', 'BA'),
		('history', 'History'),
		('change in capital', 'Change in Capital'),
		('share with voting right', 'Share with Voting Right'),
		('dividend', 'Dividend'),
	)

	education = models.CharField(max_length = 15, choices=TOOL_CHOICES, default='A')
	degree = models.CharField(max_length = 20)
	
	QUAL_CHOICES = (
		('aaa', 'Business Scope'),
		('history', 'History'),
		('change in capital', 'Change in Capital'),
		('share with voting right', 'Share with Voting Right'),
		('dividend', 'Dividend'),
	)

	qualification = models.CharField(max_length = 15, choices=QUAL_CHOICES, default='A')
	qual_time = models.CharField(max_length = 10)

	resume = models.FileField()
	letter = models.FileField()
	photo = models.FileField()
	
	OFFI_CHOICES = (
		('aaa', 'Business Scope'),
		('history', 'History'),
		('change in capital', 'Change in Capital'),
		('share with voting right', 'Share with Voting Right'),
		('dividend', 'Dividend'),
	)
	office = models.CharField(max_length = 15, choices=OFFI_CHOICES, default='A')

	start_date = models.DateTimeField(default=timezone.now)
	wanted_salary = models.IntegerField()
	prefer_location = models.CharField(max_length = 15)
	second_location = models.CharField(max_length = 15)
	
	CLAS_CHOICES = (
		('aaa', 'Business Scope'),
		('history', 'History'),
		('change in capital', 'Change in Capital'),
		('share with voting right', 'Share with Voting Right'),
		('dividend', 'Dividend'),
	)
	prefer_class = models.CharField(max_length = 15, choices=CLAS_CHOICES, default='A')

	freind = models.BooleanField()
	freind_name = models.CharField(max_length=15)


	INFL_CHOICES = (
		('aaa', 'Business Scope'),
		('history', 'History'),
		('change in capital', 'Change in Capital'),
		('share with voting right', 'Share with Voting Right'),
		('dividend', 'Dividend'),
	)
	influx = models.CharField(max_length=10, choices=INFL_CHOICES, default='A')
	
	contact = models.CharField(max_length=20)
	good_time = models.DateTimeField(default=timezone.now)

	certification = models.BooleanField()
	certification_text = models.CharField(max_length = 20)

	criminal = models.BooleanField()
	criminal_text = models.CharField(max_length = 20)

	pet = models.BooleanField()
	visa = models.CharField(max_length = 10)
	housing = models.BooleanField()

	KORE_CHOICES = (
		('aaa', 'Business Scope'),
		('history', 'History'),
		('change in capital', 'Change in Capital'),
		('share with voting right', 'Share with Voting Right'),
		('dividend', 'Dividend'),
	)
	korean_level = models.CharField(max_length=15, choices=KORE_CHOICES, default='A')


	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.created_date = timezone.now()
		self.save()


	def publish(self):
		self.created_date = timezone.now()
		self.save()


	