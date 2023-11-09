python -m venv venv
venv\Scripts\activate.bat
pip install PyQt5 PyQt5-sip PyQtWebEngine pyinstaller requests
pyinstaller -F --windowed --paths=venv\Lib\site-packages screen.py