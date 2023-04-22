from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_extensions.db.models import TimeStampedModel
from website.enums import (
    PeopleRoleChoice,
    SubjectChoice,
    IndustryChoice,
    VideoTypeChoice,
)

# Create your models here.
class NavbarCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.CharField(max_length=30, unique=True)


# Home Page Models : Start
class SuccessStorys(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    profile_pic = models.ImageField(upload_to="Success-storys-profile/")
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'SuccessStory'
        verbose_name = 'SuccessStorys'
        verbose_name_plural = 'SuccessStorys'

    def __str__(self) -> str:
        return str(self.name)


class VideoServicesCategory(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'VideoServicesCategory'
        verbose_name = 'VideoServicesCategory'
        verbose_name_plural = 'VideoServicesCategories'

    def __str__(self) -> str:
        return str(self.title)
    

class ContactUs(TimeStampedModel):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    company = models.CharField(max_length=255)
    subject = models.IntegerField(max_length=255, choices=SubjectChoice.choices)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ContactUs'
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self) -> str:
        return str(self.name)
    

class WorkDemo(TimeStampedModel):

    title = models.CharField(max_length=50, unique=True)
    video_link = models.URLField(max_length=255, unique=True)
    industry_name = models.IntegerField(choices=IndustryChoice.choices)

    class Meta:
        db_table = 'WorkDemo'
        verbose_name = 'WorkDemo'
        verbose_name_plural = 'WorkDemos'

    def __str__(self) -> str:
        return str(self.title)
    

class Insight(TimeStampedModel):
    
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_by = models.IntegerField()
    image = models.ImageField(upload_to="insight_images/")

    class Meta:
        db_table = 'Insight'
        verbose_name = 'Insight'
        verbose_name_plural = 'Insights'

    def __str__(self) -> str:
        return str(self.title)
    

# About Us Page : Start
class PeopleOfVaak(TimeStampedModel):

    name = models.CharField(max_length=255)
    designation = models.TextField()
    image = models.FileField(upload_to="peoples-profiles/", null=True, blank=True)
    role = models.IntegerField(choices=PeopleRoleChoice.choices)

    class Meta:
        db_table = 'PeopleOfVaak'
        verbose_name = 'PeopleOfVaak'
        verbose_name_plural = 'PeopleOfVaak'

    def __str__(self) -> str:
        return str(self.name)
    

# Case Studies Page : Start
class Project(TimeStampedModel):
    industry = models.IntegerField(choices=IndustryChoice.choices)
    name = models.CharField(max_length=100, unique=True)
    video_link = models.URLField(max_length=255, unique=True)
    company_name = models.CharField(max_length=100)
    video_type = models.IntegerField(choices=VideoTypeChoice.choices)
    description = models.TextField()
    style_name = models.CharField(max_length=50)
    objective = models.CharField(max_length=255)
    related_image = models.ImageField(upload_to="project-related-images/")

    class Meta:
        db_table = 'Project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self) -> str:
        return str(self.name)
    

# Services Page : Start
class VideoServices(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)
    video_link = models.URLField(max_length=255, unique=True)
    category = models.ForeignKey(VideoServicesCategory, related_name="video_services", on_delete=models.CASCADE)

    class Meta:
        db_table = 'VideoServices'
        verbose_name = 'VideoServices'
        verbose_name_plural = 'VideoServices'

    def __str__(self) -> str:
        return str(self.title)
    

# Blog pages : start
class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey("User", on_delete=models.CASCADE , related_name="user_blog_post")

    class Meta:
        db_table = "BlogPost"
        verbose_name = 'BlogPost'
        verbose_name_plural = 'BlogPosts'


    def __str__(self) -> str:
        return self.title


# Our Price Page : start
class PackeageDeatail(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="price-package-images/")

    class Meta:
        db_table = "PackeageDeatail"
        verbose_name = 'PackeageDeatail'
        verbose_name_plural = 'PackeageDeatails'


    def __str__(self) -> str:
        return self.title