from setuptools import setup, find_packages

setup(
    name='accelerate',
    version='0.27.0',
    description='Accelerate training and inference of PyTorch models',
    packages=find_packages(),
    install_requires=[
        'torch>=1.10.0',
        'pyyaml',
        'numpy',
        'packaging>=20.0',
    ],
    extras_require={
        'dev': ['pytest', 'black', 'ruff'],
        'quality': ['black', 'ruff'],
        'docs': ['sphinx', 'sphinx_rtd_theme'],
    },
)