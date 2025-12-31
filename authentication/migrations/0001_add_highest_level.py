from django.db import migrations


class Migration(migrations.Migration):
    initial = False

    dependencies = []

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE players ADD COLUMN IF NOT EXISTS highest_level integer DEFAULT 1;",
            reverse_sql="ALTER TABLE players DROP COLUMN IF EXISTS highest_level;",
        ),
    ]
