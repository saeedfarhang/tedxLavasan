from django.urls import path
from . import views

app_name = 'siteadmin'
urlpatterns = [
    path('',views.login_view , name = 'loginurl'),
    path('logout',views.logout_view , name = 'logouturl'),
    path('admin',views.admin_view , name = 'adminurl'),
    path('admin/edit/<speakerid>',views.editspeakerView , name = 'editspeakerurl'),
]
