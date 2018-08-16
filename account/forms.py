from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from django.conf import settings
# from account.models import Registration
from .models import OrderMeal

from django import forms

from crispy_forms.helper import FormHelper


class BaseHorizontalFormMixin(forms.Form):
    """Customized form class that better displays crispy forms"""

    def __init__(self, *args, **kwargs):
        """initializes form with desired style configuration"""
        super(BaseHorizontalFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.form_tag = False


class BaseFormMixin(forms.Form):
    """Customized form class that better displays crispy forms"""

    def __init__(self, *args, **kwargs):
        """initializes form with desired style configuration"""
        super(BaseFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form'
        self.helper.form_tag = False


class BaseHorizontalForm(forms.ModelForm, BaseHorizontalFormMixin):
    """Customized form class that better displays crispy forms"""


class BaseForm(forms.ModelForm, BaseFormMixin):
    """Customized form class that better displays crispy forms"""





class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'input'}))
    # address = forms.CharField(label="Repeat password", widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True}))
    # Pin = forms.CharField(label="Repeat password", widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True}),
            # 'address': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            # 'Pin': forms.TextInput(attrs={'class': 'input', 'autofocus': True})
        }

    # Validating password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))


class OrderMealForm(forms.ModelForm):
    name = forms.TextInput(attrs={'class': 'input', 'autofocus': True})
    # delivery_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = OrderMeal
        fields = ('name', 'mobile', 'email', 'thali', 'delivery_date', 'message',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_errors = False
        super(OrderMealForm, self).__init__(*args, **kwargs)