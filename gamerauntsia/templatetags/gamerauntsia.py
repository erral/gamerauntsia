from django import template
from gamerauntsia.registration.forms import RegistrationForm

register = template.Library()

def regform(request):
    forma=RegistrationForm()
    return forma.as_p()

register.simple_tag(regform)
    
