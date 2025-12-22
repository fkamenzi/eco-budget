from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('budget', 'Category')
    default_categories = [
        ("Groceries", False),
        ("Transport", False),
        ("Eco Products", True),
        ("Utilities", False),
        ("Entertainment", False),
    ]
    for name, eco in default_categories:
        Category.objects.get_or_create(name=name, eco_friendly=eco)

class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
