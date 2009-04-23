from Products.PloneTestCase import PloneTestCase as ptc
from plone.testlayers import makeTestLayer


def create(portal):
    """ create sample content for test runs """
    portal.invokeFactory('File', 'foo', title='foo', file='foo bar')

def destroy(portal):
    """ clean up sample content for test runs """
    portal.manage_delObjects(ids='foo')

ptc.setupPloneSite()


class FooTestCase(ptc.PloneTestCase):
    """ base class for integration tests """

    layer = makeTestLayer(packages=('plone.testlayers', 'plone.pony'),
        profile='plone.testlayers:default', create=create, destroy=destroy,
        name='FooLayer')


class BarTestCase(ptc.PloneTestCase):
    """ alternative base class for integration tests """

    layer = makeTestLayer(packages=('plone.testlayers',),
        profile='plone.testlayers:default', create=create, destroy=destroy,
        name='BarLayer')
