from django.urls import path
from . import views

app_name= 'catalogapp'
urlpatterns = [
    path('',views.index, name='index'),  
    path('product/<int:product_id>',views.product_detail, name='product_detail'),

    # path('blog',views.blog, name='blog'),
    # path('mentor',views.mentor, name='mentor'),
    # path('mentee',views.mentee, name='mentee'),
    # path('author',views.author, name='author'),
    # path('input_blog',views.input_blog, name='input_blog'),
    # path('save_new_blog',views.save_new_blog, name='save_new_blog'),
    # # path('article-base',views.article_base, name='article-base' ),
    # path('post/<int:blog_id>', views.article_base, name='article-base'),

]

