from setuptools import setup, find_packages

setup(
    name='platzi_ecommerce_ingestion',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'pandas',
    ],
)
