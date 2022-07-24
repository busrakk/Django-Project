from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Student

#yeni profil oluşturmak için
def student_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='student')
        instance.groups.add(group)

        Student.objects.create(
            user=instance,
            name=instance.username,
        )

post_save.connect(student_profile, sender=User)