from django.shortcuts import render, redirect
import random
import datetime


def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    context = {
    'length' : len(request.session['activity']),
    'activity' : request.session['activity']
    }
    print context['length']
    print ('*'*50)
    return render(request, 'gold/index.html', context)

def reset(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')

def pan(request):
    change = random.randrange(10, 21)
    request.session['gold'] += change
    activity = 'Gained '+str(change)+' gold by panning, on '+timestring()
    request.session['activity'].insert(0,activity)
    return redirect('/')

def mine(request):
    change = random.randrange(1, 31)
    request.session['gold'] += change
    activity = 'Gained '+str(change)+' gold by mining, on '+timestring()
    request.session['activity'].insert(0,activity)
    return redirect('/')

def fight(request):
    if random.random() < 0.35:
        change = random.randrange(1, 1000)
        request.session['gold'] += change
        activity = 'Gained '+str(change)+' gold in a fight, on '+timestring()
    else:
        change = request.session['gold']
        request.session['gold'] = 0
        activity = 'Lost '+str(change)+' gold in a fight, on '+timestring()
    request.session['activity'].insert(0,activity)
    return redirect('/')

def gamble(request):
    change = random.randrange(-50, 51)
    if (change < 0) and (-change > request.session['gold']):
        activity = 'Lost all '+str(request.session['gold'])+' of your gold gambling, on '+timestring()
        request.session['gold'] = 0
    else:
        request.session['gold'] += change
        if change > 0:
            activity = 'Gained '+str(change)+' gold by gambling, on '+timestring()
        elif change < 0:
            change = -change
            activity = 'Lost '+str(change)+' gold by gambling, on '+timestring()
        else:
            activity = 'Broke even gambling, on '+timestring()
    request.session['activity'].insert(0,activity)
    return redirect('/')

def timestring():
    return datetime.datetime.now().strftime('%B %d, %Y at %X %p')
