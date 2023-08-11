from django import forms
from .tasks import send_review_email_task


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, label='Firstname',
                           min_length=2, widget=forms.TextInput(
                               {"class": "form-control mb-3",
                                   "placeholder": "First Name", "id": "form-firstname"}
                           ))
    email = forms.EmailField(max_length=100, label='first_name',
                             min_length=2, widget=forms.TextInput(
                                 {"class": "form-control mb-3",
                                  "placeholder": "Email", "id": "form-email"}
                             ))
    review = forms.CharField(max_length=100, label='Review',
                             min_length=2, widget=forms.Textarea(
                                 {"class": "form-control",
                                  "rows": '5'}
                             ))

    def send_email(self):
        # send taks to celery to run
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'],
            self.cleaned_data['review']
        )
