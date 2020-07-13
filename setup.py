from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='update-microstock-names',
      version='0.1',
      description='This script renames all images (RAW and JPG) and videos (MOV) in the root directory and his sub-directories',
	  long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GPL 3 License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
      ],
      url='http://github.com/alepuzio/update-microstock-names',
      author='Alessandro Puzielli aka Alepuzio',
      author_email='alessandro.puzielli@alepuzio.net',
      license='GPL 3',
      packages=['explicate-img-names'],
	  install_requires=[
          'markdown',
      ],
	  tests_require=['rivedere'],
      entry_points={
          'console_scripts': ['explicate-img-names=funniest.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
