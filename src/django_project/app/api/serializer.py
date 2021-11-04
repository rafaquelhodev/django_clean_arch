from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django_project.app.api.models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"
