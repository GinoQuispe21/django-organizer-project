from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.SmallIntegerField()
    teacher = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "course"
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self) -> str:
        return self.name
    
    # relacion de one to many con usuasrios
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    

class Task(models.Model):

    title = models.CharField(max_length = 200)
    description = models.TextField()
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    # configuracion para el nombre de la base de datos y como se llame en el panel administrativo
    class Meta:
        db_table = "task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self) -> str:
        return self.title
    
    # referencia a cursos de uno a muhcos/ one to many
    course = models.ForeignKey(Course, on_delete = models.CASCADE)