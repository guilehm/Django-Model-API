from django.db import models
from multiselectfield import MultiSelectField


types = (
    ('1', 'Terno'),
    ('2', 'Calça'),
    ('3', 'Camisa'),
)

sizes = (
    ('32', '32'),
    ('34', '34'),
    ('36', '36'),
    ('38', '38'),
    ('40', '40'),
    ('42', '42'),
    ('44', '44'),
)

# Create your models here.
class Product(models.Model):
    name        = models.CharField('Nome', max_length=80)
    price       = models.DecimalField('Valor', decimal_places=2, max_digits=7)
    quantity    = models.PositiveSmallIntegerField('quantidade')
    img         = models.ImageField(upload_to='core/products')
    type        = models.CharField(max_length=7, choices=types)
    size        = MultiSelectField(choices=sizes)
    slug        = models.SlugField('slug', blank=True)

    def __str__(self):
        return self.name