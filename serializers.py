from rest_framework import serializers
from .models import Trains

class TrainsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Trains
        fields=['id','name','train_no','starting','ending','price','timings','type']
