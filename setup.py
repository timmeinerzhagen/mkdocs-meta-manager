from setuptools import setup, find_packages

setup(
    name='mkdocs-meta-manager',
    version='0.1.0',
    description='MkDocs plugin for managing meta tags across folders and files.',
    keywords='mkdocs meta manager',
    url='https://github.com/timmeinerzhagen/mkdocs-meta-manager/',
    author='Tim Jonas Meinerzhagen',
    author_email='tim@meinerzhagen.me',
    license='MIT',
    license_files = ('LICENSE'),
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=0.17',
        'jinja2'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'meta-manager = mkdocs_meta_manager_plugin.plugin:MetaManagerPlugin'
        ]
    }
)