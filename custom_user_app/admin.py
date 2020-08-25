from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from custom_user_app.models import CustomUser
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'homepage', 'age', 'is_superuser',)
    list_filter = ('is_superuser',)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Personal info', {'fields': ('homepage', 'age',)}),
    )

    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, UserAdmin)
