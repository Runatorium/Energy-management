from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from sites.models import Site, Technician
# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from sites.models import Site, Technician

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from sites.models import Site, Technician

class RoleBasedPermissionTests(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_user(username="admin", password="adminpass", is_staff=True)
        self.tech = User.objects.create_user(username="tech", password="techpass", is_staff=False)

        self.site = Site.objects.create(name="Main Plant", location="Zone A")

        self.technician = Technician.objects.create(user=self.tech)
        self.site.technicians.add(self.technician)

    def test_admin_can_delete_site(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse("site-delete", args=[self.site.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_technician_cannot_delete_site(self):
        self.client.force_authenticate(user=self.tech)
        url = reverse("site-delete", args=[self.site.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_update_site(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse("site-update", args=[self.site.id])
        response = self.client.put(url, {
            "name": "Updated Plant",
            "location": "Updated Zone",
            "technicians": [self.technician.id]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Plant")

    def test_technician_cannot_update_site(self):
        self.client.force_authenticate(user=self.tech)
        url = reverse("site-update", args=[self.site.id])
        response = self.client.put(url, {
            "name": "Tech Changed Plant",
            "location": "Tech Zone",
            "technicians": [self.technician.id]
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_technician_can_view_site_detail(self):
        self.client.force_authenticate(user=self.tech)
        url = reverse("site-detail", args=[self.site.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Main Plant")
