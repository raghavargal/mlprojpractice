## responsible to create my ML app as a package
from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def getRequirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    ## reading the file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

  
   
setup(
    name='mlprojpractice',
    version='0.0.1',
    packages=find_packages(),
    install_requires=getRequirements('requirements.txt'),
    author='Raghav Argal',
    auther_email='raghav.argal@gmail.com'
)
