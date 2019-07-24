try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

config = {
	'description': 'Game for lab1',
	'author': 'EMILY SIMON',
	'url': 'https://github.com/emilybsimon/CAAP-CS.git',
	'download_url': 'https://github.com/emilybsimon/CAAP-CS.git',
	'author_email': 'emilysimon@uchicago.edu',
	'version': '0.1',
	'install_requires': ['nose', 'pyinstaller'],
	'packages': ['game'],
	'scripts': [],
	'name': 'my_game'
}

setup(**config)
