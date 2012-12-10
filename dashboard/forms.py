from django import forms

from dashboard.models import Configuration

choices = ( (1, 'Yes'),
            (0, 'No'),
          )

class ConfigurationForm(forms.ModelForm):
    show_acknowledged = forms.TypedChoiceField(
                                choices=choices, widget=forms.RadioSelect, coerce=int
                        )

    class Meta:
        model = Configuration
        widgets = {
                'zenoss_password': forms.PasswordInput(),
        }
