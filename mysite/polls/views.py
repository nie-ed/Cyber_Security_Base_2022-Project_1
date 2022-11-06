from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import NewUsers, Texts
from django.utils import timezone
from datetime import timedelta



#FIX Identification and Authentication Failures:

#import functools
#from django.conf import settings
#from django.core.exceptions import (
#    FieldDoesNotExist, ImproperlyConfigured, ValidationError,
#)
#from django.utils.module_loading import import_string
#from django.utils.translation import gettext as _, ngettext
#


#FIX CSRF protection:

#from django.views.decorators.csrf import csrf_protect





def index(request):
    user = NewUsers.objects.get(username=request.POST.get('username'))
    return HttpResponseRedirect(reverse('polls:detail', args=(user.id,)))

#FIX Broken Access Control:

#if (request.user):
#    return HttpResponseRedirect(reverse('polls:detail', args=(request.user.id,)))
#else:
#    return redirect('/')



def detail(request, user_id):
    user = NewUsers.objects.get(pk=user_id)

    try:
# FIX Insecure Desing:

#        texts = user.texts_set.filter(pub_date__lte=timezone.now())
#        texts = user.texts_set.filter(pub_date__gte=timezone.now() - timedelta(5))

        texts = Texts.objects.all()
        texts = texts.filter(pub_date__lte=timezone.now())
        texts = texts.filter(pub_date__gte=timezone.now() - timedelta(5))


    except (KeyError, Texts.DoesNotExist):
        return render(request, 'polls/detail.html', {'user': user})
    
    return render(request, 'polls/detail.html', {'user': user, 'texts': texts})


    



#FIX Broken Access Control:

#if (request.user):
#   return render(request, 'polls/detail.html', {'user': request.user})
#else:
#    return redirect('/')




def createnew(request):
    name = request.POST.get('username')
    pw = request.POST.get('password')
    new = NewUsers.objects.create(username = name, password = pw)
    new.save()
    return redirect('/')

#FIX Cryptographic Failures:

#new = User.objects.create_user(username=name, password=pw)





#FIX Identification and Authentication Failures:

#name = request.POST.get('username')
#pw = request.POST.get('password')
#validate_password(pw)
#new = User.objects.create_user(username=name, password=pw)


#@functools.lru_cache(maxsize=None)
#def get_default_password_validators():
#    return get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)


#def get_password_validators(validator_config):
#    validators = []
#    for validator in validator_config:
#        try:
#            klass = import_string(validator['NAME'])
#        except ImportError:
#            msg = "The module in NAME could not be imported: %s. Check your AUTH_PASSWORD_VALIDATORS setting."
#            raise ImproperlyConfigured(msg % validator['NAME'])
#        validators.append(klass(**validator.get('OPTIONS', {})))

#    return validators


#def validate_password(password, user=None, password_validators=None):
#    errors = []
#    if password_validators is None:
#        password_validators = get_default_password_validators()
#    for validator in password_validators:
#        try:
#            validator.validate(password, user)
#        except ValidationError as error:
#            errors.append(error)
#    if errors:
#        raise ValidationError(errors)


def add(request):
    user = NewUsers.objects.get(pk=request.POST.get('user_id'))
    text = request.POST.get('text')
    new = Texts.objects.create(owner = user, content = text, pub_date = timezone.now())
    new.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(user.id,)))

   