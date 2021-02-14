from setuptools import setup as setuptools_setup
from setuptools import find_packages as setuptools_find_packages


long_description = '''# Console Engine
Create Console Games (Windows ONLY!)<br />
![Lol](https://github.com/Pixelsuft/Loxa-bot/raw/main/bot_small.png?raw=true)
# ChangeLog
v0.0.3:<br />
Fixed Old Bugs
# Links
[GitHub](https://github.com/Pixelsuft/console_engine/)
'''

setuptools_setup(
    name="console_engine",
    version="0.0.3",
    author="Pixelsuft",
    description="Create Console Games (Windows ONLY!)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pixelsuft/console_engine/",
    packages=setuptools_find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.5',
    license='MIT',
    keywords='console_engine',
    install_requires=[
        'console_engine', 'wav_win_sound', 'parse_args',
        'pywin32', 'colorama', 'pyautogui', 'urllib3'
    ],
    py_modules=['console_engine']
)
