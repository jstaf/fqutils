import glob
from setuptools import setup

setup(
        name='fqutils',
        version='1.0',
        description='Several useful tools for manipulating FASTQ files.',
        url='https://github.com/jstaf/fqutils',
        author='Jeff Stafford',
        license='MIT',
        packages=['fqutils'],
        install_requires=[
            'biopython',
            'numpy'
        ],
        scripts=glob.glob('./fq-*'),
        zip_safe=False,
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
        )

