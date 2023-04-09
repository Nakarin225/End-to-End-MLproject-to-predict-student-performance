from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = "-e ."
def get_requirments(file_path:str)->List[str]:
    """
    this function will return the lisg of requirments
    """
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    return requirments




setup(
name='MLproject',
version='0.0.1',
author="Nakarin",
author_email='rocdmax@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirement.txt')
)