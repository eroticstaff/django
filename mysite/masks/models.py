from django.db import models

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    img_url = models.CharField(max_length=200, default=0)
    def __unicode__(self):
        return str(self.product_name, 'utf-8')
