import json

from django.test import TestCase

from ..models import Worker


class TestWorkerListView(TestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get('/workers/')
        # print(dir(response))
        self.assertEqual(response.status_code, 200)

    def test_view_should_render_list_of_worker_names(self):
        # Given
        Worker.objects.create(
            first_name='Kan',
            last_name='Ouivirach',
            is_available=True,
            primary_phone='1233451111',
            secondary_phone='19239201',
            address='Geeky Base',
        )
        Worker.objects.create(
            first_name='Keng',
            last_name='Mak',
            is_available=False,
            primary_phone='123315111',
            secondary_phone='1923669201',
            address='Oddstria',
        )

        # When
        response = self.client.get('/workers/')

        # Then
        # self.assertContains(response, '<li>Kan</li>')
        # self.assertContains(response, '<li>Keng</li>')

        expected = [
            {
                'first_name': 'Kan',
                'last_name': 'Ouivirach',
                'is_available': True,
                'primary_phone': '1233451111',
                'secondary_phone': '19239201',
                'address': 'Geeky Base',
            },
            {
                'first_name': 'Keng',
                'last_name': 'Mak',
                'is_available': False,
                'primary_phone': '123315111',
                'secondary_phone': '1923669201',
                'address': 'Oddstria',
            }
        ]
        self.assertEqual(
            response.content.decode('utf-8'), 
            json.dumps(expected)
        )
        