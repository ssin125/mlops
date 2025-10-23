from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filename:str) -> List[str]:
    '''
    This will return the list of requirements
    '''
    requirements = []
    with open(filename) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace('\n', '') for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlops_project',
    version='1.0.0',
    attrs='Shubham Sinha',
    author_email='shubham.sinha@goindigo.in',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
