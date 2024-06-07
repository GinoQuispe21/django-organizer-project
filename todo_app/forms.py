from django import forms
from .models import Task, Course

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__' # que django considere todos los campos

class CreateTaskForm(forms.Form):

    title = forms.CharField(
        label = "Titulo de la tarea",
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control-text-input',
                'placeholder': 'Titulo de tarea'
            }
        )
    )

    description = forms.CharField(
        label = "Descripcion",
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control-text-input',
                'placeholder': 'Descripcion de tarea'
            }
        )
    )

    course = forms.ModelChoiceField(
        queryset = Course.objects.all(),
        empty_label = "Selecciona un curso",
        widget = forms.Select(
            attrs = {
                'class': 'form-control-text-input',
                'placeholder': 'Descripcion de tarea'
            }
        )
    )


class UpdateTaskForm(forms.Form):

    title = forms.CharField(
        label = "Titulo de la tarea",
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control-text-input',
                'placeholder': 'Titulo de tarea'
            }
        )
    )
    description = forms.CharField(
        label = "Descripcion",
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control-text-input',
                'placeholder': 'Descripcion de tarea'
            }
        )
    )
    course = forms.ModelChoiceField(
        label = 'Curso',
        queryset = Course.objects.all(),
        empty_label = "Selecciona un curso",
        widget = forms.Select(
            attrs = {
                'class': 'form-control-text-input',
            }
        )
    )
    completed = forms.BooleanField(
        label = "Completado",
        required = False,
        widget = forms.CheckboxInput(
            attrs = {
                'class': 'form-control-checkbox'
            }
        )
    )

class CreateCoursekForm(forms.Form):

    name = forms.CharField(
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Nombre del Curso',
                'class': 'form-control-text-input',
            }
        )
    )

    description = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control-text-input',
                'placeholder': 'Descripcion de tarea'
            }
        )
    )

    credits = forms.CharField(
        max_length = 200,
        widget = forms.NumberInput(
            attrs = {
                'placeholder': 'Creditos del Curso',
                'class': 'form-control-text-input',
            }
        )
    )

    teacher = forms.CharField(
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Nombre del Curso',
                'class': 'form-control-text-input',
            }
        )
    )