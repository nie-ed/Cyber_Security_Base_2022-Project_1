import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Texts


class TextsModelTests(TestCase):

    def test_was_published_recently_with_future_texts(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_texts = Texts(pub_date=time)
        self.assertIs(future_texts.was_published_recently(), False)

    
    def test_was_published_recently_with_old_texts(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_texts = Texts(pub_date=time)
        self.assertIs(old_texts.was_published_recently(), False)

    
    def test_was_published_recently_with_recent_texts(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_texts = Texts(pub_date=time)
        self.assertIs(recent_texts.was_published_recently(), True)