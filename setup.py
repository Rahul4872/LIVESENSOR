from setuptools import find_packages,setup
#from typing import List

def get_requirements() -> list[str]:
    
    requirements_list = list[str] = []
    
    return  requirements_list


setup(
    
    name='Sensor',
    version='0.0.1',
    author='Rahul',
    author_email='rahul123@gmail.com',
    packages =  find_packages(), # list of all python modules/packages in the directory
    install_requires = get_requirements(),
)