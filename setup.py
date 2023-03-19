
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    '''
    ##Read the requirements file and return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.1.0',
    author='GerardoMayel',
    author_email='geramfernandez@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'scikit-learn', 'click',
    #                  'joblib', 'numpy', 'seaborn', 'matplotlib']
    install_requires=get_requirements('requirements.txt'),
)
