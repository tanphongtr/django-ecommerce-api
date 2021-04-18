from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext, gettext_lazy as _
from django.conf import settings

ADDITION = 1
CHANGE = 2
DELETION = 3

ACTION_FLAG_CHOICES = (
    (ADDITION, _('Addition')),
    (CHANGE, _('Change')),
    (DELETION, _('Deletion')),
)


class LogEntry(models.Model):

    action_time = models.DateTimeField(
        _('action time'),
        auto_now=True,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        verbose_name=_('user'),
    )

    object_id = models.TextField(_('object id'), blank=True, null=True)
    # Translators: 'repr' means representation (https://docs.python.org/library/functions.html#repr)
    object_repr = models.CharField(_('object repr'), max_length=200)
    action_flag = models.PositiveSmallIntegerField(_('action flag'), choices=ACTION_FLAG_CHOICES)
    # change_message is either a string or a JSON structure
    change_message = models.TextField(_('change message'), blank=True)
