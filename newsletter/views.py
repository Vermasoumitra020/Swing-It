from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,render_to_response
from .forms import SignUpForm, ContactForm, StatusForm
from django.core.mail import send_mail
from django.conf import settings
from newsletter.models import SignUp, Status
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy


# Create your views here.

def home(request):

    my_title = "Welcome.."
    my_form = SignUpForm(request.POST, request.FILES or None)
    all_items = SignUp.objects.all()
    context = {
            'template_title': my_title,
            'my_form': my_form,
            'all_items': all_items,
    }

    if my_form.is_valid():
        all_items.delete()
        j = my_form.save(commit=False)
        j.save()
        context = {
                'template_title': 'Thank you',
        }
    return render(request, 'home.html', context)

def Contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')

        subject = 'This is the form email'
        from_email =  settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)

        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

    context = {
        'form': form,
        'template_title': 'Contact Us'
    }

    return render(request, 'contact.html', context)


def Profile(request):
    user = User.objects.all()
    all_items = SignUp.objects.all()
    status_items = Status.objects.all()
    form = StatusForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('')
    return render(request, 'profile.html', {'all_items': all_items, 'status_items':status_items, 'form': form,})

def wall(request, user_id):
    user = User.objects.all()
    all_items = SignUp.objects.all()
    person = get_object_or_404(user , id = user_id)
    settings.LOGIN_REDIRECT_URL = '/profile/'+str(user_id)+'/'
    return render(request, 'wall.html', {'all_items': all_items, 'user_id': user_id})



def ProfileUpdateView(request, pk):
    my_title = "Welcome.."
    server = get_object_or_404(SignUp, pk=pk)
    all_items = SignUp.objects.all()
    my_form = SignUpForm(request.POST or None, request.FILES or None, instance=server)
    context = {
        'template_title': my_title,
        'my_form': my_form,
        'all_items': all_items,
    }
    if my_form.is_valid():
        my_form.save()

        return redirect('profile')
    return render(request, 'home.html', context)

def ProfileDeleteView(request, pk):
    server = get_object_or_404(Status, pk=pk)
    if request.method=='GET':
        server.delete()
        return redirect('profile')
    return render(request, 'profile.html', {'object':server})