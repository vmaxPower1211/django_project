from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class TreeNode(MPTTModel):
    name=models.CharField(max_length=255)
    parent=TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by=['name']
        
    def __str__(self):
        return self.name
    
class Person(models.Model):
    name=models.CharField(max_length=255)
    sex=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return super().__str__()
    