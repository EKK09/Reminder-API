from rest_framework import serializers
from reminderApi.models.ReminderTagModel import ReminderTag
from reminderApi.models.ReminderCategoryModel import ReminderCategory
from reminderApi.models.ReminderModel import Reminder


class ReminderTagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = ReminderTag
        fields = ['id', 'name']


class ReminderCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = ReminderCategory
        fields = ['id', 'name']


class ReminderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Reminder
        fields = ['id', 'title', 'remind_time', 'finished']
