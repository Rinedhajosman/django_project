from django.db import models

# Create your models here.
JOB_type = (
        
       ('Full time','Full time'),
       ('Part time','Part time'),

	       )

class Job(models.Model): #tablo
    title = models.CharField(max_length =100) #sütun
    jop_type = models.CharField(max_length =15 , choices =JOB_type)
    description = models.TextField(max_length = 15)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self):
    	return self.title