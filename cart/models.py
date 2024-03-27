from django.db import models
from django.contrib.auth.models import User
from Course_app.models import Course
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def total_price(self):
        total = 0
        for item in self.cart_items.all():
            total += item.total_price()
        return total
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.course.CourseName}"

    def total_price(self):
        return self.quantity * self.course.CoursePrice