from django.core.mail import send_mail

def order_data_sender_to_email(user,address,phone_number,message,products):
    send_mail(
          f'Заказ от {user}',
          f'АдресЖ{address}\nНомер телефона:{phone_number}\nСообщение:{message}\nТовар:{[i.title for i in products]}',
          'ailir.sunny@gmail.com',
          ['travel1234509876@gmail.com'], 
          fail_silently=False,
          )