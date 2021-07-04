from django.db import models


class BingoAdmin(models.Model):
    name = models.CharField(max_length=100)


class AdminNumber(models.Model):
    number = models.IntegerField()
    admin = models.ForeignKey(BingoAdmin, related_name="numbers", on_delete=models.CASCADE)


class Card(models.Model):
    user_name = models.CharField(max_length=100)
    is_bingo = models.BooleanField(default=False)
    admin = models.ForeignKey(BingoAdmin, related_name="cars", on_delete=models.CASCADE, null=True)
    p1 = models.IntegerField(null=True)
    p2 = models.IntegerField(null=True)
    p3 = models.IntegerField(null=True)
    p4 = models.IntegerField(null=True)
    p5 = models.IntegerField(null=True)
    p6 = models.IntegerField(null=True)
    p7 = models.IntegerField(null=True)
    p8 = models.IntegerField(null=True)
    p9 = models.IntegerField(null=True)
    p10 = models.IntegerField(null=True)
    p11 = models.IntegerField(null=True)
    p12 = models.IntegerField(null=True)
    p13 = models.IntegerField(null=True)
    p14 = models.IntegerField(null=True)
    p15 = models.IntegerField(null=True)
    p16 = models.IntegerField(null=True)
    p17 = models.IntegerField(null=True)
    p18 = models.IntegerField(null=True)
    p19 = models.IntegerField(null=True)
    p20 = models.IntegerField(null=True)
    p21 = models.IntegerField(null=True)
    p22 = models.IntegerField(null=True)
    p23 = models.IntegerField(null=True)
    p24 = models.IntegerField(null=True)
    p25 = models.IntegerField(null=True)


