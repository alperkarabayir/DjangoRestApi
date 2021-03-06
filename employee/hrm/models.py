from django.db import models


class Users(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    ranking = models.FloatField()

    def upload_dir(self, filename):
        path = 'hrm/photo/{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_dir, null=True, blank=True)

    def upload_file(self, filename):
        path = 'hrm/file/{}'.format(filename)
        return path

    resume = models.ImageField(upload_to=upload_file, null=True, blank=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
