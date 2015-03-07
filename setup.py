from setuptools import setup

setup(
  name='gmail-alerts',
  version='1.0',
  packages=['gmailalerts'],
  url='https://github.com/yang/gmail-alerts',
  license='MIT',
  author='yang',
  author_email='',
  description='',
  entry_points={
    'console_scripts': [
      'gmail-alerts = gmailalerts:main'
    ]
  },
  install_requires=['google-api-python-client==1.3.2','python-gflags==2.0','path.py==7.2']
)
