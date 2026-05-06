from urllib import request

from django.shortcuts import render, redirect
import telebot
bot = telebot.TeleBot('8316968855:AAHevwk_HxRYZB4gf0rO6fGzyc-UTfA3mU0')
group_id = -5234941244

def home(request):
    return render(request, 'home.html')




def try_free_lesson(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        text = (f'Новый клиент! \n\n'
                f'Имя: {name}\n'
                f'Номер телефона: {number}\n')
        bot.send_message(group_id, text)
    return redirect('/')


def connect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        gadjet = request.POST.get('gadjet')
        text = (f'Новый клиент! \n\n'
                f'Имя: {name}\n'
                f'Номер телефона: {number}\n'
                f'Инструмент: {gadjet}\n')
        bot.send_message(group_id, text)
    return redirect('/')


# Create your views here.
