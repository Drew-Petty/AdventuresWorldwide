from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('main',views.main),
    path('new_guide',views.new_guide),
    path('create_guide', views.create_guide),
    path('profile',views.profile),
    path('view_guide/<int:guide_id>', views.view_guide),
    path('edit_profile',views.edit_profile),
    path('update_profile_picture',views.update_profile_picture),
    path('update_guide',views.update_guide),
    path('new_trip',views.new_trip),
    path('create_trip',views.create_trip),
    path('view_trip/<int:trip_id>',views.view_trip),
    path('edit_trip/<int:trip_id>',views.edit_trip),
    path('update_trip_picture/<int:trip_id>',views.update_trip_picture),
    path('update_trip/<int:trip_id>',views.update_trip),
    path('delete_trip/<int:trip_id>',views.delete_trip),
    
]