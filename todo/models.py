from django.db import models

# Create your models here.

# タプル型で優先度のキーと値を指定する
# ('中身のデータ','表示のデータ')
PRIORITY = (('danger','high'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY # プルダウン型で指定したタプル型から選ぶ
    )
    duedate = models.DateField()

    def __str__(self): #オブジェクトを文字列で返す
        return self.title # タイトルをそのまま返す
