from django import forms

# import models
from storemgr.models import (Brand, OrderStatus, Product)


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
