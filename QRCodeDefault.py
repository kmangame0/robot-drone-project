from sys import argv
import zbar
import Image

scanner = zbar.ImageScanner()
scanner.parse_config('enable')
pil = Image.open('img.png').convert('L')
width, height = pil.size
raw = pil.tostring()

image = zbar.Image(width, height, 'Y800', raw)
scanner.scan(image)

for symbol in image:
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

sym = iter(image).next()
print sym.location
print sym.location[1][1]
