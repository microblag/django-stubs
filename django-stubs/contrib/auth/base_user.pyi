from typing import Any, Optional, Tuple, List

from django.db import models

class BaseUserManager(models.Manager):
    @classmethod
    def normalize_email(cls, email: Optional[str]) -> str: ...
    def make_random_password(self, length: int = ..., allowed_chars: str = ...) -> str: ...
    def get_by_natural_key(self, username: Optional[str]) -> AbstractBaseUser: ...

class AbstractBaseUser(models.Model):
    password: models.CharField = ...
    last_login: Optional[models.DateTimeField] = ...
    is_active: models.BooleanField = ...
    REQUIRED_FIELDS: List[str] = ...
    class Meta:
        abstract: bool = True
    def get_username(self) -> str: ...
    def clean(self) -> None: ...
    def save(self, *args: Any, **kwargs: Any) -> None: ...
    def natural_key(self) -> Tuple[str]: ...
    @property
    def is_anonymous(self) -> bool: ...
    @property
    def is_authenticated(self) -> bool: ...
    def set_password(self, raw_password: Optional[str]) -> None: ...
    def check_password(self, raw_password: str) -> bool: ...
    def set_unusable_password(self) -> None: ...
    def has_usable_password(self) -> bool: ...
    def get_session_auth_hash(self) -> str: ...
    @classmethod
    def get_email_field_name(cls) -> str: ...
    @classmethod
    def normalize_username(cls, username: str) -> str: ...
