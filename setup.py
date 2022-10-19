from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    pass

    #requirement_list:List[str] = []
    #with open("requirements.txt") as f:
     #   for line in f:
      #      requirement_list.append(str(line).strip())
       # f.close()
    #print(requirement_list)
    #return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="dayanand",
    author_email="dayanand_87@yahoo.co.in",
    packages=find_packages(),
    install_requires = ["pymongo==4.2.0"]
    #get_requirements()
)