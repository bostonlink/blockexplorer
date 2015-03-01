from setuptools import setup

setup(name='blockexplorer',
      version='1.0',
      description='blockexplorer.com python module to lookup bitcoin addresses and transactions',
      url='http://github.com/bostonlink',
      author='David Bressler (@bostonlink), GuidePoint Security, LLC.',
      author_email='bostonlink@igetshells.io',
      license='GNU GPL',
      packages=['blockexplorer'],
      zip_safe=False,
      install_requires=['requests',
                        'lxml',
                        'beautifulsoup4']
      )
