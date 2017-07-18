import setuptools

setuptools.setup(
    name="anyprint",
    version="0.1.0",
    url="https://github.com/kragniz/anyprint",

    author="Louis Taylor",
    author_email="louis@kragniz.eu",

    description="Use any language's print statements in Python",
    long_description=open('README.md').read(),

    py_modules=['anyprint'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
