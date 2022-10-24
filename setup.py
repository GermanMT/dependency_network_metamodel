import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'dn_metamodel',
    version = '1.1.0',
    author = 'Antonio Germán Márquez Trujillo',
    author_email = 'amtrujillo@us.es',
    description = 'This repo host the dependency network model concrete classes',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/GermanMT/dependency_network_metamodel',
    packages = setuptools.find_namespace_packages(include=['flamapy.*']),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.10',
    install_requires = [
        'famapy>=1.0.0'
    ],
    tests_requires = [
        'prospector[with_everything]==1.7.7',
        'mypy==0.982',
        'types-setuptools==65.4.0'
    ]
)