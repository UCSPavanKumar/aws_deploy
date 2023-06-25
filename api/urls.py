from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("clients/", views.clientListAll, name="clientListAll"),
    path("attendants/", views.attendantListAll, name="attendantListAll"),
    path('vouchers/',views.voucherListAll,name='voucherListAll'),
    path('transactions/',views.transactionsListAll,name='transactionsListAll'),
    path('createClient/',views.createClient,name='createClient'),
    path('createTransaction/',views.createTransaction,name='createTransaction'),
    path('createAttendant/',views.createAttendant,name='createAttendant'),
    path('createVoucher/',views.createVoucher,name='createVoucher'),
    path('vouchers/<str:pk>/',views.voucher_details,name='voucher_details'),
    path('client/<str:pk>/',views.client_details,name='client_details'),
    path('attendant/<str:pk>/',views.attendant_details,name='attendant_details'),
    path('transaction/<str:pk>/',views.transaction_details,name='transaction_details'),
    path('login/',views.employeeLogin,name='employeeLogin')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)