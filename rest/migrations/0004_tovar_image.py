from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("rest", "0003_tovar")]
    operations = [
        migrations.AddField(
            model_name="tovar",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]
