from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Flight Booking Admin'

urlpatterns = [
    path('', views.home, name='home'),
    path('flights/airport_mgmt/', views.airport_mgmt, name='airport_mgmt'),
    path('flights/accounts/', include('django.contrib.auth.urls')),
    path('flights/accounts/security_login', views.login_security, name='security_login'),
    path('flights/accounts/staff_login', views.login_staff, name='staff_login'),
    path('flights/security_clearing', views.clear_security, name='security_clearing'),
    path('flights/clearing_for_security/<str:pk>', views.clear_for_security, name='clearing_for_security'),
    path('flights/view_flights', views.view_flights, name='view_flights'),
    path('flights/self_check_in/<int:pk>', views.self_check_in, name='self_check_in'),
    path('flights/search_by_source', views.search_by_source, name='search_by_source'),
    path('flights/search_by_destination', views.search_by_destination, name='search_by_destination'),
    path('flights/staff_home/<int:flight_no>', views.staff_home, name='staff_home'),
    path('flights/view_available_flights/', views.view_available_flights, name='view_available_flights'),
    path('flights/book_flight/<int:pk>', views.book_flight, name='book_flight'),
    path('flights/passenger_home/<int:pk>', views.passenger_home, name='passenger_home'),
    path('flights/create_pdf/<int:pk>', views.create_pdf, name='create_pdf'),
    path('flights/staff_check_in/<int:pk>', views.staff_check_in, name='staff_check_in'),
    path('flights/generate_report/<int:flight_no>', views.generate_report, name='generate_report'),
    path('flights/delete_passenger/<int:flight_no>', views.delete_passengers, name='delete_passengers'),
    path('flights/view_booking', views.view_booking, name='view_booking')

]
