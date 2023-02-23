from django.db import models

levels = [
    ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')
]


class Base(models.Model):
    created = models.DateField('Creation Date', auto_now_add=True)
    modified = models.DateField('Update Date', auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField("Nome", max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Store(Base):
    name = models.CharField('Name', max_length=50)
    number_store = models.IntegerField("Number Store")

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.name


class Items(Base):
    categoryId = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    storeId = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='store')
    name = models.CharField("Name", blank=False, max_length=50)
    brand = models.CharField("Brand", max_length=50)
    model = models.CharField("Model", max_length=50)
    patrimony = models.CharField("Nº patrimony", unique=True, max_length=50)
    obs = models.TextField('Observation', max_length=255)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class Priority(Base):
    description = models.CharField('Description', max_length=200)
    classification = models.CharField(
        'Classification', choices=levels, max_length=6)

    class Meta:
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'

    def __str__(self):
        return self.description
