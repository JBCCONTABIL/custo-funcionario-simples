# Custo de Funcionário no Simples Nacional — JBC Assessoria Contábil

Simulador para o cliente: quanto custa contratar um funcionário CLT (ou jovem aprendiz) em empresa do Simples Nacional, com 13º, férias, FGTS, INSS patronal e RAT do Anexo IV, benefícios e reserva para demissão.

Publicado em https://jbccontabil.github.io/custo-funcionario-simples/

## Como manter
Fonte em `src/template.html` (logo em `src/logo_src.txt`). Depois de editar, rode na raiz:

    python3 src/build.py

para regerar o `index.html`. Valores que mudam todo ano: `SALARIO_MINIMO` no script e o texto do rodapé.
