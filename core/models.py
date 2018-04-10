from django.db import models


types = (
    ('1', 'Terno'),
    ('2', 'Calça'),
    ('3', 'Camisa'),
)


# Create your models here.
class Product(models.Model):
    name        = models.CharField('Nome', max_length=80)
    price       = models.DecimalField('Valor', decimal_places=2, max_digits=7)
    quantity    = models.PositiveSmallIntegerField('quantidade')
    img         = models.ImageField(upload_to='core/products')
    type        = models.CharField(max_length=7, choices=types)
    slug        = models.SlugField('slug', blank=True)

    def __str__(self):
        return self.name