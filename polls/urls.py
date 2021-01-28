from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),  # Ex: /polls/
    path('<int:question_id>/', views.detail, name='detail'),  # Ex: /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),  # Ex: /polls/5/results/
    path('<int:question_id>/vote/', views.results, name='vote'),  # Ex: /polls/5/vote/
]
