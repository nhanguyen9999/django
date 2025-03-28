from django.db import models

class Segment(models.Model):
    segment_id = models.AutoField(primary_key=True)
    segment_code = models.CharField(max_length=50, unique=True)
    segment_info = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Customer Segment"
        verbose_name_plural = "Customer Segments"

    def __str__(self):
        return self.segment_code

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_code = models.CharField(max_length=50, unique=True)
    segment = models.ForeignKey(Segment, on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.customer_code

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_code = models.CharField(max_length=50, unique=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    bill_code = models.CharField(max_length=50, unique=True)
    time_created = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.bill_code

class BillLine(models.Model):
    bill_line_id = models.AutoField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.bill.bill_code} - {self.product.product_code}"
