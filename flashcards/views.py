from django.shortcuts import (
        get_object_or_404,
        HttpResponseRedirect,
        render,
    )
from .forms import DeckForm
from .models import Deck

# Create your views here.
def home(request):
    '''
    Renders the FLASHCARD app home template
    '''
    qs = Deck.objects.order_by('-title').filter(is_active=True)
    context = {'decks': qs}
    return render(request, 'flashcards/home.html', context)

def createDeck(request):
    '''
    Renders the form to add new decks to the database
    '''
    if request.method == 'POST':
        # create the form isntance, and populate with data from the request
        form = DeckForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            #save the form, this saves the object to the database
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = DeckForm()
    context = {'form': form}
    return render(request, 'flashcards/createDeck.html', context)

def editDeck(request, deck_id):
    '''
    Renders the form to edit information about a deck object
    '''
    deck_obj = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        # create the form isntance, and populate with data from the request
        form = DeckForm(request.POST, instance=deck_obj)
        # check if the form is valid
        if form.is_valid():
            #save the form, this saves the object to the database
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = DeckForm(instance=deck_obj)
    context = {'form': form}
    return render(request, 'flashcards/createDeck.html', context)
