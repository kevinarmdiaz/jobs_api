from django.urls import path
from jobs.api.views import JobListCreateAPIView,JobDetailAPIView
#from news.api.views import article_list_create_api_view, article_detail_api_view

urlpatterns = [
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>", article_detail_api_view, name="article-detail")
    path("jobs/", 
    JobListCreateAPIView.as_view(), 
    name="job-list"),

    path("jobs/<int:pk>", 
    JobDetailAPIView.as_view(), 
    name="job-detail"),
]