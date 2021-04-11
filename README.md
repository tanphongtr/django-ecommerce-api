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