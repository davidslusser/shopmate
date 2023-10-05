from django.shortcuts import render
from django.views.generic import View


class TestView(View):
    title = "Test View"
    template_name = "storemgr/custom/test2.html"

    def get(self, request):
        """ """
        context = {}
        return render(request, self.template_name, context=context)


class GetModal(View):
    def get(self, request):
        return render(request, "storemgr/custom/modal.htm")
