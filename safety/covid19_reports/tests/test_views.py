from unittest.mock import patch

from django.test import TestCase


class TestCovid19ReportView(TestCase):
    @patch('covid19_reports.views.requests.get')
    def test_view_should_be_accessible(self, _):
        response = self.client.get('/covid19-reports/')
        self.assertEqual(response.status_code, 200)

    @patch('covid19_reports.views.requests.get')
    def test_view_should_call_covid19_api(self, mock):
        self.client.get('/covid19-reports/')
        mock.assert_called_once_with(
            'https://covid19.th-stat.com/api/open/today'
        )