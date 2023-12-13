from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    cafe = models.ForeignKey('Cafe', on_delete=models.CASCADE)
    category = models.TextField()
    name = models.TextField()
    price = models.IntegerField()
    calories = models.FloatField()
    sodium = models.FloatField()
    protein = models.FloatField()
    caffeine = models.FloatField()

    class Meta:
        db_table = 'menu'

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    ingredient_name = models.TextField()
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    stock_amount = models.IntegerField()

    class Meta:
        db_table = 'stock'

class OrderDetails(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'order_details'
        unique_together = (('order', 'menu'),)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    state_code = models.ForeignKey('StateCode', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    cafe = models.ForeignKey('Cafe', on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    total_price = models.IntegerField()
    payment_card = models.TextField()
    card_payment_amount = models.IntegerField(default=0)
    payment_discount = models.TextField(blank=True, null=True)
    discount_payment_amount = models.IntegerField(default=0)

    class Meta:
        db_table = 'order'

class StateCode(models.Model):
    state_code_id = models.AutoField(primary_key=True)
    code_details = models.TextField()

    class Meta:
        db_table = 'state_code'

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    cafe = models.ForeignKey('Cafe', on_delete=models.CASCADE)
    date = models.DateTimeField()
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, blank=True, null=True)
    name = models.TextField()
    discount_rate = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.TextField()

    class Meta:
        db_table = 'event'

class Cafe(models.Model):
    cafe_id = models.AutoField(primary_key=True)
    name = models.TextField()
    place = models.TextField()
    opening_time = models.IntegerField()
    closing_time = models.IntegerField()

    class Meta:
        db_table = 'cafe'

class DaySales(models.Model):
    day = models.DateField()
    cafe = models.ForeignKey('Cafe', on_delete=models.CASCADE)
    total_price = models.IntegerField()
    total_order = models.IntegerField()
    use_coupon = models.IntegerField()
    total_discount = models.IntegerField()

    class Meta:
        db_table = 'day_sales'
        unique_together = (('day', 'cafe'),)

class Basket(models.Model):
    basket_id = models.AutoField(primary_key=True)
    cafe = models.ForeignKey('Cafe', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    class Meta:
        db_table = 'basket'

class BasketDetails(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    payment_status = models.IntegerField(default=0)

    class Meta:
        db_table = 'basket_details'
        unique_together = (('basket', 'menu'),)

class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    receiver = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='received_coupons')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    cafe = models.ForeignKey('Cafe', on_delete=models.CASCADE)
    sender = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='sent_coupons')
    coupon_type = models.TextField()
    remain_amount = models.IntegerField()
    receive_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    use = models.IntegerField(default=1)

    class Meta:
        db_table = 'coupon'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    join_date = models.DateField()
    password = models.TextField()
    email = models.TextField(blank=True, null=True)
    payment_card = models.TextField()
    state = models.TextField()

    class Meta:
        db_table = 'customer'
