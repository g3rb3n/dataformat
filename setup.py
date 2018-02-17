from setuptools import setup

long_description = 'Simple format check and cleanup utility for web API servers'
setup(name='dataformat',
    version='0.1.0',
    description='Simple format check and cleanup utility',
    long_description=long_description,
    url='http://github.com/g3rb3n/pyformat',
    author='Gerben van Eerten',
    author_email='gerben@eerten.com',
    license='MIT',
    packages=['dataformat'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='development',
    python_requires='>=3',
)
