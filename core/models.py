from django.db import models

# Create your models here.
class Product(models.Model):
    name        = models.CharField('Nome', max_length=80)
    price       = models.DecimalField('Valor', decimal_places=2, max_digits=7)
    quantity    = models.PositiveSmallIntegerField('quantidade')
    img         = models.ImageField(upload_to='core/products')

    def __str__(self):
        return self.name