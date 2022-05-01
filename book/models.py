from django.db import models

STATUS_CHOICES = [('active', 'active'), ('blocked', 'blocked')]


class GuestBook(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name="Name")
    mail = models.EmailField(max_length=40, null=False, blank=False, verbose_name="Email")
    post_text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Your text")
    time_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Update time")
    status = models.CharField(max_length=30, null=False, blank=False, verbose_name="status", default="active",
                              choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.pk}. {self.name}: {self.status}"

    class Meta:
        db_table = 'guest_book'
        verbose_name = 'book'
        verbose_name_plural = 'books'
