import string
from random import choice

from django.shortcuts import render


def home(request):
    return render(request, "generator/home.html")


def about(request):
    return render(request, "generator/about.html")


def password(request):
    chars = list(string.ascii_lowercase)
    chars_upper = list(string.ascii_uppercase)
    chars_num = list(string.digits)
    chars_special = list(string.punctuation)
    if request.GET.get("uppercase"):
        chars.extend(chars_upper)
    if request.GET.get("special"):
        chars.extend(chars_special)
    if request.GET.get("numbers"):
        chars.extend(chars_num)
    length = int(request.GET.get("length", 12))
    passwd = ""
    for i in range(length):
        passwd += choice(chars)
    return render(request, "generator/password.html", {"password": f"> {passwd} <"})
