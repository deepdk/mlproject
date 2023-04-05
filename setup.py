from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT = '_e .'
def get_requirements(file_path:str)->List[str:]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_DOT in get_requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements        
     

setup(
    name = "mlproject",
    version = '0.0.1',
    author = 'deepali',
    author_email='ddk.stat12@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)