from django.urls import path
from django.contrib import admin
from sites.views import SiteListCreateView, SiteDetailView,TechnicianListCreateView,TechnicianDetailView
from devices.views import DeviceListCreateView, DeviceDetailView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sites/", SiteListCreateView.as_view(), name="site-list-create"),
    path("sites/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path("technicians/", TechnicianListCreateView.as_view(), name="technician-list-create"),
    path("technicians/<int:pk>/", TechnicianDetailView.as_view(), name="technician-detail"),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path("devices/", DeviceListCreateView.as_view(), name="technician-list-create"),
    path("devices/<int:pk>/", DeviceDetailView.as_view(), name="technician-detail"),
]

