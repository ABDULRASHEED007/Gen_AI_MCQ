from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Abdul Rasheed',
    author_email='mdabdulrasheed007@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2'
    ],
)