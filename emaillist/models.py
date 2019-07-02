from django.db import models

# Create your models here.
class Emaillist(models.Model):

    first_name = models.CharField(max_length=50)  # char 타입이면  # 클래스 변수
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'Emaillist({self.first_name}, {self.last_name}, {self.email})'

    # 1 대 다 관계를 여기에 mapping 하면 자연스럽게 외래키 생성됨

