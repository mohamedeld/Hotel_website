from django.urls import path
from .views import PropertyList,PropertyDetail
from .api_view import PropertyApiView,PropertyRetrieveAPIView
app_name = 'property'

urlpatterns =[
    path('',PropertyList.as_view(),name='property_list'),
    path('<slug:slug>/',PropertyDetail.as_view(),name='property_detail'),
    
    path('api/list/',PropertyApiView.as_view(),name='property_api_view'),
    path('api/list/<int:pk>/',PropertyRetrieveAPIView.as_view(),name='retrieve_property_api_view'),
]
