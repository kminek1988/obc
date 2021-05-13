from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
        class Meta:
            model = Contact
            exclude = ["owner"]

            fields = [
                'name',
                'imie',
                'nazwisko',
                'miasto',
                'profesja'
            ]
def __init__(self, request, *args, **kwargs):
    self.request = request
    super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = self.request.user
        if commit:
            instance.save()
            self.save_m2m()
            return instance