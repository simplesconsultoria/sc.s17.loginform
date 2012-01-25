from setuptools import setup, find_packages
import os

version = '0.8'

requires = [
      'setuptools',
      # -*- Extra requirements: -*-
      'pyramid',
      'repoze.who',
      'repoze.who.plugins.formcookie',
      'Babel',
]

tests_requires = requires + ['WebTest', 'nose']

setup(name='sc.s17.loginform',
      version=version,
      description="""A standalone Pyramid app providing a Login Form to be 
                     used with wsgi servers""",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      keywords='web pyramid pylons wsgi login repozo.who',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://github.com/simplesconsultoria/sc.s17.loginform',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sc', 'sc.s17'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      #message_extractors={'sc/': [
      #      ('**.py', 'lingua_python', None),
      #      ('**.pt', 'lingua_xml', None),
      #      ]},
      tests_require=tests_requires,
      test_suite="sc.s17.loginform",
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = sc.s17.loginform:main
      """,
      )
