from setuptools import setup

setup(
    author='addingtong',
    author_email='addingtonglenn9@gmail.com',
    name='teaxyz-addingtong',
    version='1.0.6',
    description='A simple package for https://app.tea.xyz/. Example tea-xyz - https://github.com/addingtonglenn9/tea_xyz',
    url='https://github.com/addingtonglenn9/tea_xyz',
    project_urls={
        'Homepage': 'https://github.com/addingtonglenn9/tea_xyz',
        'Source': 'https://github.com/addingtonglenn9/tea_xyz',
    },
    py_modules=['hello_tea'],
    entry_points={
        'console_scripts': [
            'hello-tea=hello_tea:hello_tea_func'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.20.0',
        'teaxyz-addingtong',
    ],
)
