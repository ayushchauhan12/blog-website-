from django.urls import path,re_path
from blog import views

urlpatterns=[
     path('',views.Postlistview.as_view(),name='post_list'),
    path('about/',views.Aboutview.as_view(),name='about'),
    re_path(r'post/(?P<pk>\d+)$',views.Postdetailview.as_view(),name='post_detail'),
    path('post/new/',views.Createpostview.as_view(),name='post_new'),
    re_path(r'post/(?P<pk>\d+)/edit$',views.Postupdateview.as_view(),name='post_edit'),
    re_path(r'post/(?P<pk>\d+)/remove$',views.Postdeleteview.as_view(),name='post_remove'),
    path('drafts/',views.Draftlistview.as_view(),name='post_draft_list'),
    re_path(r'post/(?P<pk>\d+)/publish$',views.post_publish,name='post_publish'),
    re_path(r'post/(?P<pk>\d+)/comment$',views.add_comment_to_post,name='add_comment_to_post'),
    re_path(r'comment/(?P<pk>\d+)/approve$',views.comment_approve,name='comment_approve'),
    re_path(r'comment/(?P<pk>\d+)/remove$',views.comment_remove,name='comment_remove'),


]