from setuptools import find_packages, setup #find_pachage will automatically found package used in the project
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list  of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]    ## while reading the /n will also read to erase it is replaced by space

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)   ## to remove -e . in setup.py


    return requirements

setup (
name='Mlproject',
version='0.0.1',
author='Pallavi',
author_email='pallavimohantypallu31@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')  ## calling out the all the packages need to be installed
)                                         # importing all parameters