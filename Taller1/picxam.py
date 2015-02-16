from PIL import Image 
#from StringIO import StringIO
im=Image.open("tux.png")
##im.rotate(45).show
pix = im.load()
print pix
