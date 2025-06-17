from django.urls import path
from django.contrib import admin
from sites.views import RegisterUserView,SiteListCreateView,SiteUpdateView,SiteDestroyView,SiteDetailView,TechnicianListCreateView,TechnicianDetailView
from devices.views import DeviceListCreateView,MetricsSubcriptionFilteredListView,MetricsSubcriptionDetailView ,DeviceDetailView, DeviceMetricListCreateView, DeviceMetricDetailView ,MetricsSubcriptionListCreateView, MetricsSubcriptionDetailView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #authentication
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path("admin/", admin.site.urls),
    #sites
    path("sites/", SiteListCreateView.as_view(), name="site-list"),
    path("sites/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path("sites/<int:pk>/update/", SiteUpdateView.as_view(), name="site-update"),
    path("sites/<int:pk>/delete/", SiteDestroyView.as_view(), name="site-delete"),
    #technicians
    path("technicians/", TechnicianListCreateView.as_view(), name="technician-list-create"),
    path("technicians/<int:pk>/", TechnicianDetailView.as_view(), name="technician-detail"),
    #devices
    path("devices/", DeviceListCreateView.as_view(), name="device-list-create"),
    path("devices/<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
    #metrics
    path("devices-metrics/", DeviceMetricListCreateView.as_view(), name="device-metric-list-create"),
    path("devices-metrics/<int:pk>/", DeviceMetricDetailView.as_view(), name="device-metric-detail"),
    #metrics subscriptions
    path("metrics-subscription/", MetricsSubcriptionListCreateView.as_view(), name="metric-subscription-create"),
    path("metrics-subscription/<int:pk>/", MetricsSubcriptionDetailView.as_view(), name="metric-subscription-detail"),
    path("metrics-subscriptions-timeframe/",MetricsSubcriptionFilteredListView.as_view(),name="metric-subscription-filtered-list",),
]

