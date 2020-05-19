from rest_framework import serializers
from jobs.models import JobOffer
from datetime import datetime
from django.utils.timesince import timesince


class JobOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        exclude = ("id", )
        # fields = "__all__" # we eant all the fields of our model
        # fields = ("title"," description",...,)
        
