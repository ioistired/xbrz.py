#!/usr/bin/env python3

import re
from setuptools import setup, Extension

with open('README.md') as f:
	long_description = f.read()

version = ''
with open('xbrz.py') as f:
	m = re.search(r"""^__version__\s*=\s*['"]([^'"]*)['"]""", f.read(), re.MULTILINE)
	if m:
		version = m.group(1)

if not version:
	raise RuntimeError('version is not set')

setup(
	name='xbrz.py',
	author='iomintz',
	author_email='io@mintz.cc',
	version=version,
	description='ctypes-based binding library for the xBRZ pixel-art image scaling algorithm',
	long_description=long_description,
	long_description_content_type='text/markdown',
	license='AGPL-3.0-or-later',
	url='https://github.com/iomintz/xbrz.py',

	py_modules=['xbrz'],
	ext_modules=[
		Extension(
			'_xbrz',
			['lib/xbrz.cpp'],
			include_dirs=['lib/'],
			extra_compile_args=['-std=gnu++17', '-g0'],
		),
	],
	extras_require={
		'wand': 'Wand>=0.6.1,<1.0.0',
		'pillow': 'Pillow>=7.1.2,<8.0.0',
	},

	classifiers=[
		'Topic :: Software Development',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: C++',
		'Topic :: Multimedia :: Graphics',
	],
)
