# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('brambling', '0017_housingslot_person'),
        #migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id'),
            preserve_default=True,
        ),
    ]
