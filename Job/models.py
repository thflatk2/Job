from django.db import models
from Account.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings



# Create your models here.





class Job_info(models.Model):
    school_name = models.CharField(max_length=30)
    start_date = models.DateField(default=timezone.now())

    AGE_CHOICES  = (
        ('Kidergarten', 'Kindergarten'),
        ('Elementary', 'Elementary'),
        ('Middle','Middle'),
    )
    age_level = models.CharField(max_length=15, choices=AGE_CHOICES, default='A')

    location = models.CharField(max_length=20)
    contract_period = models.CharField(max_length=20)
    day_hour = models.CharField(max_length=50)
    min_salary = models.FloatField()
    max_salary = models.FloatField()

    FLIGHT_CHOICES = (
        ('none','none'),
        ('one-way','one-way'),
        ('round-trip','round-trip'),
    )
    flight_support = models.CharField(max_length=15, choices=FLIGHT_CHOICES, default='A')
    house = models.BooleanField()
    house_pic = models.FileField()
    severance_payment = models.BooleanField()
    health_insurance = models.BooleanField()
    national_pension = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like')  # post.like_set 으로 접근 가능

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def get_absolute_url(self):  # redirect시 활용
        return reverse('Job:detail', args=[self.id])

    @property
    def like_count(self):
        return self.like_user_set.count()


class Job_Apply(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job_info)
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


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Job_info)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'post')
        )