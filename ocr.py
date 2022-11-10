import os
import easyocr
from IPython.display import Image,display
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# the path of image
image_file_path='/home/lenovo/DP/LAB3/in_class_OCR/'
filelist=os.listdir(image_file_path)
for fichier in filelist:
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
    print(f"img name: {os.path.basename(image_file_path+fichier)}") 
    display(Image(image_file_path+fichier))  
    #img = mpimg.imread(image_file_path+fichier)
    #imgplot = plt.imshow(img)
    #plt.show()    
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image_file_path+fichier,detail=0)
    print(f"OCR result: {result}")
#print(filelist)

