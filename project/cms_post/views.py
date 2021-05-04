
from django.http import HttpResponse
from .models import Content, Comment
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.utils import timezone


@csrf_exempt
def logged_in(request):

    if request.user.is_authenticated:
        logged = "Logged in as " + request.user.username
    else:
        logged = "Not logged in. <a href='/login'>Login via login</a>"

    return HttpResponse(logged)


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect("/cms_post/")


@csrf_exempt
def login_view(request):
    return redirect("/login")


@csrf_exempt
def index(request):

    context = {"content": {}, "rootpage": True}
    return render(request, 'cms_post/content.html', context=context, status=200)


@csrf_exempt
def get_annotated(request, key):

    try:
        content = Content.objects.get(key=key)
        context = {"content": content, "rootpage": False}

    except Content.DoesNotExist:
        return render(request, 'cms_post/new.html', context={}, status=404)

    return render(request, 'cms_post/content.html', context=context, status=200)


@csrf_exempt
def edit(request, key):

    if request.method == "POST":
        action = request.POST['action']
        if action == "Send Content":
            value = request.POST['value']
            try:
                content = Content.objects.get(key=key)
                content.value = value

            except Content.DoesNotExist:
                content = Content(key=key, value=value)

            content.save()

    try:
        content = Content.objects.get(key=key)
        context = {"content": content, "rootpage": False}

    except Content.DoesNotExist:
        return render(request, 'cms_post/new.html', context={}, status=404)

    return render(request, 'cms_post/content.html', context=context, status=200)


@csrf_exempt
def get_content(request, key):

    if request.method == "PUT":
        value = request.body.decode('utf-8')

    if request.method == "POST":
        action = request.POST['action']

        if action == "Send Content":
            value = request.POST['value']
            try:
                content = Content.objects.get(key=key)
                content.value = value
                content.save()
            except Content.DoesNotExist:
                content = Content(key=key, value=value)
                content.save()

        elif action == "Send Comment":
            content = Content.objects.get(key=key)
            title = request.POST['title']
            body = request.POST['body']
            date = timezone.now()
            q = Comment(content=content, title=title, body=body, date=date)
            q.save()

    try:
        content = Content.objects.get(key=key)
        response = "Key '" + key + "' value is: " \
                   + content.value + "<br>"
        status = 200

        comments = content.comment_set.all()
        for comment in comments:
            response += "<p><b>Title</b>: " + comment.title + "<br><b>Body: </b>" + comment.body + "<br><b>Date: </b>" + str(comment.date)

        if request.user.is_authenticated:
            response += form + form2 + "Logged in as " + request.user.username
        else:
            response += "Not logged in. <a href='/login'>Login</a>"

    except Content.DoesNotExist:
        response = 'There is no content for key: ' + key + '<br>'
        if request.user.is_authenticated:
            response = "Logged in as " + request.user.username
        else:
            response = "<br>Not logged in. <a href='/login'>Login</a>"
        status = 404

    return HttpResponse(response, status=status)
