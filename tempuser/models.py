from django.db import models

# 테이블 이름 단수
# Attriubute snake_case
# Attribute lower case

class User(models.Model):

    email = models.CharField(unique=True, max_length=191)
    nickname = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.email
