from handyhelpers.views.htmx import BoostrapModalFormCreateView

# import forms
from storemgr.forms import BrandForm


class CreateBrandModalView(BoostrapModalFormCreateView):
    form_class = BrandForm
    modal_title = "Create Brand"
    modal_button_submit = "Create"
