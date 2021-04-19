from django.test import TestCase
import re as r
from .models import Adetails, Report_sound


class TestAssetDetails(TestCase):

    @classmethod
    def setUpTestData(cls):
        ip = "8897"
        name = "test"
        description = "wow nice assets"
        tags = "hello test comeone"
        Adetails.objects.create(
            ip=ip, name=name, description=description, tags=tags)

    def test_name_max_length(self):
        assetDetails = Adetails.objects.get(id=1)
        name_max_length = assetDetails._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 20)

    def test_description_max_length(self):
        assetDetails = Adetails.objects.get(id=1)
        description_max_length = assetDetails._meta.get_field('description').max_length
        self.assertEqual(description_max_length, 20)

    def test_tags_max_length(self):
        assetDetails = Adetails.objects.get(id=1)
        description_max_length = assetDetails._meta.get_field('tags').max_length
        self.assertEqual(description_max_length, 30)

    def test_ip_max_length(self):
        ip_regex = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])\\.){3}"\
            "([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])"
        assetDetails = Adetails.objects.get(id=1)
        ip_value = assetDetails.ip        
        assert r.search(ip_regex, ip_value)