from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero


# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary= request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))

    else:
        return render(request, 'superheroes/create.html')

def edit(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    if request.method == "POST":
        id = single_hero.id
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        update_hero = Superhero(id, name, alter_ego, primary_ability, secondary, catch_phrase)
        update_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/edit.html', context)

def delete (rerequest, hero_id):
    delete = Superhero.objects.get(pk=hero_id)
    delete.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))




