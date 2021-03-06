from django.conf.urls import patterns, include, url
from mybbs import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$',views.index),
    (r'^todetail/(\d+)/$',views.todetail),
    (r'^detail/(\d+)/$',views.detail),
    (r'^category/(\d+)/$',views.category),
    (r'^sub_comment/$', views.sub_comment),
    (r'^login/$',views.login),
    (r'^logout/$',views.logout),
    (r'^acc_login/$',views.acc_login),
    (r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^bbs_pub/$', views.bbs_pub),
    (r'^bbs_sub/$', views.bbs_sub),
    (r'^register/$', views.register),
    (r'^regio/$', views.regio),
    (r'^zan/$', views.zan),
    (r'^cai/$', views.cai),
    (r'^zan2/$', views.zan2),
    (r'^cai2/$', views.cai2),
    (r'^zan3/$', views.zan3),
    (r'^cai3/$', views.cai3),
    (r'^edit/$', views.edit),
    (r'^editall/$', views.editall),
    (r'^infavor/$', views.infavor),
    (r'^infavor2/$', views.infavor2),
    (r'^outfavor/$', views.outfavor),
    (r'^favorite/$', views.favorite),
    (r'^search/$', views.search),
    (r'^search2/$', views.search2),
    (r'^hot/(\d+)/$', views.hot),
    (r'^new/(\d+)/$', views.new),
    (r'^commentwow/(\d+)/$', views.commentwow),
    (r'^myidea/$', views.myidea),
)

