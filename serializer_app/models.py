from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=144)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=25)


    def __str__(self):
        return self.name


# __str__ = Obj => String Repr