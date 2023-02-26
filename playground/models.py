# """we will use built-in model classes"""
# from django.db import models

# # Create your models here.
# class Promotion(models.Model):
#     description = models.CharField(max_length=255)
#     discount = models.FloatField()
#     #product_set , django will define this field here, because it auto-performs reverse relationship
#     # we are defining many-to-many relationship with Product, so in reverse django denerates product_set field automatically
#     # in this filed all the products will be listed to whom promotions are applied.

# class Collection(models.Model):
#     title = models.CharField(max_length=255)
#     featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

# class Product(models.Model):
#     """this function will create Product table inside database"""
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     inventory = models.IntegerField()
#     last_update = models.DateTimeField(auto_now=True)
#     # Collection can have many Products, one-to-many relation between Collection and Products
#     # on_delete=models.PROTECT , means if we accidentaly delete a collection, we don't endup deleting all the products
#     # in that collection
#     Collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
#     # Promotion and Product , many-to-many relationships
#     promotions = models.ManyToManyField(Promotion)


# class Customer(models.Model):
#     """this function will create Customer table inside database"""
#     MEMBERSHIP_BRONZE = "B"
#     MEMBERSHIP_SILVER = "S"
#     MEMBERSHIP_GOLD = "G"
#     MEMBERSHIP_CHOICES = [
#         (MEMBERSHIP_BRONZE, 'Bronze'),
#         (MEMBERSHIP_SILVER, 'Silver'),
#         (MEMBERSHIP_GOLD, 'Gold'),
#     ]
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=255)
#     birth_date = models.DateField(null=True)
#     membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

# class Order(models.Model):
#     PAYMENT_STATUS_PENDING = 'P'
#     PAYMENT_STATUS_COMPLETE = 'C'
#     PAYMENT_STATUS_FAILED = 'F'
#     PAYMENT_STATUS_CHOICES = [
#         (PAYMENT_STATUS_PENDING, 'Pending'),
#         (PAYMENT_STATUS_COMPLETE, 'Complete'),
#         (PAYMENT_STATUS_FAILED, 'Failed'),
#     ]
#     placed_at = models.DateTimeField(auto_now_add=True)
#     payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
#      # now Customer can have many addresses, PROTECT MEANS If we delete customer we won't endup deleting all his orders
#      # one-to-many relationship between Customer and Order
#     Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.PROTECT)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)  
#     quantity = models.PositiveSmallIntegerField()
#     unit_price = models.DecimalField(max_digits=6, decimal_places=2)   

# class Address(models.Model):
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     # defined one-to-one relationship between customer and Address
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
#      # defined one-to-many relationship between customer and Address
#      # now Customer can have many addresses
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

# class Cart(models.Model):
#     created_at = models.DateTimeField(auto_now_add = True)

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField()
