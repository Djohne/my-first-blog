from django.shortcuts import render
from .forms import SubscriberForm


def goods(request):
    name = "Andrew"
    current_day "20.05.2017"
    form = SubscriberForm(request.POST or None)

    return render(request,'blog/post_list.html')

# Create your views here.
