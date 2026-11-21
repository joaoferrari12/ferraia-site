# oisocia.com.br — a vitrine pública da Sócia

Site estático de uma página, no ar em `https://oisocia.com.br` (e `www.`), publicado como Worker com static
assets na conta Cloudflare dele, **separado** do `ferra-os-web` (`app.oisocia.com.br`). Publicar aqui nunca toca o
produto no ar. `ferraia.com` e `www.ferraia.com` continuam presos a este Worker só para a Redirect Rule da zona
levar ao endereço novo (301, ADR-210; conferido em 21/11/2026). A pasta e o repositório mantêm o nome técnico
`ferraia-site`, e a chave do `localStorage` continua `ferra-site.lang` (trocar faria quem já escolheu perder a escolha).

Nasceu em 06/11/2026 de uma medição: o domínio não atendia nada e o app era só o card de login, sem uma frase
sobre o produto. Quem clicava no link do currículo não via nada. Contexto e decisões:
`../FERRA-IA/knowledge-base/brand/A-MARCA.md` (a marca), `../brainstorms/2026-11-06-vitrine-publica-do-ferra.md`
e a ADR-210 (o nome Sócia, o verde, o endereço novo).

## O que tem

- `site/index.html` — a página inteira (CSS e JS embutidos). **Três línguas, as mesmas do app** (ADR-159):
  português, inglês e espanhol, com o seletor PT · EN · ES na ordem do `SeletorDeIdioma` do app. A escolha, na
  ordem do `ferra-os-web/src/features/idioma/idioma.ts`: `?lang=pt|en|es` na URL → o que a pessoa escolheu
  (`localStorage`) → o navegador (`pt*` → pt, `es*` → es, **o resto → en**; o app, no mesmo ponto, cai em pt).
  Textos nos trios `<span lang-block="pt">` / `"en"` / `"es"`, sempre os três, lado a lado (78 por língua, mais o
  número de commits); a seção "O produto" lê o vetor `TABS` do script no fim do arquivo, com `pt`, `en` e `es`.
  Os links para o app (Entrar e as lojas de exemplo) saem com `?lang=` da língua da página.
  O espanhol usa os termos do dicionário do app (`ferra-os-web/public/idioma/es.json`): tablero, caja, stock,
  agenda, fiado, reparto, carta, envase, retiro, refuerzo, mostrador. O inglês idem (`en.json`): board, cash,
  stock, schedule, store credit, staff, cash drop, top-up, collected.
- `site/404.html` — a mesma escolha de língua, nas três.
- `site/sitemap.xml` e os `hreflang` do `<head>` — uma URL só (`/`), com os alternates `/?lang=pt|en|es`.
  As metas estáticas (`title`, `description`, `og:`) são em português: quem lê sem rodar o script vê pt.
