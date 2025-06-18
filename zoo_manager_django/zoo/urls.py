from django.urls import path
from zoo import views

urlpatterns = [
    path("animals/", views.get_animals),
    path("feed/<str:animal_name>/", views.feed_animal),
    path("zookeepers/", views.get_zookeepers),
    path("zookeepers/add/", views.add_zookeeper),
    path("food/", views.get_food_inventory),  # Add food endpoint
]
