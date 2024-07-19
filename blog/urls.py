from django.urls import path
from .views import main_page, post_detail


urlpatterns = [
    path("", main_page, name="main"),
    path("posts/<int:post_id>/", post_detail, name="detail")
]
