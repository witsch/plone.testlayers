from setuptools import setup, find_packages
from os.path import join

readme = open("README.txt").read()
history = open(join('docs', 'HISTORY.txt')).read()

setup(name = 'plone.testlayers',
      version = '1.0a3',
      description = 'Painless setup of Plone integration test layers',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords = 'plone testing layers',
      author = 'Andreas Zeidler',
      author_email = 'az@zitc.de',
      url = 'http://pypi.python.org/pypi/plone.testlayers',
      license = 'GPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages = ['plone'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
          'setuptools',
      ],
      entry_points = '',
)
