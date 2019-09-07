from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    username = models.CharField(verbose_name="User Name", max_length=50)
    password = models.CharField(verbose_name="Password", max_length=50)
    email = models.EmailField("verbose_name=Email Address", max_length=254)
    creation_date = models.DateTimeField(
        verbose_name="Creation Date", default=timezone.now)
    modification_date = models.DateTimeField(
        verbose_name="Modification Date", default=timezone.now)
    person = models.ForeignKey(
        "login.Person", verbose_name="Person", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Person(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=50)
    last_name = models.CharField(verbose_name="Last Name", max_length=50)
    creation_date = models.DateTimeField(
        verbose_name="Creation Date", default=timezone.now)
    modification_date = models.DateTimeField(
        verbose_name="Modification Date", default=timezone.now)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})
