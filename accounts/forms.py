from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add consistent styling attrs to every visible input
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-input",
                "placeholder": field.label,
            })