from django import forms
from .models import Project, Tag
from django_ckeditor_5.widgets import CKEditor5Widget

class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["content"].required = False

    class Meta:
        models = Project
        fields = "__all__"
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}
            )
        }

class TagForm(forms.ModelForm):

    class Meta:
        models = Tag
        fields = "__all__"
