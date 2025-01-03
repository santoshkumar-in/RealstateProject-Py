import os
from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """Abstract base class that adds created_at and updated_at fields to models."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class SettingGroup(TimeStampedModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = "setting_groups"
        default_related_name = "setting_group"

    def __str__(self):
        return self.title


class Setting(TimeStampedModel):
    name = models.CharField(max_length=100)
    value = models.TextField()
    group = models.OneToOneField(to=SettingGroup,
                                 to_field='slug', on_delete=models.PROTECT)

    class Meta:
        db_table = "settings"

    def __str__(self):
        return self.name


class Testimonial(TimeStampedModel):
    message = models.TextField()
    user_name = models.CharField(max_length=100)
    user_detail = models.CharField(max_length=120)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "testimonials"


class Enquiry(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        db_table = "enquiries"
        default_permissions = ['view', 'change', 'delete',]
        verbose_name_plural = "enquiries"


class Amenity(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    icon = models.ImageField(null=True)

    class Meta:
        db_table = "amenities"
        ordering = ["title"]
        default_related_name = "amenities"
        verbose_name_plural = "amenities"

    def __str__(self):
        return self.title


class Project(TimeStampedModel):
    class VisibilityChoices(models.TextChoices):
        PUBLIC = "Public"
        PRIVATE = "Private"

    class CategoryChoices(models.TextChoices):
        RESIDENTIAL = 'Residential'
        COMMERCIAL = 'Commercial'
        RETAIL = 'Retail'

    class CityChoices(models.TextChoices):
        KANPUR = 'Kanpur'
        LUCKNOW = 'Lucknow'
        AYODHYA = 'Ayodhya'
        VRINDAVAN = 'Vrindavan'

    class StateChoices(models.TextChoices):
        UTTAR_PRADESH = 'Uttar Pradesh'
        DELHI = 'Delhi'
        UTTARAKHAND = 'Uttarakhand'

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(
        max_length=32,
        choices=CategoryChoices.choices, default=CategoryChoices.RESIDENTIAL)
    description = models.TextField(null=True)
    city = models.CharField(
        max_length=32, choices=CityChoices.choices, default=CityChoices.KANPUR)
    state = models.CharField(max_length=32, choices=StateChoices.choices,
                             default=StateChoices.UTTAR_PRADESH)
    pin_code = models.CharField(max_length=30)
    coordinates = models.CharField(max_length=50)
    start_date = models.DateField()
    est_completion_date = models.DateField(null=True)
    completed_on = models.DateField(null=True)
    amenities = models.ManyToManyField(to=Amenity)
    visibility = models.CharField(
        max_length=32,
        choices=VisibilityChoices.choices, default=VisibilityChoices.PRIVATE)

    class Meta:
        db_table = "projects"
        ordering = ["-completed_on", "-created_at", "title"]
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return self.title


class ProjectImage(TimeStampedModel):

    def get_upload_path(instance, filename):
        return os.path.join(
            "projects",
            instance.project.id,
            "images",
            filename)

    image = models.ImageField(upload_to=get_upload_path)
    caption = models.CharField(max_length=120, null=True)
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        db_table = "project_images"
        default_related_name = "images"


class ProjectDoc(TimeStampedModel):
    def get_upload_path(instance, filename):
        return os.path.join(
            "projects",
            instance.project.id,
            "docs",
            filename)

    name = models.CharField(max_length=100)
    doc = models.FileField(upload_to=get_upload_path)
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        db_table = "project_docs"
        default_related_name = "docs"
        verbose_name = "Project document"
        verbose_name_plural = "Project documents"


class ProjectFloorPlan(TimeStampedModel):
    def get_upload_path(instance, filename):
        return os.path.join(
            "projects",
            instance.project.id,
            "floor-plans",
            filename)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_upload_path)
    area = models.FloatField()
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        db_table = "project_floor_plans"
        default_related_name = "floor_plans"
        ordering = ["title"]

    def __str__(self):
        return self.title


class ProjectHighlight(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        db_table = "project_highlights"
        default_related_name = "highlights"

    def __str__(self):
        return self.title


class ProjectTimeline(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    completed_on = models.DateField()
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        db_table = "project_timelines"
        default_related_name = "timelines"
        ordering = ["-completed_on"]

    def __str__(self):
        return self.title


class ProjectTimelineMedia(TimeStampedModel):
    class MediaChoices(models.TextChoices):
        IMAGE = 'IMAGE'
        PDF = 'PDF'
        CSV = 'CSV'

    def get_upload_path(instance, filename):
        return os.path.join(
            "projects",
            instance.project_timeline.project.id,
            "timelines",
            instance.project_timeline.id,
            filename)

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    file = models.ImageField(null=True)
    type = models.CharField(
        max_length=32, choices=MediaChoices.choices, default=MediaChoices.IMAGE)
    project_timeline = models.ForeignKey(
        to=ProjectTimeline,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        db_table = "project_timeline_medias"
        default_related_name = "timeline_medias"

    def __str__(self):
        return self.title


class Investor(TimeStampedModel):
    name = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=100)
    projects = models.ManyToManyField(to=Project)

    class Meta:
        db_table = "investors"
        ordering = ["name"]

    def __str__(self):
        return self.name
