from datetime import date
from django.db import models
from django.core.exceptions import ValidationError


class Musician(models.Model):
    """
    A model representing a musician with a first name, last name, and birth date.

    Fields:
    - first_name: The musician's first name (maximum length of 50 characters).
    - last_name: The musician's last name (maximum length of 50 characters).
    - birth_date: The musician's date of birth.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    class Meta:
        verbose_name = "Musician"
        verbose_name_plural = "Musicians"

    def __str__(self):
        return f"Musician(id={self.id}, last_name={self.last_name})"

    def clean(self):
        """Additional validation to ensure the birth_date is not in the future."""

        if self.birth_date > date.today():
            raise ValidationError("Birth date cannot be in the future.")
