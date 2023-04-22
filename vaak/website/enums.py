from django.db import models
from django.utils.translation import gettext_lazy as _


class PeopleRoleChoice(models.IntegerChoices):
    DIRECTOR = 0, "Director"
    TEAM_MEMBER = 1, "Team Member"


class SubjectChoice(models.IntegerChoices):
    TECHNICAL_SUPPORT = 0, "Technical Support"
    SALES_INQUIRIES = 1, "Sales Inquiries"


class IndustryChoice(models.IntegerChoices):
    SPOTIFY_ADS = 1, "Spotify Ads"
    OPPO_CARE = 2, "Oppo Care"
    JIO_CUSTOMER_SUPPORT = 3, "Jio Customer Support"


class VideoTypeChoice(models.IntegerChoices):
    VIDEO_TYPE = 0, "Video Type"