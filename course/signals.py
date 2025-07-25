from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course, CourseLog

@receiver(post_save, sender=Course)
def log_course_changes(sender, instance, created, **kwargs):
    if created:
        action = 'created'
    else:
        action = 'updated'

    CourseLog.objects.create(course=instance, action=action)
