from django import forms
from django.db import models


class SandboxForm(forms.Form):
    class Departments(models.TextChoices):
        ABUSE = "abuse"
        BILLING = "billing"
        FEEDBACK = "feedback"
        INFO = "info"

    subject = forms.CharField(max_length=128)
    department = forms.ChoiceField(choices=Departments.choices)
    description = forms.CharField(widget=forms.Textarea)
    is_urgent = forms.BooleanField()


# class SandboxForm(forms.Form):
#     like_website = forms.TypedChoiceField(
#         label="Do you like this website?",
#         choices=((1, "Yes"), (0, "No")),
#         coerce=lambda x: bool(int(x)),
#         widget=forms.RadioSelect,
#         initial='1',
#         required=True,
#     )
#
#     favorite_food = forms.CharField(
#         label="What is your favorite food?",
#         max_length=80,
#         required=True,
#     )
#
#     favorite_color = forms.CharField(
#         label="What is your favorite color?",
#         max_length=80,
#         required=True,
#     )
#
#     favorite_number = forms.IntegerField(
#         label="Favorite number",
#         required=False,
#     )
#
#     notes = forms.CharField(
#         label="Additional notes or feedback",
#         required=False,
#     )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('like_website', css_class="border-2"),
    #         'favorite_color',
    #         'favorite_food',
    #         'favorite_number',
    #         'notes',
    #     )
    #     self.helper.form_class = 'bg-gray-100 p-5'
    #     self.helper.label_class = 'bg-green-100'
    #     self.helper.field_class = 'bg-blue-100'
    #     self.helper.add_input(Submit('submit', 'Submit'))
