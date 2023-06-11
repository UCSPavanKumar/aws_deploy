from django.urls import path

from . import views

urlpatterns = [
    path("clients/", views.clientListAll, name="clientListAll"),
    path("agents/", views.agentListAll, name="agentListAll"),
    path('createClient/',views.createClient,name='createClient'),
     path('createAgent/',views.createClient,name='createAgent'),
    path('client/<str:pk>/',views.client_details,name='client_details'),
    path('agent/<str:pk>/',views.agent_details,name='agent_details'),
]