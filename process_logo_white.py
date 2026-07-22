from PIL import Image
import os

img_path = "images/logo.png"
out_path = "images/logo_branca.png"

img = Image.open(img_path).convert("RGBA")
data = img.getdata()

new_data = []

# Pega a cor do pixel do topo esquerdo para checar se o fundo é sólido
bg_color = data[0]

for item in data:
    r, g, b, a = item
    
    # Se for fundo preto sólido (caso a imagem não seja transparente), torna transparente
    if bg_color[3] == 255 and r < 10 and g < 10 and b < 10:
        new_data.append((0, 0, 0, 0))
    # Se já for transparente
    elif a < 10:
        new_data.append((0, 0, 0, 0))
    else:
        # Pinta tudo que não for transparente de branco, mantendo o canal alpha original
        # Isso garante que o texto fique branco e as bordas continuem suaves (anti-aliasing)
        new_data.append((255, 255, 255, a))

img.putdata(new_data)

# Cortar os espaços vazios (bounding box) para alinhar melhor no site
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

img.save(out_path)
print(f"Salvo com sucesso: {out_path}")
