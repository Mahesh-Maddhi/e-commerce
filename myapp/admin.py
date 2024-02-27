from django.contrib import admin
from myapp.models import SignedUser, Contact

# Register your models here.
admin.site.register(SignedUser)

admin.site.register(Contact)