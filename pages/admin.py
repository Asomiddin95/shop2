from django.contrib import admin
from pages.models import ContactModel


# Register your models here.


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = [
        'created_at']  # list filit 2ta tipdagi po'lya uchu ishlatiladi
    # 1) bu vaqtka aloqador polyalar uchun
    # 2) bog'langan po'lyalar uchun boladi
    search_fields = ['name', 'email',
                     'message']  # search bu qidirishga
