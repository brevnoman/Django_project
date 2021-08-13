"""psychology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_app.views import register_page,login_request, render_main_page, date_meetings, loguot_user, calendar, user_page, create_meeting, user_page_personal_inform, user_page_meetings, user_page_editing, meeting_conclusion

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("register/", register_page, name="register"),
    path("login/", login_request, name="login"),
    path("", render_main_page, name="main_page"),
    path("logout/", loguot_user, name="logout"),
    path("user_page/pers_inform", user_page_personal_inform, name="user_information"),
    path("user_page/create_meeting/", create_meeting, name="meeting_create_page"),
    path("user_page/meetings/<meeting>", meeting_conclusion, name="user_meeting_conclusions"),
    path("user_page/meetings/", user_page_meetings, name="user_meetings"),
    path("user_page/edit_profile", user_page_editing, name="user_edit_profile"),
    path("user_page/meetings_of_date/<meetings_date>", date_meetings, name="meetings_for_date"),
    path("user_page/", user_page, name="user_page"),
    path("calendar/year=<year>&month=<month>", calendar, name="calendar"),
]
