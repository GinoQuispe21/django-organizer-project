from django.urls import path
from . import views

# url_base = http://127.0.0.1:8000/

urlpatterns = [
    # Ejemplos de prueba
    path('hello_world', views.hello_world), # http://127.0.0.1:8000/hello_world
    path('about', views.about), # http://127.0.0.1:8000/about
    path('json_task', views.json_tasks ), # http://127.0.0.1:8000/json_task

    # tareas
    path('', views.index, name='index'), # url_base = http://127.0.0.1:8000/
    path('update_task/<int:task_id>', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    # cursos
    path('courses', views.courses, name='courses')
]

# request params : parametros de las consultas https
#http://127.0.0.1:8000/update_task/int:id