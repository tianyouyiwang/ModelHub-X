from setuptools import setup, find_packages

setup(
    name='llama',
    version='3.0',
    description='Meta Llama: Large Language Models',
    packages=find_packages(),
    install_requires=[
        'torch>=1.13.0',
        'sentencepiece',
        'transformers>=4.31.0',
        'accelerate',
        'fire',
        'requests',
        'tiktoken',
        'blobfile',
    ],
    extras_require={
        'dev': ['pytest', 'black', 'ruff'],
        'quality': ['black', 'ruff'],
    },
)