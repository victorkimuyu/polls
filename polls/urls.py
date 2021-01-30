from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Ex: /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # Ex: /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # Ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Ex: /polls/5/vote/
]
