from django.contrib import admin
from django.test import TestCase

from .admin import WorkerAdmin
from .models import Worker


class TestWorker(TestCase):
    def test_worker_should_have_defined_fields(self):
        # Given
        first_name = 'Keng'
        last_name = 'Mak'
        is_available = True
        primary_phone = '081-689-777x'
        secondary_phone = '081-689-778x'
        address = 'Geeky Base All Stars'

        # When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )

        # Then
        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertTrue(worker.is_available)
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)


class WorkerAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[Worker], WorkerAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'first_name',
            'last_name',
            'is_available',
            'primary_phone',
            'secondary_phone',
        )
        self.assertEqual(WorkerAdmin.list_display, expected)

    def test_admin_should_set_list_filter(self):
        expected = (
            'is_available',
        )
        self.assertEqual(WorkerAdmin.list_filter, expected)