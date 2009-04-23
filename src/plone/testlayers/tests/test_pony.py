from unittest import defaultTestLoader
from plone.testlayers.tests.base import FooTestCase
from Products.CMFCore.utils import getToolByName


class PonyTests(FooTestCase):
    """ tests to make sure the setup of other packages works """

    def testPonyResources(self):
        """ make sure `plone.pony`'s profile (and zcml) has been loaded """
        registry = getToolByName(self.portal, 'portal_css')
        css = '++resource++plone.pony.resources/main.css'
        self.failUnless(css in registry.getResourceIds())


def test_suite():
    return defaultTestLoader.loadTestsFromName(__name__)
