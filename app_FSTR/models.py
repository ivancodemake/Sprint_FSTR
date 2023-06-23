from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    email = models.EmailField(unique=True)


class Mountain(models.Model):

    STATUS = [
        ('New', 'Новый'),
        ('Pending', 'В обработке'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Не принято'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    other_titles = models.CharField(max_length=300)
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE)
    levels = models.ForeignKey('Level', blank=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=8, choices=STATUS, default='New')


class Level(models.Model):
    winter = models.CharField(max_length=4, blank=True)
    summer = models.CharField(max_length=4, blank=True)
    autumn = models.CharField(max_length=4, blank=True)
    spring = models.CharField(max_length=4, blank=True)


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Images(models.Model):
    mountain = models.ForeignKey(Mountain, related_name='images', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
