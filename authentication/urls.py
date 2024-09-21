from django.urls import path
from . import views


# URL pattern for the login page, directs to the login view
# URL pattern for the callback URL where Auth0 redirects after authentication
# URL pattern for logging out, directs to the logout view
# URL pattern for the index page, the main page users see after login
# URL pattern for the registration page, directs to the registration view


urlpatterns = [
    path("login/", views.login, name="login"),
    path("callback/", views.callback, name="callback"),
    path("logout/", views.logout, name="logout"),
    path("ssologin/", views.loginSSO, name="login_sso"),
    path("", views.index, name="index"),
    path("register/", views.register, name="register")
    ]
