from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "Video Resumer",
    ext_modules = cythonize('src/main.pyx'),  # Seu arquivo .pyx
)
