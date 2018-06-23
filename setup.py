import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="autosyntax",
	version="1.0.1",
	author="Gilad Barnea",
	author_email="gbetech@gmail.com",
	description="An emmet-like app for python. Autosyntax converts english words to full python code.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/GbeTech/autosyntax",
	packages=setuptools.find_packages(),
	install_requires=['keyboard', 'pyperclip'],
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		),
	)
