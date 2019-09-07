from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import User, Person


# Create your views here.


def index(request):
    users = User.objects.all()
    # User.objects.filter(username="delzar")
    # User.objects.get(id=1)
    # usernames = ', '.join([user.username for user in users])
    return render(request, 'login/index.html', {'users': users})


def detail(request, username):
    print(username)
    user = get_object_or_404(User, username=username)
    return render(request, 'login/detail.html', {'user': user})
    # try:
    #    user = User.objects.get(pk=user_id)
    #    return render('login/detail.html', {'user': user})
    # except User.DoesNotExist:
    #    raise Http404()
