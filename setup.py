from setuptools import setup

setup(
    name="lnxsum",
    version="1.0.0",
    description="LNX-256: The Uncrackable Sequential Hasher",
    author="Anagh Barnwal",
    packages=["lnxsum"],
    entry_points={
        'console_scripts': [
            'lnxsum=lnxsum.lnxsum:main',
        ],
    },
)
