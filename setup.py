from distutils.core import setup
setup(
  name = 'HyperIo',
  packages = ['HyperIo'],
  version = '0.1',
  license='MIT',
  description = 'Abstraction to Io device on raspberry pi',
  author = 'Erik Cruz Morbach',
  author_email = 'morbacherik@gmail.com',
  url = 'https://github.com/Erik-Morbach/HyperIo',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['io', 'raspberry', 'abstraction'],
  install_requires=[
          'wiringpi',
          'smbus2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
