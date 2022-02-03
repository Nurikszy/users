from django.db import models
from django.contrib.auth.models import User

BISHKEK = 1
OSH = 2
TALAS = 3
Issyk_Kul = 4
NARYN = 5
JALAL_ABAD = 6
BATKEN = 7
region = (
    (BISHKEK, "BISHKEK"),
    (OSH, "OSH"),
    (TALAS, "TALAS"),
    (Issyk_Kul, "ISSYK KUL"),
    (NARYN, "NARYN"),
    (JALAL_ABAD, "JALAL ABAD"),
    (BATKEN, "BATKEN"),
)


ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = ((ADMIN, "ADMIN"), (VIPClient, "VIP-Client"), (CLIENT, "CLIENT"))
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = ((MALE, "MALE"), (FEMALE, "FEMALE"), (OTHER, "OTHER"))


class CustomUser(User):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    user_type = models.IntegerField(
        choices=USER_TYPE, verbose_name="Тип Пользователя", default=CLIENT
    )
    phone_number = models.CharField("phone_number", max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Гендер")
    region = models.IntegerField(choices=region, verbose_name="Регион", null=True)
