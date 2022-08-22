import qrcode as qr
img = qr.make("https://www.amritpanta.com.np/")
img.save('newqr.png')
