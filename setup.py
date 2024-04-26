from setuptools import setup, find_packages

setup(
    name='dust_SED_submm',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.20.3',
        'matplotlib==3.4.2',
        'seaborn==0.11.1',
        'astropy==4.3.1',
        'git+https://github.com/aayush3009/show_emlines'
    ],
    author='Aayush Saxena',
    author_email='aayush.saxena@physics.ox.ac.uk',
    description='A Python script for building simple dust SEDs for galaxies.',
    url='https://github.com/aayush3009/dust_SED_submm',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
