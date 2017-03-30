from lettuce import *
#from lxml import html
from django.test.client import Client
#from nose.tools import assert_equals
from lettuce.django import django_url

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(django_url(url))
    world.content = response.content

@step(u'Then I see the content "([^"]*)"')
def then_i_see_the_content_group1(step, content):
    assert content in world.content.decode('utf-8'), 'Content \'{0}\' not found in {1}'.format(content, world.content)

@step(u'When I create the company "([^"]*)" with ABN "([^"]*)"')
def when_i_create_the_company_group1_with_abn_group2(step, company, abn):
    form_data = {'name': company, 'abn': abn, 'logo': ('', None)}
    response = world.browser.post(django_url("/create/"), form_data, follow=True)
    world.content = response.content

@step(u'When I create the company "([^"]*)" with ABN ""')
def when_i_create_the_company_group1_with_abn(step, company):
    when_i_create_the_company_group1_with_abn_group2(step, company, '')

@step(u'Then I do not see the content "([^"]*)"')
def then_i_do_not_see_the_content_group1(step, content):
    assert content not in world.content.decode('utf-8'), 'Content \'{0}\' was not found in {1}'.format(content, world.content)

