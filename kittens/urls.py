from django.urls import path
from .views import KittenDetailView, KittenListView
urlpatterns = [path("", KittenListView.as_view(), name="kitten_list"), path("<slug:slug>/", KittenDetailView.as_view(), name="kitten_detail")]
