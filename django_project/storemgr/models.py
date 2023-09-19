from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel
from handyhelpers.views.report import get_colors


class Brand(HandyHelperBaseModel):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name

    def disable(self):
        """disable this brand and all of its products"""
        self.enabled = False
        self.product_set.update(enabled=False)
        self.save()

    def get_absolute_url(self) -> str:
        return reverse("storemgr:detail_brand", kwargs={"pk": self.pk})

    @staticmethod
    def get_icon() -> str:
        return """<i class="fa-solid fa-language"></i>"""

    def get_products(self):
        return self.product_set.all()
    
    def get_orders(self):
        return Order.objects.filter(products__brand=self).select_related("status")

    def get_orders_by_product(self):
        order_qs = self.get_orders().values('products__sku').annotate(qty=models.Count('products__sku'))
        return dict(
            id="orders_by_product",
            type="bar",
            label_list=[i['products__sku'] for i in order_qs],
            value_list=[i['qty'] for i in order_qs],
            list_view=f"/storemgr/list_orders?products__brand__name={self.name}&products__sku=",
            color_list=get_colors(order_qs.count()),
        )

    def get_orders_by_status(self):
        order_qs = self.get_orders().values('status__name').annotate(qty=models.Count('status__name'))
        return dict(
            id="orders_by_status",
            type="bar",
            label_list=[i['status__name'] for i in order_qs],
            value_list=[i['qty'] for i in order_qs],
            list_view=f"/storemgr/list_orders?products__brand__name={self.name}&status__name=",
            color_list=get_colors(order_qs.count()),
        )


class Customer(HandyHelperBaseModel):
    customer_id = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.customer_id

    def get_absolute_url(self) -> str:
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

    def get_absolute_url(self) -> str:
        return reverse("storemgr:invoice", kwargs={"pk": self.pk})


class Manufacturer(HandyHelperBaseModel):
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
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

    def get_brands(self):
        return self.brand_set.all()

    def get_orders(self):
        return Order.objects.filter(products__brand__manufacturer=self).select_related("status")

    def get_orders_by_product(self):
        order_qs = self.get_orders().values('products__sku').annotate(qty=models.Count('products__sku'))
        print('TEST: ', order_qs)
        return dict(
            id="orders_by_product",
            type="bar",
            label_list=[i['products__sku'] for i in order_qs],
            value_list=[i['qty'] for i in order_qs],
            list_view=f"/storemgr/list_orders?products__brand__manufacturer__name={self.name}&products__sku=",
            color_list=get_colors(order_qs.count()),
        )

    def get_products(self):
        return Product.objects.filter(brand__manufacturer=self)


class Order(HandyHelperBaseModel):
    order_id = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    status = models.ForeignKey("OrderStatus", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", blank=True, through="Invoice")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.order_id

    def get_absolute_url(self) -> str:
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

    def __repr__(self) -> str:
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

    def get_absolute_url(self) -> str:
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
