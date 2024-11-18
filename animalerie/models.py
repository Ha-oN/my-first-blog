from django.db import models

class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='equipement/')
    
    def __str__(self):
        return self.id_equip


class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    couleur = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='character/')
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_character