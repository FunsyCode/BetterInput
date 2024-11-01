from setuptools import setup, find_packages

def readme():
  with open('README.md', encoding="utf-8") as f:
    return f.read()

setup(
  name='FlowInput',
  version='1.0.0',
  author='Funsy',
  author_email='abramovicegor842@gmail.com',
  description='This is the simplest module for improved work with input.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/FunsyCode/FlowInput',
  packages=find_packages(),
  install_requires=\
    [
    'colorama>=0.4.6', 
    'pynput>=1.7.7',
    ],
  keywords='input flowinput',
  project_urls={
    'GitHub': 'https://github.com/FunsyCode/FlowInput'
  },
  python_requires='>=3.11'
)