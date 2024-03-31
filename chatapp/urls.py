from django.urls import path
from chatapp import views

app_name = "chatapp"



urlpatterns = [

    path("", views.chats, name="chats"),
    path("friend/<str:pk>/", views.detail, name="detail"),
    path("register/", views.register, name="register"),
    path("friend-requests/",  views.friend_request, name="f-requests"),
    path("login/", views.signin, name="signin"),
    path("logout/", views.signout, name="signout"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("suggestions/", views.suggestion, name="suggestions"),
    path("notifications/", views.notifications, name="notifications"),
    path("send-friend-request/", views.send_friend_request, name="send-request"),
    path("cancel-friend-request/", views.cancel_friend_request, name="cancel-request"),
    path("accept-friend-request/", views.accept_friend_request, name="accept-request"),
    path("reject-friend-reques/t", views.reject_friend_request, name="reject-request"),
    path("get-friend-request/", views.fetch_friend_request,
         name="get-friend-request"),
    path("get-notifications/", views.fetch_notification, name="get-notifications"),
    path("notifyMessageCount/", views.fetch_message, name="notifyMessageCount"),
    path("create-chat/", views.createChat, name="create-chat"),
    path('get-new-chats/', views.getChats, name='get-chats'),
]
