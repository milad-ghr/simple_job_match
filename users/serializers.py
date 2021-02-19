from rest_framework import serializers

from users.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'profile_photo', 'resume', 'phone', 'phone_confirmed', 'username', 'first_name',
                  'last_name']