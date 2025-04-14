from setuptools import setup, find_packages

setup(
    name="mario-mcp-personal",
    version="0.1.0",
    packages=find_packages(include=["engines*", "prompts*", "resources*", "tools*"]),
    include_package_data=True,
    install_requires=[
        "flask",
        "flasgger==0.9.7.1",
        "requests",
        # Adicione outras dependências aqui, se necessário
    ],
    entry_points={
        "console_scripts": [
            "mcp-server=tools.server:main"  # ajuste conforme o nome real do script principal
        ]
    }
)
