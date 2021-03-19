from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
  readme = f.read()

setup(
    name='hr',
    version='1.0.0',
    author='brahami rabah',
    author_email='brahamirabah8@gmail.com',
    description="A utility to export a system's user information into formats that can be used .",
    long_desription=readme,
    long_description_content_type='test/markdown',
    url='http://github.com/brahamirabah/hr',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'hr=hr.cli:main',
    }
)
