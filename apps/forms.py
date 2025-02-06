from django.forms.models import ModelForm

from apps.models import Todo


class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        fields = "name",