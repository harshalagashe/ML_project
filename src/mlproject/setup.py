from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Harshal',
    author_email='agashe.harshal@gmail.com',
    packages=find_packages(where='src'),  # 👈 tell setuptools where to find code
    package_dir={'': 'src'},              # 👈 root package dir is "src"
    install_requires=get_requirements('requirements.txt')
)