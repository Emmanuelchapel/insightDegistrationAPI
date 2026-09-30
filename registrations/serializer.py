from rest_framework import serializers
from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = [
            "id",
            "full_name",
            "email",
            "phone_number",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]



    def validate_full_name(self, value):

        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Full name must contain at least 3 characters."
            )

        return value.strip()

    def validate_phone_number(self, value):

        if len(value.strip()) < 7:
            raise serializers.ValidationError(
                "Enter a valid phone number."
            )

        return value.strip()