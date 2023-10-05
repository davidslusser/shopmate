from django import forms

# import models
from storemgr.models import Brand, Manufacturer, OrderStatus, Product, ProductAttribute


class FilterBrandForm(forms.Form):
    """Form class used to filter Brand list view"""

    def __init__(self, *args, **kwargs):
        super(FilterBrandForm, self).__init__(*args, **kwargs)

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Manufacturer",
    )
    enabled = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}), choices=((True, True), (False, False)), required=False
    )


class FilterCustomerForm(forms.Form):
    """Form class used to filter Customer list view"""

    def __init__(self, *args, **kwargs):
        super(FilterCustomerForm, self).__init__(*args, **kwargs)

    customer_id__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Customer ID"
    )
    first_name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="First Name"
    )
    last_name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Last Name"
    )
    email__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Email"
    )


class FilterManufacturerForm(forms.Form):
    """Form class used to filter Manufacturer list view"""

    def __init__(self, *args, **kwargs):
        super(FilterManufacturerForm, self).__init__(*args, **kwargs)

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )
    enabled = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}), choices=((True, True), (False, False)), required=False
    )


class FilterProductForm(forms.Form):
    """Form class used to filter Product list view"""

    def __init__(self, *args, **kwargs):
        super(FilterProductForm, self).__init__(*args, **kwargs)

    sku__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Sku"
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Brand",
    )
    description__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Description"
    )
    enabled = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}), choices=((True, True), (False, False)), required=False
    )


class FilterOrderForm(forms.Form):
    """Form class used to filter Order list view"""

    def __init__(self, *args, **kwargs):
        super(FilterOrderForm, self).__init__(*args, **kwargs)

    order_id__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Order ID"
    )
    status = forms.ModelChoiceField(
        queryset=OrderStatus.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), required=False
    )
    products = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Product",
    )

    products__brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Brand",
    )


class ProductAttributeForm(forms.ModelForm):
    """Form class used to add/edit user ProductAttribute objects"""

    class Meta:
        model = ProductAttribute
        fields = ["key", "value"]
        widgets = {
            "key": forms.TextInput(attrs={"class": "form-control"}),
            "value": forms.TextInput(attrs={"class": "form-control"}),
        }


class BrandForm(forms.ModelForm):
    """Form class used to add/edit user Brand objects"""

    class Meta:
        model = Brand
        fields = ["manufacturer", "name", "enabled"]
        widgets = {
            "manufacturer": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "enabled": forms.Select(attrs={"class": "form-control"}, choices=((True, True), (False, False))),
        }


class ManufacturerForm(forms.ModelForm):
    """Form class used to add/edit user Manufacturer objects"""

    class Meta:
        model = Manufacturer
        fields = ["name", "enabled"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "enabled": forms.Select(attrs={"class": "form-control"}, choices=((True, True), (False, False))),
        }


class ProductForm(forms.ModelForm):
    """Form class used to add/edit user Product objects"""

    choices = [(None, "---------")]
    choices.extend([(i.id, i.value) for i in ProductAttribute.objects.all()])
    product_attributes = forms.MultipleChoiceField(
        choices=choices,
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        label="Attributes",
        required=False,
    )

    class Meta:
        model = Product
        fields = ["brand", "description", "enabled"]
        widgets = {
            "brand": forms.Select(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "enabled": forms.Select(attrs={"class": "form-control"}, choices=((True, True), (False, False))),
        }
