import os
from app.models import User

try:
    superuser = User.objects.create_superuser(
        username=os.environ['APP_ROOT_USER'],
        email=os.environ['APP_ROOT_EMAIL'],
        password=os.environ['APP_ROOT_PASSWORD'])
    superuser.save()
except:
    print(f"Super User with username {os.environ['APP_ROOT_USER']} is already present")


class CreateDb:
    def run():
        print(12312)