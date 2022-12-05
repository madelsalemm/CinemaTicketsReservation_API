from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Movie , Guest , Reservation , Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import GuestSerializer , MovieSerializer , ReservationSerializer , PostSerializer
from rest_framework import status , filters
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import mixins , generics , viewsets
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

# Create your views here.

# (1) no data from model no rest  FBV 
def no_rest_no_model (request):
    guests= [
        
        {
            'id':1,
            'Name':'mohamed',
            'mobile':'01026202586',
        },
        {
            'id':2,
            'Name':'adel',
            'mobile':'01122426778',
        }
    ]
    return JsonResponse (guests,safe=False)

# (2) Data from Model No rest 
def no_rest_from_model (request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name', 'mobile'))
    }
    return JsonResponse (response,safe=False)

# (3) REST FBV
# (3.1) GET POST
@api_view(['GET' , 'POST'])
#@permission_classes((permissions.AllowAny,))
def fbv_list(request):
    
    #GET
    if request.method=='GET':
        guest = Guest.objects.all()
        serializer = GuestSerializer (guest , many = True)
        return Response(serializer.data)
    #POST
    elif request.method=='POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status = status.HTTP_201_CREATED)
        return Response (serializer.data , status = status.HTTP_400_BAD_REQUEST)
    
    
# (3.2) GET PUT DELETE
@api_view(['GET' , 'PUT' , 'DELETE'])
#@permission_classes((permissions.AllowAny,))
def fbv_pk(request , pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    #GET
    if request.method=='GET':
        serializer = GuestSerializer (guest)
        return Response(serializer.data)
    #PUT
    elif request.method=='PUT':
        serializer = GuestSerializer(guest ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    #DELETE
    elif request.method=='DELETE':
        guest.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

#4 CBV
#(4.1)CBV Create == GET and POST
#@permission_classes((permissions.AllowAny,))
class CBV_List(APIView):
    def get (self , request):
        guest = Guest.objects.all()
        serializer = GuestSerializer (guest , many = True)
        return Response(serializer.data)
        
    def post (self , request):
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status = status.HTTP_201_CREATED)
        return Response (serializer.data , status = status.HTTP_400_BAD_REQUEST)
    
#(4.2)GET PUT DELETE
#@permission_classes((permissions.AllowAny,))
class CBV_PK(APIView):
    def get_object(self , pk):
        try:
            Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)
    
    def get (self , request , pk):
        guest=self.get_object(pk)
        serializer = GuestSerializer (guest)
        return Response (serializer.data)
    
    def put (self , request , pk):
        guest=self.get_object(pk)
        serializer = GuestSerializer (guest , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete (self , request , pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

#5 Mixins
#(5.1) Mixins_List
class Mixins_list(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    
    def get (self , request):
        return self.list(request)
    def post (self , request):
        return self.create(request)

#(5.2) Mixins_pk  GET POST Delete
class Mixins_Pk(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    
    def get (self , request , pk):
        return self.retrieve (request)
    def put (self , request , pk):
        return self.update(request)
    def delete (self , request , pk):
        return self.destroy (request)

#(6) Generics
#(6.1) Generics_list GET POST
class GenericsList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
#(6.2) Generics_Pk GET PUT DELETE
class GenericsPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

#(7) viewsets GET POST
class Viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = []

class Viewsets_Movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie']


class Viewsets_Reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = []

#(8) Find Movie 
@api_view(['GET'])
#@permission_classes((permissions.AllowAny,))
def find_movie(request):
    movies = Movie.objects.filter(
        hall = request.data['hall'],
        movie = request.data['movie']   
    )
    serializer = MovieSerializer(movies,many = True)
    return Response(serializer.data)

#(9) Make Reservation
@api_view(['POST'])
#@permission_classes((permissions.AllowAny,))
def make_reservation (request):
    movies = Movie.objects.get(
        hall = request.data['hall'],
        movie = request.data['movie']   
    )
    
    guest = Guest()
    guest.name = request.data['name']
    guest.mobile = request.data['mobile']
    guest.save()
    
    reservation = Reservation()
    reservation.guest=guest
    reservation.movie=movies
    reservation.save()
    serializer = MovieSerializer(reservation)
    return Response(serializer.data)


#(10) Post author Editor

class Post_PK(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


