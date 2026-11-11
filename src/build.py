# Gera index.html a partir de template.html + logo_src.txt. Rodar na raiz: python3 src/build.py
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
t = (root/'src'/'template.html').read_text(encoding='utf-8')
logo = (root/'src'/'logo_src.txt').read_text(encoding='utf-8').strip()
(root/'index.html').write_text(t.replace('__LOGO__', logo), encoding='utf-8')
print('index.html gerado')
