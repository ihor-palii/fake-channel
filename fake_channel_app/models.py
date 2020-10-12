from django.db import models


class OrgConfig(models.Model):
    callback_url = models.CharField(max_length=256)

    def __str__(self):
        return f"Version {self.pk}"

    @classmethod
    def instance(cls):
        return cls.objects.order_by("pk").last()


class ResponseSet(models.Model):
    number_of_response = models.PositiveIntegerField(default=0)
    text_of_response = models.TextField(max_length=256)

    @classmethod
    def get(cls, number=0):
        response = cls.objects.filter(number_of_response=number).first()
        if response:
            return response.text_of_response
        return ""


class Contact(models.Model):
    number = models.CharField(max_length=100, primary_key=True)
    requests_count = models.PositiveIntegerField(default=0)

    def get_response(self):
        self.requests_count += 1
        self.save()
        return ResponseSet.get(self.requests_count)
