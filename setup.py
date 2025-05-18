from setuptools import setup, find_packages

setup(
    name="mario-mcp-personal",
    version="0.1.0",
    packages=find_packages(include=["mcp*", "engines*", "prompts*", "resources*", "tools*"]),
    include_package_data=True,
    install_requires=[
        "flask",
        "flasgger==0.9.7.1",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "mcp-server=tools.server:main"
        ]
    }
)
