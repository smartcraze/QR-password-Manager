import qrcode
import os

def generate_qr_code(platform ,username, password, customize=False, bg_color=None, file_name=None):
    data = f"Platform: {platform}\nUsername: {username}\nPassword: {password}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    if customize:
        img = qr.make_image(fill_color='black', back_color=bg_color)
    else:
        img = qr.make_image(fill_color='black', back_color='white')
    
    if file_name:
        img_file_name = f"{file_name}.png"
    else:
        img_file_name = "qr_code.png"
    
    img_path = os.path.join(os.getcwd(), img_file_name)
    img.save(img_path)
    print(f"The QR code has been saved as '{img_file_name}' in the directory.")
    print("Thanks for using Our QR Code Service.\n")
    print("Follow My github for more Such Projects.")

    return img_path

if __name__ == "__main__":
    platform = input("Enter the platform: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    
    customize = input("Do you want to customize the QR code background color? (yes/no): ").lower()
    
    if customize == 'yes':
        bg_color = input("Enter the background color: ")
    else:
        bg_color = None

    file_name = input("Enter the file name to save the QR code (without extension): ")

    qr_image_path = generate_qr_code(platform , username, password, customize=(customize == 'yes'), bg_color=bg_color, file_name=file_name)
