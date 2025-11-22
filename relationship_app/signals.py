from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
from django.contrib.auth.models import Group, Permission

def setup_groups(sender, **kwargs):
    group_permissions = {
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        "Editors": ["can_create", "can_edit"],
        "Viewers": ["can_view"],
    }

    for group_name, perms in group_permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        for codename in perms:
            try:
                permission = Permission.objects.get(codename=codename)
                group.permissions.add(permission)
            except Permission.DoesNotExist:
                continue
