from typing import List
from setuptools import setup, find_packages


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #As reading the file we will be getting the "\n" as delimiter,
        #so we have to remove it with a blank
        #using list comprehension
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


#metadata
setup(
    name="mlproject",
    version="0.0.1",
    author="Vishal Kumar",
    author_email="vishalprasad7851@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)