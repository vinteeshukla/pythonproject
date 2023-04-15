from email.policy import default
from datetime import datetime
from tkinter import CASCADE
from django.db import models
import jsonfield


class DetailForm(models.Model):
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(
        max_length=150, blank=True, null=True, default='')
    name = models.CharField(max_length=250, blank=True)
    password = models.CharField(max_length=250, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    detail_id = models.IntegerField(blank=True, null=True)
    chatbot_title = models.CharField(max_length=250, blank=True)
    x_coordinate_of_button=models.IntegerField(blank=True, null=True)   
    y_coordinate_of_button =models.IntegerField(blank=True, null=True)   


def __str__(self):
    return self.name


def __init__(self):
    return self.name, self.chatbot_title



def save(self, *args, **kwargs):
    super(DetailForm, self).save(*args, **kwargs)


class user(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()


def __str__(self):
    return self.age


class syllabus(models.Model):
    subject = models.CharField(max_length=250)


def __str__(self):
    return self.subject


class text(models.Model):
    message = models.TextField(max_length=250)
    time = models.DateTimeField(default=datetime.now)


class NewJoin_Detail(models.Model):
    name_id = models.ForeignKey(
        'DetailForm', on_delete=models.SET_NULL, null=True, blank=True)
    message_id = models.ForeignKey(
        'text', on_delete=models.SET_NULL, null=True, blank=True)


def __unicode__(self):
    return self.name_id, self.message_id


class Scratch_values(models.Model):
    chatbot_title = models.CharField(max_length=250, blank=True)
    scratch_id = models.IntegerField(blank=True, null=True)


def __str__(self):
    return self.chatbot_title


class Gambit_container(models.Model):
    gambit_id = models.IntegerField(null=True)
    gambit_name = models.CharField(max_length=250, blank=True)
    chatbot_name = models.CharField(max_length=250, blank=True)


class New_chatbot_values(models.Model):
    chatbot_id = models.IntegerField(blank=True, null=True)
    chatbot_title = models.ForeignKey(
        'Scratch_values', db_column='chatbot_title', on_delete=models.CASCADE)
    name = models.ForeignKey(
        'DetailForm', db_column='name', on_delete=models.CASCADE)


class New_Gambit_container(models.Model):
    New_Gambit_created_id = models.IntegerField(blank=True, null=True)
    New_Gambit_created_name = models.CharField(max_length=250, blank=True)
    chatbot_name = models.CharField(max_length=250, blank=True)
    connec_btn_value = models.CharField(max_length=250, blank=True)


class MyModel(models.Model):
    the_json = jsonfield.JSONField()
