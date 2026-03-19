from PIL import Image
import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.webp'):
            path = os.path.join(root, f)
            png = path.replace('.webp', '.png')
            Image.open(path).save(png)
            print(f'Convertido: {path}')

print('Conversión completada')
