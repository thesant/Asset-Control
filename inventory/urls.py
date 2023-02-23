from django.urls import path

from inventory.views import Report, SearchResultsView

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.home, name='home'),
    path('report/', Report.as_view(), name='report'),
    path('search/',  SearchResultsView.as_view(), name='search_results'),

    path('item/create/', views.item_create, name='item_create'),
    path('items/register/create', views.item_register, name='item_register'),
    path('item/read/', views.item_read, name='item_read'),
    path('item/update/<int:pk>', views.item_update, name='item_update'),
    path('items/delete/<int:pk>', views.item_delete, name='item_delete'),
]
