"""Converte as capturas do ar (PNG 2x) para site/assets/telas/*.webp. Uso: python3 -I telas.py <pasta-das-fotos>"""
import sys, os
from PIL import Image

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site', 'assets', 'telas')
os.makedirs(OUT, exist_ok=True)
EMPRESA = {
    'pizzaria-forno-nove': 'forno-nove',
    'patas-cia-pet-shop': 'patas-e-cia',
    'jangada-azul-bar-e-deposito': 'jangada-azul',
    'barbearia-baia-de-espuma': 'baia-de-espuma',
}
n = 0
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.png') or '--' not in f:
        continue
    emp, tag, tela = f[:-4].split('--')
    emp = EMPRESA.get(emp, emp)
    nome = f'{emp}-{tela}' if tag == 'd' else f'{emp}-m-{tela}'
    im = Image.open(os.path.join(SRC, f)).convert('RGB')
    if tag == 'd' and im.width > 1600:
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, nome + '.webp'), 'WEBP', quality=80, method=6)
    n += 1
print(n, 'telas em', OUT)
