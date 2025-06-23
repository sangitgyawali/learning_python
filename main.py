# QR code generator

import qrcode

def generate_qr():
    data = input("Enter text or URL to generate QR code: ")
    filename = input("Enter filename to save (without .png): ")

    qr = qrcode.make(data)
    qr.save(f"{filename}.png")
    print(f"✅ QR Code saved as {filename}.png")

generate_qr()

