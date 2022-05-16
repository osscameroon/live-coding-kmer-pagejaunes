from django import forms
from django.forms import ValidationError
from core.models import Business
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout


class BusinessForm(forms.ModelForm):
    email = forms.EmailField(label="Your email")

    class Meta:
        model = Business
        fields = ['name', 'city', 'quarter', 'sector', 'email', 'phone_number', 'image', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            'name',
            'city',
            'quarter',
            'sector',
            'email',
            'phone_number',
            'image',
            'tags',
            ButtonHolder(Submit('submit', 'Submit'))
        )

        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})

    def clean_phone_number(self):
        phone_number = self.data['phone_number']
        if len(phone_number) != 9 or not phone_number.startswith('6'):
            raise ValidationError('Wrong phone number format')
        return phone_number