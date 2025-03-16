# QR CODER

'''
Create a program that converts the input entered by the user into a QR code that can be scanned by a QR reader.
To achieve this program we must use libraries that allow the generation of QR codes (qrcode for example).
The program can also offer the user the option to save or copy the generated QR code to the clipboard.

'''

import qrcode
from PIL import Image
import pyperclip

def generate_qr(data, filename="qrcode.png"):
    """Generates a QR code from user input and saves it as an image."""
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR grid
        border=4  # Border size around the QR code
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)  # Save the QR code as an image
    print(f"✅ QR code saved as {filename}")

    return img

def copy_to_clipboard(data):
    """Copies the QR code data (URL or text) to the clipboard."""
    pyperclip.copy(data)
    print("📋 Data copied to clipboard!")

def main():
    print("📌 QR Code Generator 📌")
    user_input = input("Enter the text or URL to encode: ")

    # Generate and save the QR code
    qr_image = generate_qr(user_input)

    # Show the QR code image
    qr_image.show()

    # Ask the user if they want to copy the text to clipboard
    copy_choice = input("Do you want to copy the text to clipboard? (yes/no): ").strip().lower()
    if copy_choice in ["yes", "y"]:
        copy_to_clipboard(user_input)

if __name__ == "__main__":
    main()
