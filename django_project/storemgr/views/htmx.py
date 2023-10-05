from handyhelpers.views.htmx import BoostrapModalFormCreateView

# import forms
from storemgr.forms import (
    BrandForm,
    ManufacturerForm,
    ProductAttributeForm,
    ProductForm,
)


class CreateBrandModalView(BoostrapModalFormCreateView):
    form_class = BrandForm
    modal_title = "Create Brand"
    modal_button_submit = "Create"


class CreateManufacturerModalView(BoostrapModalFormCreateView):
    form_class = ManufacturerForm
    modal_title = "Create Manufacturer"
    modal_button_submit = "Create"


class CreateProductModalView(BoostrapModalFormCreateView):
    form_class = ProductForm
    modal_title = "Create Product"
    modal_button_submit = "Create"


class CreateProductAttributeModalView(BoostrapModalFormCreateView):
    form_class = ProductAttributeForm
    modal_title = "Create Attribute"
    modal_button_submit = "Create"
