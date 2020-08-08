from django.test import TestCase

from ..models import Worker
from ..serializers import WorkerSerializer


class TestWorkerSerializer(TestCase):
    def test_serializer_should_return_correct_serialized_data(self):
        worker = Worker.objects.create(
            first_name='Kan',
            last_name='Ouivirach',
            is_available=True,
            primary_phone='083-xxx-xxxx',
            secondary_phone='085-xxx-1234',
            address='Oddstria',
        )
        serializer = WorkerSerializer(worker)

        expected = {
            'first_name': 'Kan',
            'last_name': 'Ouivirach',
            'is_available': True,
            'primary_phone': '083-xxx-xxxx',
            'secondary_phone': '085-xxx-1234',
            'address': 'Oddstria',
        }
        assert serializer.data == expected