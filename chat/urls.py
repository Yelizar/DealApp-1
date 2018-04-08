from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'chat'
urlpatterns = [
    path('chat/', views.ChatView.as_view(), name="chat"),
    path("chat/<int:chat_id>/", views.MessageView.as_view(), name="message"),
    path('chat/create/<int:user_id>/', views.CreateSessionView.as_view(), name='create_session')
]