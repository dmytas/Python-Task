from typing import List
from datetime import date

from restaurant_service.models import Restaurant, Menu
from employee_service.models import Employee


class MenuService:
    @staticmethod
    def upload_menu(restaurant: Restaurant, date: date, items: List[str]):
        items_str = "\n".join(items)
        menu, created = Menu.objects.get_or_create(restaurant=restaurant, date=date, defaults={'items': items_str})
        if not created:
            menu.items = items_str
            menu.save()

    @staticmethod
    def create_employee(name: str, email: str):
        employee, created = Employee.objects.get_or_create(name=name, email=email)
        return employee

    @staticmethod
    def get_current_day_menu(restaurant: Restaurant) -> Menu:
        today = date.today()
        try:
            menu = Menu.objects.get(restaurant=restaurant, date=today)
            return menu
        except Menu.DoesNotExist:
            return None

    @staticmethod
    def get_results_for_current_day(restaurant: Restaurant) -> dict:
        menu = MenuService.get_current_day_menu(restaurant)
        if not menu:
            return {'status': 'error', 'message': 'No menu for today'}

        votes = menu.voting_set.all()
        up_votes = votes.filter(vote=True).count()
        down_votes = votes.filter(vote=False).count()

        return {
            'status': 'success',
            'up_votes': up_votes,
            'down_votes': down_votes
        }
