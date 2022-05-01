from django.urls import path
from . import views
from .views import create_comment, home ,blog,postdetail,userdetail,save_comment,EEL1010,CT


urlpatterns = [
# path('search', search, name="search"),
path('',home ,name = "home"),
path('blog/',blog,name ="blog"),
path('create_comment/<int:cid>/',create_comment, name ="create_comment"),
# path('course/IIEE/',IIEE,name= )
path("couse/EEL1010/",EEL1010,name = "EEL1010"),
path("couse/CT/",CT,name = "CT"),

path('post/<int:cid>/',postdetail , name='postpage'),
path('user/<int:cid>/',userdetail , name='userpage'),
path('save_comment/<int:cid>/',save_comment , name = 'savecomment'),
]
