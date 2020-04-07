from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField(blank=False)
    available = models.BooleanField(default=True)
    special_offer = models.BooleanField(default=False)
    bestseller = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    bullet1 = models.CharField(max_length=150, blank=True)
    bullet2 = models.CharField(max_length=150, blank=True)
    bullet3 = models.CharField(max_length=150, blank=True)
    bullet4 = models.CharField(max_length=150, blank=True)
    bullet5 = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'))  # For querying products by id & slug

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
