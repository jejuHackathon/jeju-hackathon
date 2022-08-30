from django.db import models


class Oreum(models.Model):
    name = models.CharField(max_length=50)
    
    locations = [
        ('Susanbong', '수산봉'),
        ('Biyangbong', '비양봉'),
        ('Juge-oreum', '저지오름'),
        ('Saebyeol-Oreum', '새별오름'), 
        ('Eoseungsaengak', '어승생악'),
        ('Ansemio', '안세미오'),
        ('Geomun-Oreum', '거문오름'),
        ('Manjang', '만장굴'),
        ('Daranche-Oreum', '다랑쉬오름'),
        ('Someori-Oreum', '소머리오름'),
        ('Gunsan-Oreum', '군산오름'),
        ('Moseulbong', '모슬봉'),
    ]
    
    
    location = models.CharField(max_length=50, choices=locations)
    lat = models.FloatField(null =True)
    lng = models.FloatField(null=True)
    mainphoto = models.ImageField(blank=True, null=True)
    subphoto = models.ImageField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    phone = models.CharField(max_length=20)
    insta = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name