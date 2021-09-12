from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """ Таблица "Товаров"
    
    
    id
    Название товара
    Ссылка на товар
    Цена на товар
    Дата и время создания записи    
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return self.title

class WishList(models.Model):
    """ Таблица "Список желаемых подарков"
    
    
    id
    Название
    Владелец (Пользователь)
    Товары - ManyToMany
    Скрыт ли - bool
    """
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title
