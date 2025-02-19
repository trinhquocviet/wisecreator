from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

def install_nltk_data():
    import nltk
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('averaged_perceptron_tagger_eng')

class PostDevelopCommand(develop):
    def run(self):
        install_nltk_data()
        develop.run(self)

class PostInstallCommand(install):
    def run(self):
        install_nltk_data()
        install.run(self)

setup(
    name='wisecreator',
    version='1.0.0',
    python_requires='>=3.13',
    author='Timofey Milovanov',
    packages=['wisecreator'],
    package_data={
        'wisecreator':['data/*', 'third_party/*']
    },
    install_requires=[
        'nltk==3.9.1',
        'cursor==1.3.4',
        'six==1.17.0',
        'dataclasses',
    ],
    setup_requires=[
        'nltk==3.9.1',
    ],
    cmdclass={
      'install': PostInstallCommand,
      'develop': PostDevelopCommand,
    },
    entry_points={
        'console_scripts': [
            'wisecreator = wisecreator.main:main',
        ],
    },
)