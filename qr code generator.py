import qrcode
import os

#Data to be encoded in the QR code
data = input('enter date to change to qr code:')

#Path where you want to save the QR code image (Android/iOS Storage)
#You can specify a path like '/sdcard/' on Android or use other paths supported by mobile OS.
file_path = "/path/for/the/file/to/save/qrcode.png"# Android example path
#For iOS, use a valid path like '/var/mobile/Containers/Data/Application/...' 

#Create a QR code instance
qr = qrcode.QRCode(
    version=3,  # Size of the QR code 0-40
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=30,  # Box size of the QR code
    border=4,  # Border thickness
)

#Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

#Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

#Save the image to the specified file path
img.save(file_path)

#Optionally, you can display the image using Pillow (PIL)
img.show()

print(f"QR code saved to: {file_path}")
