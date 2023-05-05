from django.shortcuts import render, redirect
from .models import Menu, Voting
from .forms import VoteForm


def menu(request):
    week = {
        'Monday': ['Spaghetti Bolognese', 'Vegetable Curry', 'Fish and Chips'],
        'Tuesday': ['Steak and Fries', 'Lamb Rogan Josh', 'Mushroom Risotto'],
        'Wednesday': ['Chicken Fajitas', 'Beef and Broccoli Stir Fry', 'Salmon and Asparagus'],
        'Thursday': ['Meatball Sub', 'Tofu and Veggie Skewers', 'Fried Rice'],
        'Friday': ['Pesto Pasta', 'Pork Chops and Apple Sauce', 'Grilled Cheese'],
        'Saturday': ['Full English Breakfast', 'Cobb Salad', 'Prawn Cocktail'],
        'Sunday': ['Roast Beef and Yorkshire Pudding', 'Vegetable Lasagne', 'Tandoori Chicken']
    }

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            selected_day = form.cleaned_data['day']
            selected_menu = form.cleaned_data['menu']

            menu_item = Menu.objects.get(day=selected_day, name=selected_menu)

            vote = Voting(menu_item=menu_item, employee=request.user)
            vote.save()

            message = f"Your vote for {selected_menu} on {selected_day} has been recorded. Thank you for voting!"
            return render(request, 'menu.html', {'week': week, 'message': message})
    else:
        form = VoteForm()

    return render(request, 'menu.html', {'week': week, 'form': form})
