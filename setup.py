from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of our README file for PyPi
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Please make sure to cap all dependency versions, in order to avoid unwanted
# functional and integration breaks caused by external code updates.

general_requirements = [
    "policyengine-core",
    "numpy",
]

dev_requirements = [
    "black",
    "coverage",
    "jupyter-book",
    "plotly",
    "pytest",
    "setuptools",
    "wheel",
    "yaml-changelog>=0.1.7",
    "linecheck",
    "furo<2023",
    "markupsafe==2.0.1",
    "sphinx>=4.5.0,<5",
    "sphinx-argparse>=0.3.2,<1",
    "sphinx-math-dollar>=1.2.1,<2",
]

setup(
    name="policyengine-ng",
    version="0.4.2",
    author="PolicyEngine",
    author_email="hello@policyengine.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    description="Core microsimulation engine enabling country-specific policy models.",
    keywords="tax benefit microsimulation framework",
    license="https://www.fsf.org/licensing/licenses/agpl-3.0.html",
    license_files=("LICENSE",),
    url="https://github.com/policyengine/policyengine-core",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "policyengine-core=policyengine_core.scripts.policyengine_command:main",
        ],
    },
    extras_require={
        "dev": dev_requirements,
    },
    include_package_data=True,  # Will read MANIFEST.in
    install_requires=general_requirements,
    packages=find_packages(exclude=["tests*"]),
)
