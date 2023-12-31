from django.db import models
from django.core.validators import MinValueValidator
from user_view.models import User


class Category(models.Model):
    CHOICES = (('Wardrobes', 'Wardrobes'), ('Chairs', 'Chairs'),
               ('Beds', 'Beds'), ('Washing machines', 'Washing machines'),
               ('Tables', 'Tables'))

    parent_category_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, choices=CHOICES)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.name}, {self.price}'

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

