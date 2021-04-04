# django-api
https://editor.swagger.io/



from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('vi-VN', _('Vietnamese')),
]

import os
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
https://mlocati.github.io/articles/gettext-iconv-windows.html


### Run the command to create the language
python manage.py makemessages -l vi_VN
python manage.py compilemessages

## Lỗi url: vào api/v1/file không được, phải thêm / vào cuối => xem lại cấu hình media_url