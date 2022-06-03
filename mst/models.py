from django.db import models

class Group(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField('グループ名', max_length=30)

    def __str__(self):
        return self.code

class Member(models.Model):

    full_name = models.CharField('名前', max_length=150)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    auth = models.BooleanField(
        '権限A',
        default=False,
    )