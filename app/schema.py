import graphene
from graphene import relay

from graphene.types import field
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug

from app.models import Category, Ingredient, User

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        interfaces = (relay.Node,)  # make sure you add this
        fields = ("id", "name", "notes", "category")

class IngredientConnection(relay.Connection):
    class Meta:
        node = IngredientType

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ['password']

class UserConnection(relay.Connection):
    class Meta:
        node = UserType

class Query(
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")
    # all_ingredients = graphene.List(IngredientType)
    all_ingredients = relay.ConnectionField(IngredientConnection)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    users = relay.ConnectionField(UserConnection)

    def resolve_users(root, info):
        # We can easily optimize query count in the resolve method
        return User.objects.all()

    def resolve_all_ingredients(root, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)