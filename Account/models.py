import os
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from hashlib import sha1, md5


class UserManager(BaseUserManager):
    def create_user(self, email, name, country, birth, gender, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            country= country,
            birth= birth,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, country, birth, gender, password):
        """
        주어진 이메일, 폰넘버,네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            country = country,
            birth=birth,
            gender=gender,
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
    country = models.CharField(
        verbose_name=_('Country'),
        max_length=18,
        #unique=True
    )
    birth = models.DateField(
	verbose_name=_('Birthday'),
    )
    gender = models.BooleanField(
	verbose_name=_('Gender'),
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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','country', 'birth', 'gender']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def set_password(self, raw_password):
        # Opencart의 salt 값은 9자리의 alphanumeric 문자열
        salt = md5(os.urandom(128)).hexdigest()[:9]

        # Opencart PHP 프로그램의 비밀번호 암호화 알고리즘
        hashed = sha1(
            (salt + sha1(
                (salt + sha1(
                    raw_password.encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()).encode('utf8')
        ).hexdigest()

        self.salt = salt
        self.password = hashed

    def check_password(self, raw_password):
        try:
            user = User.objects.get(email=self.email)

            hashed = sha1(
                (user.salt + sha1(
                    (user.salt + sha1(
                        raw_password.encode('utf8')
                    ).hexdigest()).encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()

            if user.password == hashed:
                return True
            else:
                return False

        except User.DoesNotExist:
            return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    get_full_name.short_description = _('Full name')
