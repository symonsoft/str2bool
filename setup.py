from distutils.core import setup

version = "1.2"

setup(
    name='str2bool',
    packages=['str2bool'],
    version=version,
    description='Convert string to boolean',
    author='SymonSoft',
    author_email='symonsoft@gmail.com',
    url='https://github.com/symonsoft/str2bool',
    download_url="https://github.com/symonsoft/str2bool/tarball/{0}".format(version),
    keywords=['str2bool', 'bool', 'boolean', 'convert', 'yes', 'no', 'true', 'false', 'enabled', 'disabled'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
    ],
)
