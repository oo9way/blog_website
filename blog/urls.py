from django.urls import path
from .views import main_page, post_detail, resume_page, message_page


urlpatterns = [
    path("", main_page, name="main"),
    path("posts/<int:post_id>/", post_detail, name="detail"),
    path("resume/", resume_page, name="resume"),
    path("message/", message_page, name="message")
]
