from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
   
    def short_content(self):
        return f'{self.content[:100]}......'
  