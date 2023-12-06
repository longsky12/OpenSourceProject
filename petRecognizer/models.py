from django.db import models


class PetImage(models.Model):
    image = models.ImageField(upload_to='petImage')
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pet Image {self.id}"

class PetBreed(models.Model):
    BREED_CHOICES = [
        ('cat-Abyssinian', '아비시니안 고양이'),
        ('cat-Bengal', '벵갈 고양이'),
        ('cat-Birman', '버먼 고양이'),
        ('cat-Bombay', '봄베이 고양이'),
        ('cat-British_Shorthair', '브리티시 쇼트헤어 고양이'),
        ('cat-Egyptian_Mau', '이집션 마우 고양이'),
        ('cat-Maine_Coon', '메인쿤 고양이'),
        ('cat-Persian', '페르시안 고양이'),
        ('cat-Ragdoll', '랙돌 고양이'),
        ('cat-Russian_Blue', '러시안 블루 고양이'),
        ('cat-Siamese', '샴 고양이'),
        ('cat-Sphynx', '스핑크스 고양이'),
        ('dog-american_bulldog', '아메리칸 불독'),
        ('dog-american_pit_bull_terrier', '아메리칸 핏불 테리어'),
        ('dog-basset_hound', '바셋 하운드'),
        ('dog-beagle', '비글'),
        ('dog-boxer', '복서'),
        ('dog-chihuahua', '치와와'),
        ('dog-english_cocker_spaniel', '잉글리시 코커 스패니얼'),
        ('dog-english_setter', '르웰린'),
        ('dog-german_shorthaired', '저먼 쇼트헤어드 포인터'),
        ('dog-great_pyrenees', '그레이트 피레니즈'),
        ('dog-havanese', '하바나'),
        ('dog-japanese_chin', '제페니스 친'),
        ('dog-keeshond', '키스혼드'),
        ('dog-leonberger', '레온베르거'),
        ('dog-miniature_pinscher', '미니어처 핀셔'),
        ('dog-newfoundland', '뉴펀들랜드'),
        ('dog-pomeranian', '포메라니안'),
        ('dog-pug', '퍼그'),
        ('dog-saint_bernard', '세인트 버나드'),
        ('dog-samoyed', '사모예드'),
        ('dog-scottish_terrier', '스코티시 테리어'),
        ('dog-shiba_inu', '시바 이누'),
        ('dog-staffordshire_bull_terrier', '스타포드셔 불 테리어'),
        ('dog-wheaten_terrier', '휘튼 테리어'),
        ('dog-yorkshire_terrier', '요크셔테리어'),
    ]

    breed = models.CharField(max_length=50,choices=BREED_CHOICES)
    description = models.CharField(max_length=511)

    def __str__(self):
        return f"Breed : {self.breed}"
    
class PetNews(models.Model):
    headline = models.CharField(max_length=200)
    headlineUrl = models.URLField()

    def __str__(self):
        return self.headline