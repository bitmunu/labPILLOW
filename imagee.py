from PIL import ImageDraw, Image, ImageFilter

width, height = (map(int, input().split()))
img = Image.new('RGBA', (width, height), 'white')
idraw = ImageDraw.Draw(img)


idraw.rectangle((width/100, height/100, width * 0.5, width * 0.5), fill = 'black')
x0 = (width/100 + width * 0.5) /2
y0 = (height/100 + width * 0.5) /2
step = width/100 * 5
size = width * 0.2
idraw.ellipse( (( x0 + step, y0 ) ,
                (x0 + size + step, x0 + size)),
               fill ='#FFFFFF')
idraw.ellipse( (( x0 - size - step , y0 ) ,
                (x0 - step, x0 + size)),
               fill ='#FFFFFF')

x1, x2, x3 = x0, width * 0.5, width/100
y1, y2, y3 = size *3, y0, y0

idraw.polygon(((x1,y1), (x2, y2), (x3, y3)), fill = 'black')
img.save('canvas.png')
img.show()