from django.db import models
from django.db.models import Manager

class FoodManager(Manager):
    pass

class Food(models.Model):
    name = models.CharField(max_length=100, default='Default Food Name')  
    food_id = models.IntegerField(default=0)  
    meal_type = models.CharField(max_length=100)  # Accept any value for meal type

    objects = FoodManager()  # Add this line to define the objects attribute

    @classmethod
    def save_food(cls, meal_type, food_name, food_id):
        existing_food = cls.objects.filter(meal_type=meal_type).first()
        if existing_food:
            # Update existing food entry
            existing_food.name = food_name
            existing_food.food_id = food_id
            existing_food.save()
        else:
            # Create a new food entry
            cls.objects.create(meal_type=meal_type, name=food_name, food_id=food_id)

    def __str__(self):
        return f'Food for {self.meal_type}: {self.name}'



class Contact(models.Model):
    s_no = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=50)
    Message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.Name
