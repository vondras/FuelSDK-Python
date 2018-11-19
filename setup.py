from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    version='1.1.1',
    name='Salesforce-FuelSDK',
    description='Salesforce Marketing Cloud Fuel SDK for Python',
    long_description=readme,
    author='ExactTarget',
    py_modules=['ET_Client'],
    packages=['FuelSDK'],
    url='https://github.com/salesforce-marketingcloud/FuelSDK-Python',
    license='MIT',
    install_requires=[
        'pyjwt>=1.5.3',
        'requests>=2.18.4',
        'suds-jurko==0.6',
        'suds-requests==0.4.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.3',
    ],
)