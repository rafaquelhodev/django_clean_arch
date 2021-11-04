from django.conf.urls import url
from django_project.app.api import views

urlpatterns = [
    url(r"^tutors/$", views.TutorView.as_view()),
    url(r"^tutors/(?P<pk>[0-9]+)/$", views.TutorDetailView.as_view()),
]
