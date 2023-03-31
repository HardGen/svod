from django.db import models


# Create your models here.
class Otd(models.Model):
    idlpu = models.IntegerField()
    lpu = models.CharField(max_length=255)
    idotd = models.IntegerField(primary_key=True)
    otd_name = models.CharField(max_length=255)
    short_otd = models.CharField(max_length=255)
    activ = models.SmallIntegerField()
    zav_otd = models.CharField(max_length=100, null=True, blank=True)
    msister = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.otd_name


class Food_svod(models.Model):
    dt_svood = models.DateTimeField(auto_now_add=True)
    priznak = models.IntegerField(default=0)
    idotd = models.ForeignKey('Otd', on_delete=models.RESTRICT)
    vsego = models.IntegerField(default=0)
    child = models.SmallIntegerField(default=0)
    mam = models.SmallIntegerField(default=0)
    mam_nofood = models.SmallIntegerField(default=0)
    wow = models.SmallIntegerField(default=0)
    zond = models.SmallIntegerField(default=0)
    golod = models.SmallIntegerField(default=0)
    diet_01_kis = models.SmallIntegerField(default=0)
    diet_01_bul = models.SmallIntegerField(default=0)
    diet_02 = models.SmallIntegerField(default=0)
    diet_03 = models.SmallIntegerField(default=0)
    diet_ovd = models.SmallIntegerField(default=0)
    diet_shd = models.SmallIntegerField(default=0)
    diet_child = models.SmallIntegerField(default=0)
    diet_age_1_3 = models.SmallIntegerField(null=True, blank=True, default=0)
    diet_age_3_7 = models.SmallIntegerField(null=True, blank=True, default=0)
    diet_age_7_11 = models.SmallIntegerField(null=True, blank=True, default=0)
    diet_age_11_18 = models.SmallIntegerField(null=True, blank=True, default=0)
    dop = models.SmallIntegerField(null=True, blank=True, default=0)
    diet_vdb = models.SmallIntegerField(default=0)
    diet_nbd = models.SmallIntegerField(default=0)
    diet_nkd = models.SmallIntegerField(default=0)
    fio_ms = models.CharField(max_length=255, null=True, blank=True)
    dt_create = models.DateTimeField(auto_now=True)