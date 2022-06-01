from setuptools import setup

setup(
    name='python-flask-example-applications',
    packages=['python-flask-sso-example', 'python-flask-directory-sync-example',
              'python-flask-magic-link-example', 'python-flask-mfa-example', 'python-flask-sso-example'],
    include_package_data=True,
    install_requires=['flask']
)
