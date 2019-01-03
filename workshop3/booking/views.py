from datetime import date, timedelta, datetime
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.dateparse import parse_date

from .forms import RoomForm,BookingForm

# Create your views here.
from django.views import View


from .models import Room, Booking


class newRoom(View):
    def get(self,request):
        form=RoomForm()
        return render(request, 'new_room.html', {'form': form})

    def post(self,request):
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=True)
            return redirect(reverse('allRooms'))


class modifyRoom(View):

    def get(self,request,id):
        room = get_object_or_404(Room, id=id)
        form=RoomForm(instance=room)
        return render(request, 'new_room.html', {'form': form})

    def post(self,request,id):
        room = get_object_or_404(Room, id=id)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room=form.save(commit=True)
            return redirect('allRooms')


class deleteRoom(View):
    def get(self,request,id):
        room=get_object_or_404(Room,id=id)
        room.delete()
        return redirect('allRooms')

class room(View):
    def get(self,request,id):
        today=date.today()
        r=Room.objects.get(id=id)
        booked_dates=Booking.objects.filter(room_id=id).filter(booking_date__gte=today)
        return render(request, "room_details.html", locals())


class allRooms(View):
    def get(self,request):
        today=date.today()
        #flat=True let save only the list of values, in this case, only id's of rooms
        booked_today=Booking.objects.filter(booking_date=today).values_list('room_id',flat=True)
        rooms_list=Room.objects.all().order_by('id')
        return render(request,"rooms.html",locals())

class allBookings(View):
    def get(self,request):
        bookings_list=Booking.objects.all().order_by('id')
        return render(request,"bookings.html",locals())

class newBooking(View):
    def get(self,request,id=0):
        today=date.today()
        form = BookingForm(initial={'room':id})
        booked_dates = Booking.objects.filter(room_id=id).filter(booking_date__gte=today)
        #return render(request, 'room_booking.html', {'form': form})
        return render(request, 'room_booking.html', locals())

    def post(self,request,id=0):
        today = date.today()
        form = BookingForm(request.POST)
        booked_dates = Booking.objects.filter(room_id=id).filter(booking_date__gte=today)
        if form.is_valid():
            booking = form.save(commit=False)
            check=Booking.objects.filter(Q(booking_date=booking.booking_date) & Q(room=booking.room))
            if booking.booking_date<today:
                messages.error(request, "Date is from the past, please correct it.")
                return render(request, 'room_booking.html', locals())
            elif check:
                messages.error(request, "This room is already booked for that date. Please choose another one.")
                return render(request, 'room_booking.html', locals())
            else:
                booking.save()
                return redirect('allBookings')

class modifyBooking(View):

    def get(self,request,id,room):
        today=date.today()
        booking = get_object_or_404(Booking, id=id)
        booked_dates = Booking.objects.filter(room_id=room).filter(booking_date__gte=today)
        form=BookingForm(instance=booking)
        return render(request, 'room_booking.html', locals())

    def post(self,request,id,room=0):
        booking = get_object_or_404(Booking, id=id)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking=form.save(commit=True)
            return redirect('allBookings')


class deleteBooking(View):
    def get(self,request,id):
        booking=get_object_or_404(Booking,id=id)
        booking.delete()
        return redirect('allBookings')


class search(View):
    def get(self,request):
        form = RoomForm()
        form_b=BookingForm()
        return render(request, 'search.html', locals())
    def post(self,request):
        form = RoomForm(request.POST)
        form_b = BookingForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            date_0 = str(request.POST.get('booking_date'))
            date=datetime.strptime(date_0, "%Y-%m-%d").date()
            #date = parse_date(date_str)
            name=request.POST.get("name")
            volume=request.POST.get("volume")
            if 'projector_availability' in request.POST:
                projector_availability=True
            else:
                projector_availability=False

            try:
                r = Room.objects.get(name=name)
            except ObjectDoesNotExist:
                messages.error(request, "There is no room with such name.")
                return render(request, 'search.html', locals())
            rooms_list = Room.objects.all().filter(Q(name=name) & Q(volume=volume) & Q(projector_availability=projector_availability))
            booked_for_given_date=Booking.objects.filter(booking_date=date).values_list('room_id',flat=True)
            if r.id in booked_for_given_date:
                messages.error(request, "No available rooms for given criteria")
                return render(request, 'search.html', locals())
            else:
                return render(request, 'search.html', locals())
                #return HttpResponse("bforgd={}".format(booked_for_given_date))