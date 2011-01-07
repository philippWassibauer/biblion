from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template
from biblion.settings import SECTION_IN_URL

urlpatterns = patterns("",
    url(r'^$', "biblion.views.blog_index", name="blog"),
    url(r'^post/(?P<post_pk>\d+)/$', "biblion.views.blog_post_detail", name="blog_post_pk"),
    url(r'^(?P<section>[-\w]+)/$', "biblion.views.blog_section_list", name="blog_section"),
    url(r'^(?P<section>[-\w]+)/(?P<category>\d+)/$', 
            "biblion.views.posts_of_category", name="posts_of_category"),
)



if SECTION_IN_URL:
    urlpatterns += patterns("",
        url(r'^(?P<section>[-\w]+)/(?P<slug>[-\w]+)/sdfsdf$', 
            "biblion.views.blog_post_detail", name="blog_post"),
    )
else:
    urlpatterns += patterns("",
        url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
            "biblion.views.blog_post_detail", name="blog_post"),
    )