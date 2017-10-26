from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def index(request):
    # for i in range(0, 30):
    #     new_user = User(username=str(i), first_name=str(i), email=str(i) + '@gmail.com')
    #     new_user.save()

    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'user_list.html', { 'users': users })