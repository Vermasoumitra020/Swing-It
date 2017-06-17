from django.contrib import admin
from .models import SignUp, Status
from .forms import SignUpForm

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "update"]
    form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Status)