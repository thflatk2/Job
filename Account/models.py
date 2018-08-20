import os
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from hashlib import sha1, md5
from django.template.defaultfilters import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, name, phone, type,password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            type=type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, type, password):
        """
        주어진 이메일, 폰넘버,네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            phone=phone,
            type=type,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('Email address2'),
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=30,
        unique=True,
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=18,
        unique=True,
        default=0
        #unique=True
    )
    type = models.CharField(
        verbose_name=_('Type'),
        max_length=18,
        #unique=True
    )

    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now,
    )
    salt = models.CharField(
        verbose_name=_('Salt'),
        max_length=10,
        blank=True
    )
    slug = models.SlugField(blank=True)

    user_pic1 = models.ImageField(null=True, blank=True)
    user_pic2 = models.ImageField(null=True, blank=True)

    last_name = models.CharField(max_length=25, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)

    TOOL_CHOICES = (
        ('USA', 'USA'),
        ('Canada', 'Canada'),
        ('UK', 'UK'),
        ('Ireland', 'Ireland'),
        ('South Africa', 'South Africa'),
        ('New Zealand', 'New Zealand'),
        ('Australia', 'Australia'),
    )

    country = models.CharField(max_length=20, choices=TOOL_CHOICES, null=True, blank=True)

    GEN_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GEN_CHOICES, null=True, blank=True)
    cur_residence = models.CharField(max_length=50, null=True, blank=True)
    birth = models.CharField(max_length=30, null=True, blank=True)
    graduate = models.NullBooleanField(default=False,null=True,blank=True)
    estimate_graduate = models.DateField(null=True,blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.CharField(max_length=50, null=True, blank=True)

    CLAS_CHOICES = (
        ('Kindergarten', 'Kindergarten'),
        ('Elementary', 'Elementary'),
        ('Middle', 'Middle'),
    )
    prefer_class = models.CharField(max_length=15, choices=CLAS_CHOICES, default='A')

    resume = models.FileField(null=True, blank=True)

    agency_name = models.CharField(max_length=30, null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    job_count = models.IntegerField(null=True, blank=True, default=0)
    activate = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','type']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    get_full_name.short_description = _('Full name')
