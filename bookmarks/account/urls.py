from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout-then-login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),  
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new-post/$', views.new_post, name='new_post'),
    url(r'^your-posts/$', views.your_posts, name='your_posts'),
    url(r'^delete-post/(?P<id>\d+)/$', views.delete_post, name='delete_post'),
    url(r'^available-add/$', views.add_available, name='add_available'),
    url(r'^category/$', views.show_genres, name='show_genres'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.list_of_post_by_category, name= 'list_of_post_by_category'),
]
