from Products.PloneTestCase import PloneTestCase as ptc
from plone.testlayers import makeTestLayer


def create(portal):
    """ create sample content for test runs """
    portal.invokeFactory('File', 'foo', title='foo', file='foo bar')

def destroy(portal):
    """ clean up sample content for test runs """
    portal.manage_delObjects(ids='foo')

ptc.setupPloneSite()
MyLayer = makeTestLayer(packages=('plone.testlayers', 'plone.pony'),
    profile='plone.testlayers:default', create=create, destroy=destroy)


class MyTestCase(ptc.PloneTestCase):
    """ base class for integration tests """

    layer = MyLayer
