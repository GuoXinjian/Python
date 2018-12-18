from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
import tinymce
# Create your models here.
class Column(models.Model):
    columnId = models.AutoField('栏目id',auto_created=True, primary_key=True, serialize=False)
    name = models.CharField('栏目名称',max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='',blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('column',args=(self.slug,))
    class Meta:
        db_table='column'
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']

class Article(models.Model):
    articleId = models.AutoField('文章id',auto_created=True, primary_key=True, serialize=False)
    column = models.ManyToManyField(Column,verbose_name='所属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    author = models.ForeignKey('auth.User', blank=True, null=True,on_delete=models.DO_NOTHING, verbose_name='作者')
    brief = models.CharField('简述', max_length=256, blank=True,null=True,default='' )
    content = tinymce.models.HTMLField('内容',default='',blank=True)

    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article', args=(self.slug,))
    class Meta:
        db_table='article'
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['pub_date']
'''
class Content(models.Model):
    contentId = models.IntegerField('文章id',auto_created=True, primary_key=True, serialize=False)
    articleId = models.OneToOneField(Article,on_delete=models.CASCADE,db_index=True)
    content = models.TextField('内容',default='',blank=True)

    class Meta:
        db_table='content'
        verbose_name = '内容'
        verbose_name_plural = '内容'
        ordering = ['articleId']
'''
