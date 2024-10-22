from django.db import models
from django.contrib.auth import get_user_model

class ResearchProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lead_researcher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class ResearchData(models.Model):
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    data_file = models.FileField(upload_to='research_data/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data for {self.project.title}"
