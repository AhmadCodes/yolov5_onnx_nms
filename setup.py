#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Ahmad Ali",
    author_email='amdali97@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Add nms to onnx exported model of yolov5",
    entry_points={
        'console_scripts': [
            'yolov5_onnx_nms=yolov5_onnx_nms.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='yolov5_onnx_nms',
    name='yolov5_onnx_nms',
    packages=find_packages(include=['yolov5_onnx_nms', 'yolov5_onnx_nms.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AhmadCodes/yolov5_onnx_nms',
    version='0.1.0',
    zip_safe=False,
)
