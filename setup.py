from setuptools import setup, find_packages

setup(
    name='csvIO',
    version='0.1.0',
    packages=find_packages(),
    description='Simple authentication module for CSV based user management',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='TudoHuang',
    author_email='tudohuang@gmail.com',
    url='https://github.com/tudohuang/csvIO',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
