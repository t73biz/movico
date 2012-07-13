from distutils.core import setup

setup(
    name='movico',
    version='0.1.0',
    author='Ronald Chaplin',
    author_email='rchaplin@t73.biz',
    packages=['movico', 'movico.test'],
    scripts=['bin/test.py'],
    url='http://movico.t73.biz',
    license='LICENSE.txt',
    description='Python MVC',
    long_description=open('README.txt').read()
)

