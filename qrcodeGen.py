# install these two packages via pip to make the code work.
# pip install pillow
# pip install qrcode

import qrcode

input_data = "http://www.ethiotelcom.et"

def readData(fname):
    dataList = []
    with open(fname, 'r') as fd:
        for line in fd:
            dataList.append(line.strip())
            # print(line, end='')
    fd.close()
    return dataList 

# Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=7,
        border=3)
fname = "randomCodes.txt"
getData = readData(fname)
for pattern in getData:
    qr.add_data(pattern)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    qrFname = "genratedqrCode/"+"qrCode" + pattern + ".png"
    img.save(qrFname)
    #img.close()
    qr.clear()
# print(readData(fname))
