from django import forms
from .models import Project, Tag, Contact
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


class ContactForm(forms.ModelForm):
   
   class Meta:
       model = Contact
       fields = ('full_name', 'email', 'subject', 'message')

       widgets = {
           'full_name': forms.TextInput(
               attrs={
                   'class': 'form-control',
                   'required': True,
                   'autocomplete': 'off',
                   'placeholder': 'Masukkan nama lengkap'
               }
           ),
            'email': forms.TextInput(
               attrs={
                   'class': 'form-control',
                   'type': 'email',
                   'required': True,
                   'autocomplete': 'off',
                   'placeholder': 'Masukkan alamat email'
               }
           ),
            'subject': forms.Textarea(
               attrs={
                   'class': 'form-control',
                   'required': True,
                   'autocomplete': 'off',
                   'placeholder': 'Masukkan subjek anda',
                   'rows': 2
               }
           ),
            'message': forms.Textarea(
               attrs={
                   'class': 'form-control',
                   'required': True,
                   'autocomplete': 'off',
                   'placeholder': 'Masukkan pesan anda',
                   'rows': 4
               }
           ),
       }