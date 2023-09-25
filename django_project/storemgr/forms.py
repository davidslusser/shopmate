from django import forms

# import models
from storemgr.models import Brand, Manufacturer, OrderStatus, Product


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


# class ManufacturerForm(forms.ModelForm):
#     """Form class used to add/edit user Manufacturer objects"""

#     class Meta:
#         model = Manufacturer
#         fields = ["name", "enabled"]
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control"}),
#             "enabled": forms.Select(attrs={"class": "form-control"}, choices=((True, True), (False, False))),
#         }


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "enabled"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the 'form-control' class to both fields
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["enabled"].widget.attrs.update({"class": "form-control"})

        # Mark both fields as required
        self.fields["name"].required = True
        self.fields["enabled"].required = True
