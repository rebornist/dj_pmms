from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from users import models


class HomeView(View):
    """ HomeView Definition """

    def get(self, request):
        if request.session.get('_auth_user_id'):
            id = request.session.get('_auth_user_id')
            user = models.User.objects.get(id=id)
            return render(request, "home/index.html", {"user": user})
        return redirect(reverse("users:login"))
