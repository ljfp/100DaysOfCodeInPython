''''
QR Code Generator.
With this CLI you can generate QR codes in PNG format.
Just type the text you want to encode and the filename.
The program will generate a PNG image with the QR encoding
of your text, in the directory where you run the script.
'''
import qrcode


def cli():
    '''
    This is just a wrapper for generate().
    If you execute this file, you will be presented with
    this CLI, and you can use it from you shell.
    '''
    print("Welcome to the QR code generator!")
    data = input("Insert the text you want to encode: \n")
    filename = input("Write the name of the file: \n")

    generate(data, filename)


def generate(data, filename):
    '''
    This function will generate the QR code given data and a filename.
    '''
    qr_code = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,)

    qr_code.add_data(data)
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save(f"{filename}.png")


if __name__ == "__main__":
    cli()