- `site/assets/telas/*.webp` — capturas **do ar**, das vitrines (negócios fictícios, ADR-186). As 61 que a página
  usa foram refeitas em **21/11/2026, depois do molde** (ADR-211: a pílula com a Estrela, "Pergunte à Sócia ou
  pesquise", o cartão "Achado da Sócia"), **nas três línguas**: 20 em português, 21 em inglês, 20 em espanhol.
  O script é o `.tmp-sessao/molde/capturas-socia.mjs` (cópia adaptada do `vitrine/scripts/vitrine-socia.mjs`): roda
  de dentro do `ferra-os-web`, com o login guardado por `guardar-senha-vitrine.ps1`, entra em
  `app.oisocia.com.br/?lang=<lingua>` (o `?lang=` fica guardado no navegador e manda mais que a língua da empresa),
  espera a tela parada (sem esqueleto, animações finitas terminadas), recarrega se a consulta estourar o tempo e só lê.
  Sai em `.tmp-sessao/molde/capturas/socia-pt`, `socia-en` e `socia-es`; as duas portas públicas (`/p/<link>`, sem
  login, na língua do aparelho) saem do mesmo script.

  ```powershell
  cd C:\Users\jones\projetos\ferra-os-web
  $env:NODE_ENV='development'; node ..\.tmp-sessao\molde\capturas-socia.mjs            # tudo
  $env:NODE_ENV='development'; node ..\.tmp-sessao\molde\capturas-socia.mjs pt,es "pizzaria-forno-nove"   # só um pedaço (expressão regular sobre <lingua>/<arquivo>)
  ```

  Nome: `<empresa>-<tela>.webp`, `-m-` = celular. Conversão (precisa do Pillow; na máquina dele está no Python da VM
  Linux, não no do Windows): `python3 -I telas.py <pasta>` (pt), `python3 -I telas.py <pasta> en` e
  `python3 -I telas.py <pasta> es`.
  **Cada língua tem as telas dela**: em inglês, `harbour-and-hound-*` é a demo Harbour & Hound Grooming
  (en · CAD · Vancouver) e `<empresa>-en-*` / `porta-*-en` são as vitrines com a interface em inglês; em espanhol,
  `<empresa>-es-*` / `porta-*-es` são as mesmas lojas e rotas do português com a interface em espanhol (`?lang=es`).
  A página troca por `data-pt` / `data-en` / `data-es` e por `TABS[].img` / `.phone`.
  ⚠️ **A pizzaria abre às 18h de Salvador**: antes disso o Início e o Quadro dela saem vazios ("Nada fechado ainda").
  Fotografar depois das 19h30 de lá (as de 21/11 são das 19h50: R$ 277,40 vendidos, 6 pedidos abertos).
  ⚠️ O texto que descreve tela (legendas do trio, `alt` da captura do topo, `TABS`) cita o que a captura mostra
  (o "Achado da Sócia", a Coca-Cola 2 L que vai acabar; a legenda NÃO cita a data, que envelhece em dias, a ração do pet shop): **refez a captura, releia o texto**.
  O `telas.py` converte tudo o que está na pasta; o script também fotografa o Início da barbearia no celular, que a
  página não usa (`baia-de-espuma-m-inicio`, `-es-m-inicio`): apagar depois de converter.
  Sobras sem uso na página, de 06/11 (marca antiga), esperando a decisão dele: 15 `telas/*.webp`
  (`forno-nove-agenda`, `-balcao`, `-clientes`, `-entregas`, `-mesas`, `-m-mesas`, `-relatorios`,
  `baia-de-espuma-quadro`, `jangada-azul-inicio`, `-quadro`, `patas-e-cia-agenda`, `-clientes`, `-m-agenda`,
  `-m-inicio`, `-quadro`), `cavalo.png` e `emblema-branco.svg`.
- `site/assets/` — `icone.svg` e `favicon-app.svg` (a Estrela no ladrilho verde, ADR-210), `estrela.svg` e
  `estrela-branca.svg`, `apple-touch-icon.png`, `og-image.png` (Sócia, "A sócia que não divide o lucro").
- `site/_headers` — cabeçalhos de segurança (17/11/2026): os do app (ADR-154) menos a CSP, que espera medir o CSS e o JS embutidos.
- `wrangler.jsonc` — nome `ferraia-site`, rotas `oisocia.com.br`, `www.oisocia.com.br`, `ferraia.com` e
  `www.ferraia.com`, todas com `custom_domain: true`.
- Contato: WhatsApp +1 604 725-1622 (decisão dele, 06/11) na faixa `#contato` e no rodapé. E-mail
  **`contato@ferraia.com`** (decisão dele, 17/11) na faixa, em "Seus direitos" e no rodapé: Email Routing da
  Cloudflare na zona `ferraia.com` encaminha para o Gmail dele. **O e-mail continua no domínio antigo de propósito:**
  em 21/11/2026 `oisocia.com.br` tinha MX nulo e SPF `-all` (não recebe e-mail; só `send.oisocia.com.br` envia, pelo
  Resend). Trocar para `contato@oisocia.com.br` só depois de criar a rota lá.

## Forma

Fundo `#08080A`, Montserrat 900 em caixa alta, rótulos em IBM Plex Mono, **verde `#19C37D`** como acento (faixas em
verde fundo `#0E7A50`), ouro `#F2A900` na palavra marcada do título, sem canto arredondado, grades de 1 px. A forma
veio do site de marketing do pacote de marca de 15/09 (`FERRA-IA/knowledge-base/brand/handoff-2026-09-15/`); o
vermelho `#E11D2E` e o cavalo saíram na ADR-210. **O nome é Sócia** (ADR-210, 19/11/2026; antes Ferra).
A prévia do molde (cantos arredondados, alvos de 44 px, a Estrela viva) está no branch `molde-vitrine`, esperando o
sim dele; no `main` os botões do seletor de idioma têm 36 × 33 px.

## Publicar

De dentro do `ferra-os-web` (que tem o `wrangler` instalado e logado por OAuth):

```powershell
cd C:\Users\jones\projetos\ferra-os-web
npx wrangler deploy --config ..\ferraia-site\wrangler.jsonc
```

Conferir com os olhos depois: `https://oisocia.com.br` em pt, en e es, a 360 e a 1366.

Este repositório não tem verificador próprio. A medida de 21/11/2026 (as três línguas a 320, 360 e 1366: nenhum
bloco de outra língua visível, os três conjuntos com o mesmo número de blocos, nenhuma rolagem lateral, o seletor
marcando a língua certa, a escolha sobrevivendo ao recarregar, os links do app com `?lang=`) saiu do
`.tmp-sessao/molde/verifica-vitrine-es.mjs`, com o Playwright do `ferra-os-web`. Com as capturas novas, a cópia
`verifica-vitrine-capturas.mjs` deu 356 medidas, 0 falhas (nenhuma imagem quebrada, nenhum arquivo pedido e não achado).

## Números que a página afirma (medidos em 06/11/2026, remedidos em 17/11, 18/11 e 21/11/2026; atualizar quando mudarem)

| número | de onde |
|---|---|
| 212 ADRs | `ls FERRA-IA/docs/adr/ADR-*.md` (ADR-000 a ADR-211) |
| 142 migrações | `ls ferra-os/supabase/migrations/*.sql` |
| 330 arquivos de teste | 205 `*.test.ts(x)` em `ferra-os-web/src` + 125 `tela/*.spec.ts` |
| 1.542 commits | `git log --oneline \| wc -l` em ferra-os-web (516) + ferra-os (271) + FERRA-IA (755) |
| 7 vitrines vivas | `ferra-os/supabase/demo/README.md`, `app.showcase_tick` (ADR-185/186); os sete `/p/<link>` responderam no ar em 21/11/2026 |
