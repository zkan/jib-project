from django.test import TestCase

from ..models import Certificate


class TestCertificate(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_certificate_should_have_defined_fields(self):
        name = 'Django Certificate by ODDS'
        issued_by = 'ProoF'

        certificate = Certificate.objects.create(
            name=name,
            issued_by=issued_by,
        )

        assert certificate.name == name
        assert certificate.issued_by == issued_by
