from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from blog.models import post

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name="detail", lookup_field="id")
    user = SerializerMethodField()
    class Meta:
        model = post
        fields = "id","user","title" , "content", "puplish","url",
    def get_user(self,obj):
        return str(obj.user.username)

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = "title" , "content", "puplish",

class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = "title" , "content", "puplish",

class PostDetailSerializer(ModelSerializer):
    image = SerializerMethodField()
    class Meta:
        model = post
        fields = "id","user", "title" , "image", "content", "puplish", "update",
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image