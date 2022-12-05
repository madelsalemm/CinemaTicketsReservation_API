from django.urls import path , include
from . import views
from rest_framework.authtoken import views as ve

app_name = 'tickets'


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', views.Viewsets_guest, basename='viewsets_guest')

router1 = DefaultRouter()
router1.register('', views.Viewsets_Movie, basename='viewsets_movie')

router2 = DefaultRouter()
router2.register('', views.Viewsets_Reservation, basename='viewsets_reservation')


urlpatterns = [
    #1
    path('django/jsonresponsenomodel', views.no_rest_no_model, name='no_rest_no_model'),
    #2
    path('django/jsonresponsefrommodel', views.no_rest_from_model, name='no_rest_from_model'),
    #3.1
    path('rest/fbvlist', views.fbv_list, name='fbv_list'),
    #3.2
    path('rest/fbvpk/<int:pk>', views.fbv_pk, name='fbv_pk'),
    #4.1
    path('rest/cbv/', views.CBV_List.as_view(), name='cbv'),
    #4.2
    path('rest/cbv_pk/<int:pk>', views.CBV_PK.as_view(), name='cbv'),
    #5.1
    path('rest/mixins', views.Mixins_list.as_view(), name='mixins'),
    #5.2
    path('rest/mixins/<int:pk>', views.Mixins_Pk.as_view(), name='mixinspk'),
    #6.1
    path('rest/generics', views.GenericsList.as_view(), name='genericslist'),
    #6.2
    path('rest/generics/<int:pk>', views.GenericsPK.as_view(), name='genericsPK'),
    #7
    path('rest/viewsetsguests/', include (router.urls)),
    path('rest/viewsetsmovie/', include (router1.urls)),
    path('rest/viewsetsreservations/', include (router2.urls)),
    #8
    path('rest/find_movie', views.find_movie, name='find_movie'), #test the GET "search" By Postman
    #9
    path('rest/make_reservation', views.make_reservation, name='make_reservation'), #test the make_reservation
    # get the user token number
    path('api-token-auth/', ve.obtain_auth_token), #access from user to get token number 
    #10     posts
    path('rest/post/<int:pk>', views.Post_PK.as_view(), name='post_pk'),
    
]
