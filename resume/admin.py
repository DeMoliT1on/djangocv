from django.contrib import admin
from .models import Person, Education, Experience, Project, Skill, Detail

# Register your models here.

admin.site.register(Person)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Detail)
admin.site.register(Project)

