# pip install pillow

from PIL import Image, ImageFilter

img = Image.open("d:\\111\\2.png")   # открыть файл
print(img.size, img.mode)       # (ширина, высота), цветовой режим
img.show()   


'''
open(filename)	Открыть изображение	img = Image.open('photo.jpg')
save(filename)	Сохранить в файл	img.save('out.png')
show()	Показать в просмотрщике	img.show()
resize((w,h))	Изменить размер	img.resize((800, 600))
crop((l,t,r,b))	Обрезать	img.crop((100, 100, 400, 300))
rotate(angle)	Повернуть	img.rotate(90)
convert(mode)	Конвертировать режим	img.convert('L') # ч/б
filter(filter)	Применить фильтр	img.filter(ImageFilter.BLUR)

'''