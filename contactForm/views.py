from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact

# Create your views here.

class ContactForm(views.APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            email = data.get('email')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            phone_number = data.get('phone_number')
            message = data.get('message')
            contact = Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            contact.save()
            
            send_mail(
                'Sent email from {}'.format(f'{first_name} {last_name}'),
                'Message: {}'.format(f'{message} \n Mobile: {phone_number} \n Email: {email}'),
                email,
                ['solveit37@gmail.com'],
                fail_silently=False,
            )
            return Response({"message": "Successfully sent"}, status=status.HTTP_200_OK)
        return Response({'message': "Failed"}, status=status.HTTP_400_BAD_REQUEST)
