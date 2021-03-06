from django.db import models
from Account.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


# Create your models here.

class Job_info(models.Model):
    user = models.CharField(max_length=100, null=True)
    job_title = models.CharField(max_length=100,blank=True, null=True)
    school_name = models.CharField(max_length=30)
    class_size = models.PositiveIntegerField()
    start_date = models.CharField(max_length=100,null=True,blank=True)
    summary = models.TextField(null=True, blank=True)

    age_level = models.CharField(max_length=50)

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
    allowance = models.BooleanField(default=False)
    house_pic1 = models.FileField()
    pic1_thumbnail = ImageSpecField(
        source='house_pic1',  # 원본 ImageField 명
        processors=[Thumbnail(100, 100)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})  # 저장 옵션
    pic1_thumbnail2 = ImageSpecField(
        source='house_pic1',  # 원본 ImageField 명
        processors=[Thumbnail(250, 250)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})  # 저장 옵션
    house_pic2 = models.FileField(blank=True, null=True)
    pic2_thumbnail = ImageSpecField(
        source='house_pic2',  # 원본 ImageField 명
        processors=[Thumbnail(250, 250)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})  # 저장 옵션
    house_pic3 = models.FileField(blank=True, null=True)
    pic3_thumbnail = ImageSpecField(
        source='house_pic3',  # 원본 ImageField 명
        processors=[Thumbnail(250, 250)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})  # 저장 옵션
    house_pic4 = models.FileField(blank=True, null=True)
    pic4_thumbnail = ImageSpecField(
        source='house_pic4',  # 원본 ImageField 명
        processors=[Thumbnail(250, 250)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})  # 저장 옵션
    house_pic5 = models.FileField(blank=True, null=True)
    pic5_thumbnail = ImageSpecField(
        source='house_pic5',  # 원본 ImageField 명
        processors=[Thumbnail(250, 250)],  # 처리할 작업 목룍
        format='JPEG',  # 최종 저장 포맷
        options={'quality': 60})  # 저장 옵션
    severance_payment = models.BooleanField(default=False)
    health_insurance = models.BooleanField(default=False)
    national_pension = models.BooleanField(default=False)
    hits = models.IntegerField(null=True, blank=True, default=0)
    apply_count = models.IntegerField(null=True, blank=True, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    #like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
     #                                      blank=True,
      #                                     related_name='like_user_set',
       #                                    through='Like')  # post.like_set 으로 접근 가능

    def __unicode__(self):
        return self.school_name

    def publish(self):
        self.created_date = timezone.now()
        self.hits = 0
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

    graduate = models.BooleanField(default=False)
    estimate_graduate = models.DateField(blank=True, null=True)
    university = models.CharField(max_length=100)
    major = models.CharField(max_length = 100)
    start_date = models.CharField(max_length=40)

    prefer_class = models.CharField(max_length = 50)

    resume = models.FileField(blank=True, null=True)

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