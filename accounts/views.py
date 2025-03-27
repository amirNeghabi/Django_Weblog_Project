from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SingUpView(generic.CreateView):
    form_class = UserCreationForm  # نام صحیح: form_class
    template_name = "registration/singup.html"
    success_url = reverse_lazy('login')