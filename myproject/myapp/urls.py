from django.urls import path
from . import views

urlpatterns = [
    path('tree/<int:node_id>/', views.tree_view, name='tree_view'),
]
