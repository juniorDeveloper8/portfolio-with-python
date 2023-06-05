from django.urls import path
from blog.views import article, post_detail  

app_name = 'blog'

urlpatterns = [
    path('', article, name='article'),
    path('<int:posts_id>', post_detail, name='detail') 
]

