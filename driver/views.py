from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from uber import settings
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    title = 'Welcome | uber-pool'
    instance = request.user
    if request.method == 'POST':
        form = DriverRiderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')

            return redirect(ride)
        else:
            messages.error(

                request, 'Error')

    return render(request, 'index.html', {'title': title})


@login_required(login_url='/accounts/login/')
@transaction.atomic
def Driver_Prof(request):
    instance = request.user
    if request.method == 'POST':
        form = RiderForm(request.POST, request.FILES,
                         instance=request.user)
        user_profile = RiderProfileForm(
            request.POST, request.FILES, instance=request.user.rider_profile)
        if form.is_valid() and user_profile.is_valid():
            form.save()
            user_profile.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(ride)
        else:
            messages.error(
                request, 'Error')
    else:
        form = RiderForm(instance=request.user)
        user_profile = RiderProfileForm(instance=request.user.rider_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})

    return render(request, 'driver/profile_edit.html', {'form': form, 'driver_profile': driver_pro})


@login_required(login_url='/accounts/login/')
def profile_driver(request):
    current_user = request.user
    profile = Driver.objects.filter(user=current_user).all()

    return render(request, 'driver/profile.html', {"profile": profile})


@login_required(login_url='/accounts/login/')
@transaction.atomic
def edituserprofile(request):
    instance = request.user
    if request.method == 'POST':

        form = RiderForm(request.POST, request.FILES, instance=request.user)
        user_profile = RiderForm(
            request.POST, request.FILES, instance=request.user.rider_profile)
        if form.is_valid() and user_profile.is_valid():
            form.save()
            user_profile.save()
            messages.success(request, 'Profile successfully updated')
            return render(request, 'index.html')
        else:
            messages.error(
                request, 'Error while updating profile,,, try again')
    else:
        form = RiderForm(instance=request.user)
        user_profile = RiderForm(instance=request.user.rider_profile)

    return render(request, 'rider/profile_edit.html', {'form': form, 'user_profile': user_profile})


@login_required(login_url='/accounts/login/')
def user_profile(request):

    current_user = request.user

    profile = Rider.objects.filter(user=current_user).all()

    return render(request, "rider/profile.html", {"profile": profile})


@csrf_exempt
def ajax_selection(request):

    current_user = request.user.id
    
    length_list=Driver_Or_Rider.objects.get(user_id=current_user)
    print(length_list.user_id)
    print(current_user)
    if length_list.user_id!=current_user :
        if request.POST.get('Driver') != None:

            '''
            creates a driver  instance once you click on the driver button Ajax
            '''
            Driver = request.POST.get('Driver')
            driver_rider_instance = Driver_Or_Rider.objects.create(
                user_id=current_user, selection=int(Driver))
            print(driver_rider_instance)

            data = {'success': 'You have been successfully Driver'}

            return JsonResponse(data)

        elif request.POST.get('Rider') != None:

            '''
            creates a Rider  instance once you click on the rider button Ajax
            '''

            rider_holder = request.POST.get('Rider')
            rider_instance = Driver_Or_Rider.objects.create(
                user_id=current_user, selection=int(rider_holder))
            print(rider_instance)

            data = {'success': 'You have been successfully Rider'}
            return JsonResponse(data)
        else:
            return JsonResponse('error occured')
    else:
         return HttpResponse("it didnt work")