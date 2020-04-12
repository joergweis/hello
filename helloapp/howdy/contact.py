# howdy\contact.py

from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False,label='Your e-mail address')
    subject = forms.CharField(max_length=100, label='Subject') # if label is ommited name is taken as label
    message = forms.CharField(widget=forms.Textarea, label='Message')

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})
