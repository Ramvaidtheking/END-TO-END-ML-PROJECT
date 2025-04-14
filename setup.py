## setup.py lets us to bundle our project so that koi bhi aur banda hmare projects ko install kr ske using pip
## it basically creates our project as a package
from setuptools import find_packages,setup
from typing import List


Hyphen_E_Dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #remove \n
        requirements = [req.replace("\n","")for req in requirements]
#Hume -e . ko sirf tb chalana hai jab connect krna ho finally setup aur requiements.txt ko har bari nai chalana isiliye isko ignore kro jab normally apne project run krna ho
        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)


    return requirements

setup(
    name='END-TO-END-ML-PROJECT',
    version='0.0.1',
    author='Ram',
    author_email='ramsandeepvaid@gmail.com',
    packages=find_packages(),
    # whenever this find_packages() runs it will try to find how many folders have__init__.py file
    ## jin  jin folders me hogi ye vali file vo vo folders ko ye package bna degi
    install_requires=get_requirements('requirements.txt')
    #This will install whatever is there in the requirements.txt one by one

)