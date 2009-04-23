from unittest import defaultTestLoader
from plone.testlayers.tests.base import FooTestCase


class FooTests(FooTestCase):

    def testFoo(self):
        # the 'foo' object set up in the layer should already exist
        self.failUnless(self.portal['foo'])
        self.assertEqual(self.portal['foo'].Title(), 'foo')


def test_suite():
    return defaultTestLoader.loadTestsFromName(__name__)
