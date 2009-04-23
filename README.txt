plone.testlayers
================

Introduction
------------

`plone.testlayers`_ is supposed to make setting up test layers for Plone
integration tests quick and painless.  It's main function, `makeTestLayer`
will conveniently generate a test layer, which will load your packages ZCML
and install them, apply a `GenericSetup` profile and help you set up sample
content for speedier testing.

  .. _`plone.testlayers`: http://github.com/witsch/plone.testlayers/


Usage
-----

To make use of `plone.testlayers`_ you'd typically create a base test case for
your package, somewhat like::

  from Products.PloneTestCase import PloneTestCase as ptc
  from plone.testlayers import makeTestLayer

  def create(portal):
      """ create sample content for test runs """
      portal.invokeFactory('File', 'foo', title='foo', file='foo bar')

  def destroy(portal):
      """ clean up sample content for test runs """
      portal.manage_delObjects(ids='foo')

  ptc.setupPloneSite()
  FooLayer = makeTestLayer(packages=('collective.foo', 'collective.bar'),
      profile='collective.foo:default', create=create, destroy=destroy)

  class FooTestCase(ptc.PloneTestCase):
      """ base class for integration tests """
      layer = FooLayer

With that in place you can now set up your individual test cases like::

  from unittest import defaultTestLoader
  from collective.foo.tests.base import FooTestCase

  class FooTests(FooTestCase):

      def testFoo(self):
          # the 'foo' object set up in the layer should already exist
          self.failUnless(self.portal['foo'])

  def test_suite():
      return defaultTestLoader.loadTestsFromName(__name__)
