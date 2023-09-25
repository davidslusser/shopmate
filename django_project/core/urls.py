"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", logout_then_login, name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("userextensions/", include("userextensions.urls")),
    path("handyhelpers/", include("handyhelpers.urls")),
    path("hostutils/", include("djangoaddicts.hostutils.urls")),
    path("pygwalker/", include("djangoaddicts.pygwalker.urls")),
    # API documentation
    path("rest/schema/", SpectacularAPIView.as_view(), name="schema"),
    # path("api/swagger/", cache_page(120 * 15)(SpectacularSwaggerView.as_view(url_name="schema")), name="swagger"),
    path("rest/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    # path("api/redoc/", cache_page(120 * 15)(SpectacularRedocView.as_view(url_name="schema")), name="redoc"),
    path("rest/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("", include("storemgr.urls", namespace="root")),
    path("storemgr/", include("storemgr.urls", namespace="storemgr")),
]

if settings.DEBUG:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
