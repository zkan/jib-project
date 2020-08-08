from django.test import TestCase

from ..models import Certificate
from workers.models import Worker


class TestCertificate(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_certificate_should_have_defined_fields(self):
        worker = Worker.objects.create(
            first_name='Kan',
            last_name='Ouivirach',
            is_available=True,
            primary_phone='1233451111',
            secondary_phone='19239201',
            address='Geeky Base',
        )

        name = 'Django Certificate by ODDS'
        issued_by = 'ProoF'

        certificate = Certificate.objects.create(
            name=name,
            issued_by=issued_by,
            worker=worker,
        )

        assert certificate.name == name
        assert certificate.issued_by == issued_by
        assert certificate.worker.first_name == worker.first_name
