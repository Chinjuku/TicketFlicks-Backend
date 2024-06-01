from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["isAdmin"] = user.isAdmin
        
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        data["user_id"] = user.id
        data["email"] = user.email
        data["isAdmin"] = user.isAdmin

        return data
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer