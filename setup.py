from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
  '''
  This function will return a list of requirements
  '''
  requirements = []
  with open('requirements.txt') as file_obj:
    requiremnts = file_obj.readlines()
    requirements = [req.replace("\n", "")for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
      requirements.remove(HYPHEN_E_DOT)
      
  return requirements



setup(
name='MLPROJECTS',
version='0.0.1',
author='Gibson',
author_email='kipropgibson13@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

  
  
)