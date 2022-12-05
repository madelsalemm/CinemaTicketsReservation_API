from .models import Movie , Reservation , Guest , Post
from rest_framework import serializers


class MovieSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
               
class GuestSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Guest
        fields = ['pk','reservation_res','name' , 'mobile']

class ReservationSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = '__all__'

class PostSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'