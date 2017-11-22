from django.conf.urls import url

from blog.views import show_post, all_posts, all_categories, show_category, search

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/$', show_post, name="post"),
    url(r'^post/all/$', all_posts, name="all_post"),
    url(r'^category/all/$', all_categories, name="all_categories"),
    url(r'^category/(?P<pk>\d+)/$', show_category, name="show_category"),
    url(r'^search/$', search, name="search"),
    ]
