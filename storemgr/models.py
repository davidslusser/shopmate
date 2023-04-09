from django.db import models
from handyhelpers.models import HandyHelperBaseModel


class ProductAttribute(HandyHelperBaseModel):
    key = models.CharField(max_length=16)
    value = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        unique_together = (("key", "value"),)


class Product(HandyHelperBaseModel):
    sku = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    attributes = models.ManyToManyField(ProductAttribute, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.sku

    def save(self, *args, **kwargs):
        if not self.pk:
            if Product.objects.count() < 1:
                self.sku = "SKU-" + "1".zfill(8)
            else:
                self.sku = "SKU-" + str(Product.objects.count() + 1).zfill(8)
        super(Product, self).save(*args, **kwargs)


class OrderStatus(HandyHelperBaseModel):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Customer(HandyHelperBaseModel):
    customer_id = models.CharField(
        max_length=16, unique=True, blank=True, primary_key=True
    )
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.customer_id

    def save(self, *args, **kwargs):
        if not self.pk:
            if Customer.objects.count() < 1:
                self.customer_id = "CU-" + "1".zfill(8)
            else:
                self.customer_id = "CU-" + str(Customer.objects.count() + 1).zfill(8)
        super(Customer, self).save(*args, **kwargs)


class Order(HandyHelperBaseModel):
    order_id = models.CharField(
        max_length=16, unique=True, blank=True, primary_key=True
    )
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.order_id

    def save(self, *args, **kwargs):
        if not self.pk:
            if Order.objects.count() < 1:
                self.order_id = "OR-" + "1".zfill(8)
            else:
                self.order_id = "OR-" + str(Order.objects.count() + 1).zfill(8)
        super(Order, self).save(*args, **kwargs)
