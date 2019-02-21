# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Auto Generated Models file of the SQLite Database
from django.db import models


class Actor(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=80)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=80)  # Field name made lowercase.
	
    def __str__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    class Meta:
        db_table = 'actor'
        unique_together = (('firstname', 'lastname'),)


class Director(models.Model):
    directorid = models.TextField(db_column='directorID', primary_key=True)  # Field name made lowercase. This field type is a guess.
    firstname = models.CharField(db_column='firstName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=80, blank=True, null=True)  # Field name made lowercase.
	
    def __str__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    class Meta:
        db_table = 'director'



class Film(models.Model):
    filmid = models.TextField(db_column='filmID', primary_key=True )  # Field name made lowercase. This field type is a guess.
    title = models.CharField(max_length=80, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    image = models.CharField(max_length=255, blank=True, null=True)
    syn = models.CharField(max_length=1500, blank=True, null=True)
    trailer = models.CharField(max_length=255, blank=True, null=True)

    #test = models.Manager()
	
    def __str__(self):
        return u'%s' % (self.title)

    class Meta:
        db_table = 'film'

		
		
class Filmdirector(models.Model):
    filmid = models.TextField(db_column='filmID')  # Field name made lowercase. This field type is a guess.
    directorid = models.TextField(db_column='directorID')  # Field name made lowercase. This field type is a guess.
	
    class Meta:
        db_table = 'filmdirector'
        unique_together = (('filmid', 'directorid'),)



class Filmgenre(models.Model):
    filmid = models.TextField(db_column='filmID')  # Field name made lowercase. This field type is a guess.
    genrename = models.CharField(db_column='genreName', max_length=80)  # Field name made lowercase.


    class Meta:
        db_table = 'filmgenre'
        unique_together = (('filmid', 'genrename'),)


class Genre(models.Model):
    genrename = models.CharField(db_column='genreName', unique=True, max_length=80)  # Field name made lowercase.

    def __str__(self):
        return u'%s' % (self.genrename)

    class Meta:
        db_table = 'genre'


class Producer(models.Model):
    producerid = models.TextField(db_column='producerID',  primary_key=True)  # Field name made lowercase. This field type is a guess.
    producername = models.CharField(db_column='producerName', max_length=80)  # Field name made lowercase.

    def __str__(self):
        return u'%s' % (self.producername)

    class Meta:
        db_table = 'producer'


class Produces(models.Model):
    filmid = models.TextField(db_column='filmID')  # Field name made lowercase. This field type is a guess.
    producerid = models.TextField(db_column='producerID')  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'produces'
        unique_together = (('filmid', 'producerid'),)


class Role(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(max_length=80)
    filmid = models.TextField(db_column='filmID')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return u'%s %s' % (self.filmid, self.role)

    class Meta:
        db_table = 'role'
        unique_together = (('role', 'filmid'),)
