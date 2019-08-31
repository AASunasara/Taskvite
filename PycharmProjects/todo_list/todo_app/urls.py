from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('register/', views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change_password'),

]
