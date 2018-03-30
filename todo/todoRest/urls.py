from rest_framework.urls import url

from .views import TodoListView, TodoDetailsView, UsersListView, UserDetailsView

urlpatterns = [
    url(r'^todos/$', TodoListView.as_view()),
    url(r'^todos/(?P<pk>[0-9]+)/$', TodoDetailsView.as_view()),
    url(r'^users/$', UsersListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view())
]
