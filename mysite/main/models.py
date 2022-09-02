from django.db import models

class Oreum(models.Model):
    name = models.CharField(max_length=50)
    
    locations = [
        ('Hangyeong-myeon', '한경면'), 
        ('Hallim-eup', '한림읍'),
        ('Aewol-eup', '애월읍'), 
        ('Jeju-si', '제주시'), 
        ('Jocheon-eup', '조천읍'), 
        ('Gujwa-eup', '구좌읍'),
        ('Udo-myeon', '우도면'),
        ('Seongsan-eup', '성산읍'),
        ('Pyoseon-myeon', '표선면'),
        ('Namwon-eup', '남원읍'),
        ('Seogwipo-si', '서귀포시'),
        ('Andeok-myeon', '안덕면'),
        ('Daejeong-eup', '대정읍'),
    ]
    
    oreumlevels = [
        ('steep-slope', '경사 심함'),
        ('easy-slope', '경사 완만'),
    ]

    nightviews = [
        ('Good-view', '야경 좋음'),
        ('normal-view', '야경 보통'),
    ]

    oreumlevel = models.CharField(max_length=30, choices=oreumlevels)
    nightview = models.CharField(max_length=30, choices=nightviews)
    location = models.CharField(max_length=50, choices=locations)
    lat = models.FloatField(null =True)
    lng = models.FloatField(null=True)
    mainphoto = models.ImageField(blank=True, null=True)
    subphoto = models.ImageField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    phone = models.CharField(max_length=13, null=True)
    insta = models.CharField(max_length=50, null=True)
    nickname = models.CharField(max_length=30, default="admin")
    
    def __str__(self):
        return self.name

