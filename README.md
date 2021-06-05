```
docker-compose --env-file .env.dev config
docker-compose --env-file .env.dev up
```

## django-api
https://editor.swagger.io/


```python
from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('vi-VN', _('Vietnamese')),
]
```

```python
import os
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
```
https://mlocati.github.io/articles/gettext-iconv-windows.html


### Run the command to create the language
python manage.py makemessages -l vi_VN
python manage.py compilemessages

## Lỗi url: vào api/v1/file không được, phải thêm / vào cuối => xem lại cấu hình media_url

## DOCKER
Chạy lần đầu TK SupperUser sẽ tự động create:
- User: admin
- Password: 123456


## Run Jupyter

Open project by cmd run jupyter-lab

In notebook add to cell:
```python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings')
os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'true')
import django
django.setup()
```
## Dump/Load Data
https://docs.djangoproject.com/en/3.2/ref/django-admin/#django-admin-dumpdata

python manage.py dumpdata -o filename.ext --format EXT
python manage.py loaddata filename.ext

--format default: Json, yaml, xml


## Send test email
python manage.py sendtestemail your-email@gmail.com


## Docker

Exploring Docker container's file system
```
docker ps
```
Then:
```
docker exec -t -i mycontainer /bin/bash
docker exec -t -i mycontainer sh
```

## MySQL
```
mysql -uroot -p123456

show databases;
use database-name
```
```
source /var/www/scripts/xxx.sql
```


## Heroku
```
Error: Cannot run more than 1 Free size dynos.
Fix: https://stackoverflow.com/questions/34727605/heroku-cannot-run-more-than-1-free-size-dynos
```

## Celery
celery -A proj worker -l INFO
python3 -m celery -A django_api worker -l info

## Code import
```py
import tablib
from import_export import resources
from app.models import Post
import pandas as pd
from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User


class PostResource(resources.ModelResource):
    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(User, 'username'))
    class Meta:
        model = Post
        

xlsx = pd.ExcelFile("post.xlsx")
df = pd.read_excel(xlsx)
data = df.values.tolist()
post_resource = resources.modelresource_factory(model=Post, resource_class=PostResource)()
dataset = tablib.Dataset(*data)
dataset.headers = ['title', 'content', 'user','status','update_at','created_at']

result = post_resource.import_data(dataset, dry_run=True)
print(result.has_errors())

result = post_resource.import_data(dataset, dry_run=False)

```


https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction

```
$ pip install -r requirements.txt
```