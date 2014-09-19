from django import template
from registration.forms import RegistrationFormUniqueEmail

register = template.Library()

def regform(request):
    forma=RegistrationFormUniqueEmail()
    #forma.fields['username'].help_text='periko'
    return forma.as_p()

register.simple_tag(regform)
    