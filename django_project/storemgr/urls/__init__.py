from .api import urlpatterns as api_urls
from .gui import urlpatterns as gui_urls

app_name = "storemgr"

urlpatterns = api_urls + gui_urls
