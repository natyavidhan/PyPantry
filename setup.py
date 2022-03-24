from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='PyPantry',
    version='0.1.0',    
    description='An API wrapper for Pantry json database',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/studiousgamer/PyPantry',
    author='Studious Gamer',
    author_email="natyavidhanbiswas10@gmail.com",
    project_urls={
        "Bug Tracker": "https://github.com/studiousgamer/PyPantry/issues",
    },
    license='MIT Licence',
    packages=['PyPantry'],
    install_requires=['requests'],

    classifiers=[
        'Intended Audience :: Database',
        'License :: OSI Approved :: MIT License',  
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
    ],
)