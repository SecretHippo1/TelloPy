"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['tello_qt.py']
DATA_FILES = ['mainwindow.ui']
OPTIONS = {
    'iconfile': 'wifi.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
