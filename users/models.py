from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    """User who can log-in to the application."""
