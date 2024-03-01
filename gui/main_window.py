from PySide6 import QtCore, QtWidgets
from ui_mainwindow import Ui_CowabungaLite

from devicemanagement.device_manager import DeviceManager

tweak_tabs = [
    "Home",
    "Explore",
    "Springboard Options",
    "Apply"
]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, device_manager: DeviceManager):
        super(MainWindow, self).__init__()
        self.device_manager = device_manager
        self.ui = Ui_CowabungaLite()
        self.ui.setupUi(self)

    @QtCore.Slot()
    def refresh_devices(self):
        self.device_manager.get_devices()
        self.devices.clear()
        if len(self.device_manager.devices) == 0:
            self.devices.addItem('None')
        else:
            for device in self.device_manager.devices:
                self.devices.addItem(device.name)

    def change_selected_device(self, index):
        if len(self.device_manager.devices) > 0:
            self.device_manager.set_current_device(index=index)
        else:
            self.device_manager.set_current_device(index=None)