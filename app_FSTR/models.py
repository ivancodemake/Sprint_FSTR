from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, blank=True)
    second_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=50, blank=True)


class Mountain(models.Model):

    STATUS = [
        ('New', 'Новый'),
        ('Pending', 'В обработке'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Не принято'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    other_titles = models.CharField(max_length=300, blank=True)
    beauty_title = models.CharField(max_length=300, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE)
    connect = models.CharField(max_length=300, blank=True)
    levels = models.ForeignKey('Level', on_delete=models.PROTECT)
    status = models.CharField(max_length=8, choices=STATUS, default='New')


class Level(models.Model):
    winter = models.CharField(max_length=4, blank=True)
    summer = models.CharField(max_length=4, blank=True)
    autumn = models.CharField(max_length=4, blank=True)
    spring = models.CharField(max_length=4, blank=True)


class Coordinates(models.Model):
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    height = models.IntegerField(blank=True)


class Images(models.Model):
    mountain = models.ForeignKey(Mountain, related_name='images', null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(blank=True, max_length=30)
    image = models.ImageField(upload_to='images/', null=True, blank=True)





