from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
   
    dest1=Destination()
    dest1.name="Aakash Raja"
    dest1.desc="President"
    dest1.img="destination_1.jpg"
    dest1.price=700

    dest2=Destination()
    dest2.name="Saran"
    dest2.desc="Treasurer"
    dest2.img="destination_2.jpg"
    dest2.price=600

    dest3=Destination()
    dest3.name="Saran"
    dest3.desc="Treasurer"
    dest3.img="destination_2.jpg"
    dest3.price=600

    dest4=Destination()
    dest4.name="Saran"
    dest4.desc="Treasurer"
    dest4.img="destination_2.jpg"
    dest4.price=600

    dest5=Destination()
    dest5.name="Saran"
    dest2.desc="Treasurer"
    dest5.img="destination_2.jpg"
    dest5.price=600

    dest6=Destination()
    dest6.name="Saran"
    dest6.desc="Treasurer"
    dest6.img="destination_2.jpg"
    dest6.price=600

    dest7=Destination()
    dest7.name="Saran"
    dest7.desc="Treasurer"
    dest7.img="destination_2.jpg"
    dest7.price=600

    dest8=Destination()
    dest8.name="Saran"
    dest8.desc="Treasurer"
    dest8.img="destination_2.jpg"
    dest8.price=600

    dest9=Destination()
    dest9.name="Saran"
    dest9.desc="Treasurer"
    dest9.img="vishnu.jpg"
    dest9.price=600

    dest10=Destination()
    dest10.name="Saran"
    dest10.desc="Treasurer"
    dest10.img="destination_2.jpg"
    dest10.price=600

    dest11=Destination()
    dest11.name="Saran"
    dest11.desc="Treasurer"
    dest11.img="destination_2.jpg"
    dest11.price=600

    dest12=Destination()
    dest12.name="Saran"
    dest12.desc="Treasurer"
    dest12.img="destination_2.jpg"
    dest12.price=600

    dest13=Destination()
    dest13.name="Saran"
    dest13.desc="Treasurer"
    dest13.img="destination_2.jpg"
    dest13.price=600

    dest14=Destination()
    dest14.name="Saran"
    dest14.desc="Treasurer"
    dest14.img="destination_2.jpg"
    dest14.price=600

    dest15=Destination()
    dest15.name="Saran"
    dest15.desc="Treasurer"
    dest15.img="destination_2.jpg"
    dest15.price=600
    
    dests=[dest1,dest2,dest3,dest4,dest5,dest6,dest7,dest8,dest9,dest10,dest11,dest12,dest13,dest14,dest15]
    ache1=Achievements()
    ache1.name="Pragyan"
    ache1.desc="won the gold in sangam"
    aches=[ache1]

    return render(request, "index.html",{'dests': dests,'aches':aches})
