from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import CustomUser, Followers
from twitteruser.forms import CustomUserChangeForm, CustomUserForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'display_name', 'email', 'is_staff', 'is_active',)
    list_filter = ('username', 'display_name', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {"fields": ('username', 'display_name', 'email', 'password')}),
            ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    add_fieldsets  = (
        (None, {
            "classes": ('wide',),
            "fields": ('username', 'display_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('display_name', 'email')
    ordering = ('username', 'display_name', 'email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Followers)
