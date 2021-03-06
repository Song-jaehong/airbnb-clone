from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GEMDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GEMDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Koreana"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField("프로필사진", null=True, blank=True)
    gender = models.CharField(
        "성별", choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField("사용자정보", default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        "언어유형", choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    currency = models.CharField(
        "화폐유형", choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField("호스트권한", default=False)
