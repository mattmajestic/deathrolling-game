import qrcode
img = qrcode.make('https://deathrolling-game.onrender.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("static/images/qr_code.png")