from rest_framework import serializers
from reminderApi.models.ReminderTagModel import ReminderTag
from reminderApi.models.ReminderCategoryModel import ReminderCategory
from reminderApi.models.ReminderModel import Reminder


class ReminderTagSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = ReminderTag
        fields = ['id', 'name']


class ReminderCategorySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = ReminderCategory
        fields = ['id', 'name']


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ['id', 'title', 'remind_time',
                  'finished', 'category']

    def to_representation(self, instance):
        self.fields['category'] = ReminderCategorySerializer(
            read_only=True)
        return super(ReminderSerializer, self).to_representation(instance)
