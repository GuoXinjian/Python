from django.db import models

# Create your models here.
class User(models.Model):
    gender =(
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length = 256,verbose_name='用户名')
    password = models.CharField(max_length = 256,verbose_name='密码')
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender,default='男')
    c_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'