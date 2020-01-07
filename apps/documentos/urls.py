from django.urls import path
from .views import DocumentoDelete, DocumentoNovo

urlpatterns = [
    # path('delete/<int:pk>/', DocumentoDelete.as_view(), name='delete_documento'),
    path('novo/<int:funcionario_id>/', DocumentoNovo.as_view(), name='create_documento'),

]