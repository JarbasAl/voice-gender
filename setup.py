from setuptools import setup
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


BASEDIR = os.path.abspath(os.path.dirname(__file__))


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


setup(
    name='voice-gender',
    version='0.1',
    packages=['voice_gender'],
    install_requires=required('requirements.txt'),
    package_data={'': package_files('voice_gender')},
    include_package_data=True,
    url='',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='recognize gender'
)
