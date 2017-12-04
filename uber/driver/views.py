from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.views import logout
from django.db import transaction
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    title='Welcome | uber-pool'

    return render(request,'index.html',{'title':title})

