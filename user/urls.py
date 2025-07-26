from django.urls import path
from user.views import login_page
app_name = 'user'

urlpatterns = [
    path('login/', login_page, name='login_page'),
]