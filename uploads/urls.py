from django.urls import path
from .views import UploadListView,  UploadDetailView, UploadCreateView, HomePageView

urlpatterns = [

    path('upload/new/', UploadCreateView.as_view(), name='upload_new'),  # new
    path('upload/<int:pk>/', UploadDetailView.as_view(), name='image_detail'),  # new
    path('home', HomePageView.as_view(), name='home'),
    path('', UploadListView.as_view(), name='upload_home'), 

]
