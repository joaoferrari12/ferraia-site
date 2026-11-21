"""Converte as capturas do ar (PNG 2x) para site/assets/telas/*.webp.

Uso: python3 -I telas.py <pasta-das-fotos> [en|es]   (sem língua = português, sem sufixo)
"""
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
    'harbour-hound-grooming': 'harbour-and-hound',
}
# `python3 -I telas.py <pasta> en` / `es`: fotos tiradas com a interface em ingles ou em espanhol (?lang=en, ?lang=es);
# as empresas em portugues ganham o sufixo da lingua (forno-nove-en-inicio, forno-nove-es-m-quadro, porta-forno-nove-es);
# a Harbour & Hound ja e inglesa e fica sem sufixo. `pt` (ou nada) = sem sufixo.
LINGUA = sys.argv[2] if len(sys.argv) > 2 else 'pt'
if LINGUA not in ('pt', 'en', 'es'):
    sys.exit('lingua desconhecida: ' + LINGUA + ' (use pt, en ou es)')
SUFIXO = '' if LINGUA == 'pt' else '-' + LINGUA
n = 0
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.png') or '--' not in f:
        continue
    partes = f[:-4].split('--')
    if len(partes) == 2:  # porta-forno-nove--m.png (porta publica, so celular)
        nome = partes[0] + SUFIXO
        emp, tag, tela = None, 'm', None
    else:
        emp, tag, tela = partes
        emp = EMPRESA.get(emp, emp)
        suf = '' if emp == 'harbour-and-hound' else SUFIXO
        nome = f'{emp}{suf}-{tela}' if tag == 'd' else f'{emp}{suf}-m-{tela}'
    im = Image.open(os.path.join(SRC, f)).convert('RGB')
    if tag == 'd' and im.width > 1600:
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, nome + '.webp'), 'WEBP', quality=80, method=6)
    n += 1
print(n, 'telas em', OUT)
