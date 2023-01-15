from PyQt5 import QtBluetooth, QtCore



localDevice = QtBluetooth.QBluetoothLocalDevice()

# Check if Bluetooth is available on this device
if localDevice.isValid():
    # Turn Bluetooth on
    localDevice.powerOn()
    # Read local device name
    localDeviceName = localDevice.name()
    # Make it visible to others
    localDevice.setHostMode(QtBluetooth.QBluetoothLocalDevice.HostDiscoverable)
    # Get connected devices


print(localDeviceName)
    