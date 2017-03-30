from django.test import TestCase
from companies.forms import CompanyForm

class TestCompanyForm(TestCase):
    def test_valid_abn_works(self):
        form_data = {'name': 'Company', 'abn': '12345678901', 'logo': ('', None)}
        form = CompanyForm(data=form_data)
        self.assertTrue(form.is_valid(), 'Errors={0}'.format(form.errors))

    def test_blank_abn_works(self):
        form_data = {'name': 'Company', 'abn': '', 'logo': ('', None)}
        form = CompanyForm(data=form_data)
        self.assertTrue(form.is_valid(), 'Errors={0}'.format(form.errors))

    def test_invalid_abn_fails(self):
        form_data = {'name': 'Company', 'abn': '1', 'logo': ('', None)}
        form = CompanyForm(data=form_data)
        self.assertFalse(form.is_valid())

