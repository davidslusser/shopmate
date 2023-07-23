from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel


class Brand(HandyHelperBaseModel):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("storemgr:detail_brand", kwargs={"pk": self.pk})

    @staticmethod
    def get_icon() -> str:
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

    def get_absolute_url(self):
        return reverse("storemgr:detail_customer", kwargs={"pk": self.pk})

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
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return getattr(self.order, "order_id", str(self.pk))

    def get_absolute_url(self):
        return reverse("storemgr:invoice", kwargs={"pk": self.pk})


class Manufacturer(HandyHelperBaseModel):
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("storemgr:detail_manufacturer", kwargs={"pk": self.pk})

    @staticmethod
    def get_icon() -> str:
        return """<i class="fa-solid fa-industry"></i>"""

    def disable(self):
        """disable this manufacturer and all of its brands and products"""
        self.enabled = False
        self.brand_set.update(enabled=False)
        for brand in self.brand_set.all():
            brand.product_set.update(enabled=False)
        self.save()


class Order(HandyHelperBaseModel):
    order_id = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    status = models.ForeignKey("OrderStatus", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", blank=True, through="Invoice")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.order_id

    def get_absolute_url(self):
        return reverse("storemgr:detail_order", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.pk:
            if Order.objects.count() < 1:
                self.order_id = "OR-" + "1".zfill(8)
            else:
                self.order_id = "OR-" + str(Order.objects.count() + 1).zfill(8)
        super(Order, self).save(*args, **kwargs)

    @staticmethod
    def get_icon() -> str:
        return """<i class="fa-solid fa-receipt"></i>"""

    def get_invoice(self):
        """get the quantity (qty) of unique products in this order"""
        return self.products.all().annotate(qty=models.Count('invoice'))

    invoice = property(get_invoice)


class OrderStatus(HandyHelperBaseModel):
    name = models.CharField(max_length=16, unique=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("storemgr:orderstatus", kwargs={"pk": self.pk})


class Product(HandyHelperBaseModel):
    sku = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, blank=True, null=True)
    attributes = models.ManyToManyField("ProductAttribute", blank=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.sku

    def get_absolute_url(self):
        return reverse("storemgr:detail_product", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.pk:
            if Product.objects.count() < 1:
                self.sku = "SKU-" + "1".zfill(8)
            else:
                self.sku = "SKU-" + str(Product.objects.count() + 1).zfill(8)
        super(Product, self).save(*args, **kwargs)

    @staticmethod
    def get_icon() -> str:
        return """<i class="fa-brands fa-product-hunt"></i>"""


class ProductAttribute(HandyHelperBaseModel):
    key = models.CharField(max_length=16)
    value = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self) -> str:
        return self.key

    def get_absolute_url(self):
        return reverse("storemgr:productattribute", kwargs={"pk": self.pk})

    class Meta:
        unique_together = (("key", "value"),)


# Models to register with AuditLog
auditlog.register(Brand)
auditlog.register(Customer)
auditlog.register(Manufacturer)
auditlog.register(Order)
auditlog.register(Product)
