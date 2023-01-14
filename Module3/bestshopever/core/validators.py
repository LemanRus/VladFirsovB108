import datetime

from django.core.exceptions import ValidationError


def validate_birth_date(value):
    if value > (datetime.datetime.now()).date() or value < (datetime.datetime.now() - datetime.timedelta(days=105*365)).date():
        raise ValidationError('Value cannot be later than today or you should be younger than 105 years')
