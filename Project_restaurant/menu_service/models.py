from django.db import models
from django.utils import timezone
from employee_service.models import Employee
from restaurant_service.models import Restaurant


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name


class Menu_of_day(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.ManyToManyField(Menu)

    def __str__(self):
        return f"{self.restaurant.name} - {self.date}"

    def get_votes(self):
        up_votes = self.voting_set.filter(vote=True).count()
        down_votes = self.voting_set.filter(vote=False).count()
        return {'up_votes': up_votes, 'down_votes': down_votes}


class Voting(models.Model):
    menu = models.ForeignKey(Menu_of_day, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    vote = models.BooleanField(default=False)
    app_version = models.CharField(max_length=10, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.employee.username} voted {self.vote} on {self.menu}"

    class Meta:
        unique_together = ['menu', 'employee']
        indexes = [
            models.Index(fields=['menu', 'employee']),
            models.Index(fields=['employee', 'vote']),
        ]
