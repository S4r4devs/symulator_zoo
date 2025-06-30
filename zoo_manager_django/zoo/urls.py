from django.urls import path
from zoo import views

urlpatterns = [
    path("animals/", views.get_animals),
    path("feed/<str:animal_name>/", views.feed_animal),
    path("maintenance/<str:animal_name>/", views.maintenance),
    path("zookeepers/", views.get_zookeepers),
    path("food/", views.get_food_inventory),
    path("login/", views.login),
    path("move/<str:animal_name>/", views.move),
]
