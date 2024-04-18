# setuptools

from setuptools import setup, find_packages # (em caso de sub pacotes)

setup(
    name="dundie_alss",
    #        x.y.z 
    version="0.1.0",
    #        | | | > PATCH 
    #        | | >>  MINOR
    #        | >>>>  MAJOR
    description="Reward Point System for Dunder Mifflin",
    author="Alberto Luiz",
    packages=find_packages(),
)

# pyproject

# external build tools (Poetry , Flit)