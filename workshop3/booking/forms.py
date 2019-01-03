from django import forms
from django.forms import SelectDateWidget

from .models import Room,Booking
from django.contrib.admin.widgets import AdminDateWidget

class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=('name','volume','projector_availability')



class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=('booking_date','comment','room')
        YEARS=[x for x in range(2018,2030)]
        #booking_date=forms.DateField(label='Date widget',widget=forms.SelectDateWidget(empty_label="Nothing"))
        widgets = {
            'booking_date': SelectDateWidget(years=YEARS),
        }



