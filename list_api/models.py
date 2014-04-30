from django.db import models


class ShoppingList(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey('auth.User', related_name='shopping_lists')

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class ShoppingItem(models.Model):
    name = models.CharField(max_length=64)
    shopping_list = models.ForeignKey(ShoppingList, related_name='shopping_items')
    category = models.ForeignKey(Category, related_name='shopping_items', null=True, blank=True)

    def __unicode__(self):
        return self.name

