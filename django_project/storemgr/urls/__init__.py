from .rest import urlpatterns as rest_urls
from .gui import urlpatterns as gui_urls

app_name = "storemgr"

urlpatterns = rest_urls + gui_urls
