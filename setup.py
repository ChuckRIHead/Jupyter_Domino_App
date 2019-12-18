import setuptools

setuptools.setup(
    name="jupyter-codeserver-proxy",
    version='.1',
    url="",
    author="support@dominodatalab.com",
    description="",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'Domino_App = Jupyter_Domino_App:setup_app',
        ]
    },
    package_data={
        'Jupyter_Domino_App': ['icons/*'],
    },
)
