from django.db import models

# Create your models here.

class MovieLabel(models.Model):
    label = models.CharField(max_length=20, verbose_name="label")

    def __str__(self):
        return str(self.label)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'labels'
        verbose_name_plural = verbose_name


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="电影名称")
    label = models.ManyToManyField(to=MovieLabel, verbose_name="标签")
    head_pics = models.FileField(upload_to="web/head_pics/", verbose_name="图片")
    movie_url = models.URLField(verbose_name="链接", default="http://")
    validity = models.CharField(max_length=255, verbose_name="电影简介")
    point = models.CharField(max_length=255, verbose_name="观点")
    douban = models.URLField(verbose_name="豆瓣影评", default="http://")
    up_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")

    def up_head_pic_us3(self):
        pass

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'movies'
        verbose_name_plural = verbose_name