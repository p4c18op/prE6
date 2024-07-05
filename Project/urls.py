from django.contrib import admin
from django.urls import path, include
from chatback import views as chat_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', chat_views.register, name='signup'),
    path('account/', chat_views.profile, name='account'),
    path('login/', auth_views.LoginView.as_view(
        template_name='chat/registration/login.html'), name='login'),
    path('', include('chat.urls')),
]
