from dataclasses import dataclass
from django.db import models

# @dataclass
# class Actor:
#     id: int
#     first_name: str
#     last_name: str



class Genre:
    name = models.CharField(max_length=255)


class Actor:
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
