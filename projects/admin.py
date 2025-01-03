from django.contrib import admin
# from mypage.widgets import RichTextEditorWidget
from .models import SettingGroup, Setting, Testimonial, Enquiry, Amenity, Project, ProjectImage, ProjectDoc, ProjectFloorPlan, ProjectHighlight, ProjectTimeline, ProjectTimelineMedia, Investor
# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    exclude = ["created_at", "updated_at"]


@admin.register(SettingGroup)
class SettingGroupAdmin(BaseModelAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Setting)
class SettingAdmin(BaseModelAdmin):
    autocomplete_fields = ["group"]


@admin.register(Testimonial)
class TestimonialAdmin(BaseModelAdmin):
    pass


@admin.register(Enquiry)
class EnquiryAdmin(BaseModelAdmin):
    pass


@admin.register(Amenity)
class AmenityAdmin(BaseModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(BaseModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    # autocomplete_fields = ["amenities"]


@admin.register(ProjectImage)
class ProjectImageAdmin(BaseModelAdmin):
    pass


@admin.register(ProjectDoc)
class ProjectDocAdmin(BaseModelAdmin):
    pass


@admin.register(ProjectFloorPlan)
class ProjectFloorPlanAdmin(BaseModelAdmin):
    pass


@admin.register(ProjectHighlight)
class ProjectHighlightAdmin(BaseModelAdmin):
    pass


@admin.register(ProjectTimeline)
class ProjectTimelineAdmin(BaseModelAdmin):
    pass


@admin.register(ProjectTimelineMedia)
class ProjectTimelineMediaAdmin(BaseModelAdmin):
    pass


@admin.register(Investor)
class InvestorAdmin(BaseModelAdmin):
    pass
