from setuptools import setup

setup(
    name='manager-api',
    description='Publishes your Lektor site to Google App Engine.',
    url='https://github.com/isotherm/python-manager-api/',
    version='0.1',
    author=u'Kirk Meyer',
    author_email='kirk.meyer@alpaxo.com',
    license='MIT',
    platforms='any',
    packages=[
        'manager_api'
    ],
    install_requires=[
        'pydantic',
        'uplink',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
