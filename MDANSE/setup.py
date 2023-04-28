import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='MDANSE',
    author='Maciej Bartkowiak',
    author_email='maciej.bartkowiak@stfc.ac.uk',
    description='MDANSE Core package - Molecular Dynamics trajectory handling and analysis code',
    keywords='molecular dynamics, science, simulation, analysis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.isis.stfc.ac.uk/Pages/MDANSEproject.aspx',
    project_urls={
        'Documentation': 'https://mdanse.readthedocs.io/en/latest/',
        'Bug Reports':
        'https://github.com/ISISNeutronMuon/MDANSE/issues',
        'Source Code': 'https://github.com/ISISNeutronMuon/MDANSE',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 4 - Beta',

        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
