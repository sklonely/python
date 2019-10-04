from django.db import models

# Create your models here.
class PageData(models.Model):
    name = models.CharField(max_length = 20) # 資料的名稱
    time = models.DateField() # 資料創立的時間
    data = models.CharField(max_length = 20) # 資料內容
	