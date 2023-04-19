from django.contrib import admin

# Register your models here.
from core.models import Car, Contact, Testimonial, Route,Section_Counter

admin.site.register(Car)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Route)
admin.site.register(Section_Counter)
