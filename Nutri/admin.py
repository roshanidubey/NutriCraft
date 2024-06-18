from django.contrib import admin
from .models import Food  # Import the Food model from your application's models
from .models import Contact 


admin.site.register(Food)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'Name', 'Email', 'Subject', 'Message')