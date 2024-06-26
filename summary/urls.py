from django.urls import path
from . import views

app_name = "summary"

urlpatterns = [
    # chapter에 대한 URL 패턴
    path('summary_detail/<str:lecture_name>/<str:chapter_name>/', views.summary_detail_view, name='summary_detail'),  # summary_detail
    path('upload_file_summary/<str:lecture_name>/<str:chapter_name>/', views.upload_file_summary, name='upload_file_summary'),
    path('delete_file_summary/<int:file_id>/', views.delete_file_summary, name='delete_file_summary'),
    path('stt_view/<int:file_id>/', views.stt_view, name='stt_view'),
    path('show_summary_view/<int:file_id>/', views.show_summary_view, name='show_summary_view'),
    
]

