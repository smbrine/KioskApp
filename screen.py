from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl, QSize
from PyQt5.QtGui import QIcon
import requests
from PyQt5.QtGui import QPixmap

try:
    from PyQt5 import sip
except ImportError:
    import sip

url = 'https://interact.reklama145.ru/kiosk'
url = 'http://127.0.0.1:8000/kiosk'

class BrowserApp(QWidget):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView(self)
        self.browser.setUrl(QUrl(url))
        self.browser.setGeometry(0, 0, self.width(), self.height())  # Set the geometry of the browser view
        
        icon_url = "https://interact.reklama145.ru/get-img/static/resources/icons/home.png"
        response = requests.get(icon_url, verify=False)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        
        self.home_button = QPushButton(self)
        self.home_button.setIcon(QIcon(pixmap))  # Load the icon from a QPixmap
        self.home_button.setIconSize(QSize(80, 80))  # Set the icon size to be twice as large
        self.home_button.setStyleSheet("background-color: transparent; border: none;")
        self.home_button.clicked.connect(self.on_home_button_clicked)

        self.setAttribute(Qt.WA_TranslucentBackground)  # Set the background to be translucent
        
        # Connect the urlChanged signal to your custom slot
        self.browser.urlChanged.connect(self.on_url_changed)

    def on_home_button_clicked(self):
        self.browser.setUrl(QUrl(url))

    def resizeEvent(self, event):
        self.browser.setGeometry(0, 0, self.width(), self.height())  # Resize the browser view when the window is resized
        self.home_button.setGeometry(10, self.height()-90, 80, 80)  # Adjusts the button position based on the window size

    def on_url_changed(self, new_url):
        # Get the path of the URL
        path = new_url.path()
        print(path)
        # Check if the path contains 'poster/'
        if 'poster/' in path:
            # If so, replace 'poster/' with 'poster-kiosk/' and set the new path
            new_path = path.replace('poster/', 'poster-kiosk/')
            print(new_path)
            new_url.setPath(new_path)
            # Set the updated URL to navigate to it
            self.browser.setUrl(new_url)
        
if __name__ == "__main__":
    app = QApplication([])
    app_widget = BrowserApp()
    app_widget.setWindowFlags(Qt.FramelessWindowHint)  # Removes window borders
    app_widget.showFullScreen()  # Shows the widget in full screen
    app.exec_()
