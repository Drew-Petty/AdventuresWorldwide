from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth.models import *
from .models import *
from .filters import *


def root(request):
    return redirect('/accounts/login')
def main(request):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    trip_list = Trip.objects.all()
    myFilter = TripFilter(request.GET, queryset=trip_list)
    trip_list = myFilter.qs
    paginator = Paginator(trip_list,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj':page_obj,
        'myFilter':myFilter,
    }
    return render(request, 'main.html',context)
def new_guide(request):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    context={
        'form': PictureForm()
    }
    return render(request, 'new_guide.html', context)
def create_guide(request):
    form = PictureForm(request.POST,request.FILES)
    user = User.objects.get(id=request.user.id)
    if form.is_valid():
        picture=form.cleaned_data.get('picture')
        guide = Guide.objects.create(
            user=user,
            type='guide',
            about_me=request.POST['about_me'],
        )
        if picture != None:
            guide.picture = picture
            guide.save()
    return redirect('/profile')
def profile(request):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    guide=Guide.objects.get(id=request.user.guide.id)
    trip_list = Trip.objects.filter(guide=guide)
    paginator = Paginator(trip_list,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'guide':guide,
        'page_obj':page_obj,
    }
    return render(request,'guide.html',context)
def view_guide(request, guide_id):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    guide=Guide.objects.get(id=guide_id)
    trip_list = Trip.objects.filter(guide=guide)
    paginator = Paginator(trip_list,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'guide':guide,
        'page_obj':page_obj,
    }
    return render(request,'guide.html',context)



def edit_profile(request):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    context ={
        'pictureForm':PictureForm(),
    }
    return render(request, 'edit_guide.html', context )
def update_profile_picture(request):
    form = PictureForm(request.POST,request.FILES)
    guide = Guide.objects.get(id=request.user.guide.id)
    if form.is_valid():
        if guide.picture.url != '/img/default_guide.png':
            guide.picture.delete()
        guide.picture = form.cleaned_data.get('picture')
        guide.save()
    return redirect('/edit_profile')
def update_guide(request):
    guide = Guide.objects.get(id=request.user.guide.id)
    guide.about_me = request.POST['about_me']
    guide.save()
    return redirect('/profile')
def new_trip(request):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    context={
        'form': TripForm()
    }
    return render(request, 'new_trip.html', context)
def create_trip(request):
    form = TripForm(request.POST, request.FILES)
    guide = Guide.objects.get(id=request.user.guide.id)
    if form.is_valid():
        picture = form.cleaned_data.get('picture')
        print(form.cleaned_data.get('categories'))
        trip = Trip.objects.create(
            name=request.POST['name'],
            duration=request.POST['duration'],
            cost=request.POST['cost'],
            capacity=request.POST['capacity'],
            about=request.POST['about'],
            guide=guide,
        )
        trip.category.set(form.cleaned_data.get('categories'))
        if picture != None:
            trip.picture = picture
        trip.save()
    return redirect('/profile')
def view_trip(request,trip_id):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    context ={
        'trip': Trip.objects.get(id=trip_id)
    }
    return render(request,'trip.html',context)
def edit_trip(request,trip_id):
    if request.user.is_authenticated == False:
        return redirect('/accounts/login')
    trip = Trip.objects.get(id=trip_id)
    context={
        'trip': trip,
        'pictureForm':PictureForm(),
        'tripEditForm':TripEditForm(instance=trip),
    }
    return render(request,'edit_trip.html',context)
def update_trip_picture(request, trip_id):
    form = PictureForm(request.POST, request.FILES)
    trip = Trip.objects.get(id=trip_id)
    if form.is_valid():
        if trip.picture.url != '/img/default_trip.jfif':
            trip.picture.delete()
        trip.picture = form.cleaned_data.get('picture')
        trip.save()
    return redirect('/edit_trip/'+str(trip_id))
def update_trip(request,trip_id):
    trip = Trip.objects.get(id=trip_id)
    form = TripEditForm(request.POST, instance=trip)
    if form.is_valid():
        form.save()
        trip.about = request.POST['about']
        trip.save()
    return redirect('/view_trip/'+str(trip_id))
def delete_trip(request,trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.delete()
    return redirect('/profile')
