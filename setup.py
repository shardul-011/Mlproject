from setuptools import find_packages, setup
from typing import List

HYPER_E_VALUE= '-e .'
def get_requirements(file_path:str) -> List [str]:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace('\n'," ") for req in requirements]
        
        if HYPER_E_VALUE in requirements:
            requirements.remove(HYPER_E_VALUE)
    return requirements

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    author='Shardul',
    author_email='singhshardul64@gmail.com',
    description='My Python package',
    install_requires=get_requirements('requirements.txt'),
    
    
    
    
)