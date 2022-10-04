from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category')
    class Meta:
        ordering=('name',)
        verbose_name='Category'
        verbose_name_plural='Categories'
    def get_url(self):
        return reverse('shopapp:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product')
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def get_url(self):
        return reverse('shopapp:prodetailview',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)



