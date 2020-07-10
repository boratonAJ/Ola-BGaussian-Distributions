from setuptools import setup

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

with open("README.md", 'r') as f:
    long_description = f.read()

    
setup(
    name='Ola-Bino-Gaussian-Distributions',
    version='0.1',
    description='This is Binomial and Gaussian Distributions Package',
    author='Ajayi Olabode Oluwaseun',
    author_email='boraton2010@gmail.com',
    url='https://github.com/boratonAJ/SNPs_Analysis',
    license='LICENSE.txt',
    keywords = "Binomial Gaussian Distribution Probability Histogram BarChart",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
    install_requires=[
        "python_version == 3.0",
        "matplotlib == 3.2.2",
    ],
    zip_safe = False,
    include_package_data = True,
    packages=['distributions'],
    long_description = """\
Universal character encoding detector
-------------------------------------
Detects
 - ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
 - Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
 - EUC-JP, SHIFT_JIS, ISO-2022-JP (Japanese)
 - EUC-KR, ISO-2022-KR (Korean)
 - KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
 - ISO-8859-2, windows-1250 (Hungarian)
 - ISO-8859-5, windows-1251 (Bulgarian)
 - windows-1252 (English)
 - ISO-8859-7, windows-1253 (Greek)
 - ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
 - TIS-620 (Thai)
This version requires Python 3 or later; a Python 2 version is available separately.
"""
)