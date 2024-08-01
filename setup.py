from setuptools import setup, find_packages

setup(
    name="llm_generate",
    version="0.1.0",
    author="Asma Houimli",
    author_email="asma.houimli@etudiant-fst.utm.tn",
    description="A package for interacting with LLama3 models.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
        classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
        install_requires=[
        "ollama",
        "fpdf", 
    ],
        entry_points={
        'console_scripts': [
            'll_model=way_llm_model.cli:main',
        ],
    }

)