from django.db import models
from Account.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings



# Create your models here.

class Job_info(models.Model):
    user = models.CharField(max_length=100, null=True)
    school_name = models.CharField(max_length=30)
    start_date = models.DateField(null=True,blank=True)
    summary = models.TextField(null=True, blank=True)

    AGE_CHOICES  = (
        ('Kindergarten', 'Kindergarten'),
        ('Elementary', 'Elementary'),
        ('Middle','Middle'),
    )
    age_level = models.CharField(max_length=15, choices=AGE_CHOICES, default='A')

    location = models.CharField(max_length=30)
    contract_period = models.CharField(max_length=20)
    day_hour = models.CharField(max_length=100)
    min_salary = models.FloatField()
    max_salary = models.FloatField()

    FLIGHT_CHOICES = (
        ('None','None'),
        ('One-way','One-way'),
        ('Round-trip','Round-trip'),
    )
    flight_support = models.CharField(max_length=15, choices=FLIGHT_CHOICES, default='A' )
    house = models.BooleanField(default=False)
    house_pic1 = models.FileField()
    house_pic2 = models.FileField(blank=True, null=True)
    house_pic3 = models.FileField(blank=True, null=True)
    house_pic4 = models.FileField(blank=True, null=True)
    house_pic5 = models.FileField(blank=True, null=True)
    severance_payment = models.BooleanField(default=False)
    health_insurance = models.BooleanField(default=False)
    national_pension = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    qualification = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    #like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
     #                                      blank=True,
      #                                     related_name='like_user_set',
       #                                    through='Like')  # post.like_set 으로 접근 가능

    def __unicode__(self):
        return self.school_name

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def get_absolute_url(self):  # redirect시 활용
        return reverse('Job:detail', args=[self.id])

   # @property
    #def like_count(self):
     #   return self.like_user_set.count()


class Job_Apply(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job_info)
    profile_image1 = models.ImageField(blank=True, null=True)
    profile_image2 = models.ImageField(blank=True, null=True)
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length = 35)
    skyid = models.CharField(max_length= 35)

    TOOL_CHOICES = (
        ('USA', 'USA'),
        ('Canada', 'Canada'),
        ('UK', 'UK'),
        ('Ireland', 'Ireland'),
        ('South Africa', 'South Africa'),
        ('New Zealand', 'New Zealand'),
        ('Australia', 'Australia'),
    )

    country = models.CharField(max_length = 20, choices=TOOL_CHOICES)

    GEN_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GEN_CHOICES)
    cur_residence = models.CharField(max_length=30)
    birth = models.CharField(max_length = 30)
    degree = models.CharField(max_length = 100)
    start_date = models.CharField(max_length=40)

    prefer_class = models.CharField(max_length = 50)

    resume = models.FileField(blank=True, null=True)
    letter = models.FileField(blank=True, null=True)

    introduction = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()
'''
    address = models.CharField(max_length = 30)
    medical = models.BooleanField()
    family = models.IntegerField()


    education = models.CharField(max_length = 15, default='A')

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
    photo = models.FileField()

    OFFI_CHOICES = (
        ('aaa', 'Business Scope'),
        ('history', 'History'),
        ('change in capital', 'Change in Capital'),
        ('share with voting right', 'Share with Voting Right'),
        ('dividend', 'Dividend'),
    )
    office = models.CharField(max_length = 15, choices=OFFI_CHOICES, default='A')

    wanted_salary = models.IntegerField()
    prefer_location = models.CharField(max_length = 15)
    second_location = models.CharField(max_length = 15)


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
'''


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Job_info)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'post')
        )