from setuptools import setup

setup(
    name='VideoToolBox',
    version='1.1.0',    
    description='A video processing package',
    url='https://github.com/nsgil85/VideoToolBox',
    author='Gil h',
    author_email='nsgil85@gmail.com',
    license='BSD 2-clause',
    packages=['VideoToolBox'],
    install_requires=['numpy'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        #'Operating System :: POSIX :: Linux',        
        'Operating System :: POSIX :: Windows',        
        'Programming Language :: Python :: 3.7',
        #'Programming Language :: Python :: 3.8',
    ],
)