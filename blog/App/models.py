from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200,help_text='Enter the title.')
    content = models.TextField(help_text='Enter the content here.')
    publication_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
   
    def short_content(self):
        return f'{self.content[:100]}......'
  