from django.db import models

# Create your models here.
class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

    def __repr__(self):
        return f"Name: {self.name}, House: {self.house}, Pet: {self.pet}, Year: {self.year}"

#Comandos shell
#Wizard.objects.create(name="Harry Potter",house="Griffindor",pet="Hedwig",year=5)
#Wizard.objects.create(name="Hermione Granger",house="Griffindor",pet="Crookshanks",year=5)
#Wizard.objects.create(name="Luna Lovegood", house="Ravenclaw", pet="None", year="4")
#Wizard.objects.create(name="Padma Patil", house="Ravenclaw", pet="None", year="5")
#Wizard.objects.create(name="Draco Malfoy", house="Slytherim", pet="None", year="5")
#Wizard.objects.get(id=1)
#Wizard.objects.first()  
#Wizard.objects.last() 
#Wizard.objects.filter(house="Griffindor")
#Wizard.objects.exclude(house="Griffindor")
#Wizard.objects.all().order_by("name")
#Wizard.objects.all().order_by("-name")

# Para actualizar un registro...
#wizard_for_update = Wizard.objects.get(name="Luna Lovegood")
#wizard_for_update.pet = "Garfield"
#wizard_for_update.save()

# Para eliminar un registro...
#wizard_for_delete = Wizard.objects.get(id=5)
#wizard_for_delete.delete()

# Para eliminar varios registros...
#wizard_for_delete = Wizard.objects.filter(house="Ravenclaw") (esta consulta devuelve 2 registros)
#wizard_for_delete.delete() 

