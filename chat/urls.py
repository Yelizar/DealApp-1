from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'chat'
urlpatterns = [
    path("", login_required(views.ChatView.as_view()), name="chat"),
]