from setuptools import setup, find_packages

with open('README.rst') as fin:
    readme = fin.read()

setup(
    name='nap-token-auth',
    version='0.1.2',
    description='A Minimal Token-Based Auth for Django',
    long_description=readme,
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    url='http://github.com/funkybob/nap-token-auth/',
    keywords=['django', 'token', 'auth', 'api'],
    packages = find_packages(exclude=('tests*',)),
    zip_safe=False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: Implementation :: PyPy',
    ],
    requires = [
        'Django (>=1.8)',
    ],
    install_requires = [
        'Django>=1.8',
    ],
)
