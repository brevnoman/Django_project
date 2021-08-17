from django.contrib import admin
from main_app.models import Meeting, Conclusion


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)




class ConclusionAddAdmin(admin.StackedInline):
    model = Conclusion
    extra = 0
    exclude = ["create_time", "id", ]


@admin.register(Meeting)
class MeetingsAdmin(admin.ModelAdmin):
    exclude = ["id", "user"]
    readonly_fields = ['description', 'phone_number']
    fields = ['description', 'phone_number', 'time_start', 'time_end', 'date', 'is_accepted', 'is_done']
    inlines = [ConclusionAddAdmin]



@admin.register(Conclusion)
class ConclusionAdmin(admin.ModelAdmin):
    exclude = ["id", "create_time"]

# admin.site.register(Meetings)
# admin.site.register(Conclusion)

