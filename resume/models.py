from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    person = models.ForeignKey(Person, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    coursework = models.TextField(blank=True)

class Skill(models.Model):
    person = models.ForeignKey(Person, related_name='skills', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True)
    skills_list = models.TextField()

class Experience(models.Model):
    person = models.ForeignKey(Person, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

class Project(models.Model):
    person = models.ForeignKey(Person, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Detail(models.Model):
    experience = models.ForeignKey(Experience, related_name = 'expirence_details', on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, related_name = 'project_details', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()