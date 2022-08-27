import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_number(request, number):
    answer = f"""
    <html>
        <body>
        <p>The answer is {number}!</p>
        </body>
    </html>
    """

    return HttpResponse(answer)


def pick_number(request, max_number):
    wylosowana_liczba = random.randint(0, int(max_number))
    result = f"Użytkownik podał wartość {max_number}. Wylosowano liczbę: {wylosowana_liczba}."
    return HttpResponse(result)