from Testing.ZopeTestCase import app, close, installPackage
from AccessControl.SecurityManagement import newSecurityManager
from Products.Five import fiveconfigure
from Products.Five.zcml import load_config
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import PloneSite
from Products.CMFCore.utils import getToolByName
from transaction import commit


def makeTestLayer(packages, profile, name=None,
        create=None, destroy=None, quiet=True):
    """ generate a layer that will set up a package-specific test
        environment by loading zcml, a genericsetup profile and optionally
        createing sample content """

    class PackageTestLayer(PloneSite):

        @classmethod
        def setUp(cls):
            # load zcml
            fiveconfigure.debug_mode = True
            for pkg in packages:
                module = __import__(pkg)
                for comp in pkg.split('.')[1:]:
                    module = getattr(module, comp)
                load_config('configure.zcml', module)
            fiveconfigure.debug_mode = False
            # install packages (products cannot be loaded from the layer)
            for pkg in packages:
                installPackage(pkg, quiet=quiet)
            # import profile
            root = app()
            prof = 'profile-%s' % profile
            tool = getToolByName(root.plone, 'portal_setup')
            tool.runAllImportStepsFromProfile(prof, purge_old=False)
            # login as admin (copied from `loginAsPortalOwner`) and
            # create some sample content
            uf = root.acl_users
            user = uf.getUserById(PloneTestCase.portal_owner).__of__(uf)
            newSecurityManager(None, user)
            if create:
                create(root.plone)
            # and commit the changes
            commit()
            close(root)

        @classmethod
        def tearDown(cls):
            root = app()
            # login as admin (copied from `loginAsPortalOwner`) and
            # remove the sample content again...
            uf = root.acl_users
            user = uf.getUserById(PloneTestCase.portal_owner).__of__(uf)
            newSecurityManager(None, user)
            if destroy:
                destroy(root.plone)
            # commit the cleanup...
            commit()
            close(root)

    if name is not None:
        PackageTestLayer.__name__ = name

    return PackageTestLayer
