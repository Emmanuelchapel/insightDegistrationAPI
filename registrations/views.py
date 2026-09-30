from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegistrationSerializer
from .service import send_registration_email


class RegistrationView(APIView):

    def post(self, request):

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():

            registration = serializer.save()

            send_registration_email(registration)

            return Response(
                {
                    "message": "Registration successful",
                    "data": RegistrationSerializer(registration).data,
                    "success": True
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "message": "Registration failed",
                 "errors": serializer.errors,
                 "success": False

            },
            status=status.HTTP_400_BAD_REQUEST,
        )