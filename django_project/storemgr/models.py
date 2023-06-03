from django.db import models
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel


class Brand(HandyHelperBaseModel):
    name = models.CharField(max_length=16, unique=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_icon():
        return """<i class="fa-solid fa-language"></i>"""

    def disable(self):
        """disable this brand and all of its products"""
        self.enabled = False
        self.product_set.update(enabled=False)
        self.save()


class Customer(HandyHelperBaseModel):
    customer_id = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.EmailField(blank=True, null=True)

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

    @staticmethod
    def get_icon():
        return """<i class="fa-solid fa-user-tag"></i>"""


class Invoice(HandyHelperBaseModel):
    order = models.ForeignKey("Order", blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", blank=True, null=True, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1, blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return getattr(self.order, "order_id", str(self.pk))


class Order(HandyHelperBaseModel):
    order_id = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    status = models.ForeignKey("OrderStatus", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", blank=True, through="Invoice")

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

    @staticmethod
    def get_icon():
        return """<i class="fa-solid fa-receipt"></i>"""


class OrderStatus(HandyHelperBaseModel):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(HandyHelperBaseModel):
    sku = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, blank=True, null=True)
    attributes = models.ManyToManyField("ProductAttribute", blank=True)
    enabled = models.BooleanField(default=True)

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

    @staticmethod
    def get_icon():
        return """<i class="fa-brands fa-product-hunt"></i>"""


class ProductAttribute(HandyHelperBaseModel):
    key = models.CharField(max_length=16)
    value = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.key

    class Meta:
        unique_together = (("key", "value"),)


# Models to register with AuditLog
auditlog.register(Brand)
auditlog.register(Customer)
auditlog.register(Order)
auditlog.register(Product)
