from django.db import models


class BingoAdmin(models.Model):
    name = models.CharField(max_length=100)


class AdminNumber(models.Model):
    number = models.IntegerField()
    admin = models.ForeignKey(BingoAdmin, related_name="numbers", on_delete=models.CASCADE)


class Card(models.Model):
    user_name = models.CharField(max_length=100)
    is_bingo = models.BooleanField(default=False)
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    p3 = models.IntegerField()
    p4 = models.IntegerField()
    p5 = models.IntegerField()
    p6 = models.IntegerField()
    p7 = models.IntegerField()
    p8 = models.IntegerField()
    p9 = models.IntegerField()
    p10 = models.IntegerField()
    p11 = models.IntegerField()
    p12 = models.IntegerField()
    p13 = models.IntegerField()
    p14 = models.IntegerField()
    p15 = models.IntegerField()
    p16 = models.IntegerField()
    p17 = models.IntegerField()
    p18 = models.IntegerField()
    p19 = models.IntegerField()
    p20 = models.IntegerField()
    p21 = models.IntegerField()
    p22 = models.IntegerField()
    p23 = models.IntegerField()
    p24 = models.IntegerField()
    p25 = models.IntegerField()


