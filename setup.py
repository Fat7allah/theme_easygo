from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tekton_theme/__init__.py
from theme_easygo import __version__ as version

setup(
	name="theme_easygo",
	version=version,
	description="Corporate Theme for Frappe",
	author="Blazie-cpu&Farhan",
	author_email="",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
