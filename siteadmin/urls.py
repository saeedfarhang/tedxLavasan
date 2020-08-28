from django.urls import path
from . import views

app_name = 'siteadmin'
urlpatterns = [
    path('',views.login_view , name = 'loginurl'),
    path('logout',views.logout_view , name = 'logouturl'),
    path('admin',views.admin_view , name = 'adminurl'),
    path('admin/addspeaker',views.addspeakerView , name = 'addspeakerurl'),
    path('admin/addteam',views.addteamView , name = 'addteamurl'),
    path('admin/editspeaker/<speakerid>',views.editspeakerView , name = 'editspeakerurl'),
    path('admin/editteam/<teamid>',views.editteamView , name = 'editteamurl'),
]
