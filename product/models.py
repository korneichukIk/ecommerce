from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Category title')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass

def upload_image(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{0}/{1}'.format(instance.slug, filename)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Category')
    title = models.CharField(max_length=200, db_index=True, verbose_name='Product title')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to=upload_image, blank=True, verbose_name="Product image")
    short_description = models.TextField(max_length=500, blank=True, verbose_name='Short description')
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    stock = models.PositiveIntegerField(verbose_name="Amount")
    available = models.BooleanField(default=True, verbose_name="Is available")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    class Meta:
        ordering = ['title']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
