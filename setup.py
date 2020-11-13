from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='organize-media',
      version='1.1.0',
      description='This script copies the media files in the correct path as described by Daniele Carrer',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
      ],
      url='http://github.com/alepuzio/organize-media',
      author='Alessandro Puzielli aka Alepuzio',
      author_email='alessandro.puzielli@alepuzio.net',
      license='GPL 3',
      packages=['src'],
      install_requires=[
          'markdown',
      ],
      entry_points={
          'console_scripts': ['organize-media=main'],
      },
      include_package_data=True,
      zip_safe=False)
