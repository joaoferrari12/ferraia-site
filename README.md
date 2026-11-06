# ferraia.com — a vitrine pública do Ferra

Site estático de uma página, no ar em `https://ferraia.com` (e `www.`), publicado como Worker com static
assets na conta Cloudflare dele, **separado** do `ferra-os-web` (app.ferraia.com). Publicar aqui nunca toca o
produto no ar.

Nasceu em 06/11/2026 de uma medição: `ferraia.com` não atendia nada e `app.ferraia.com` era só o card de login,
sem uma frase sobre o produto. Quem clicava no link do currículo não via nada. Contexto e decisões:
`../FERRA-IA/knowledge-base/brand/A-MARCA.md` (a marca) e `../brainstorms/2026-11-06-vitrine-publica-do-ferra.md`.

## O que tem

- `site/index.html` — a página inteira (CSS e JS embutidos). Bilíngue: português se o navegador for `pt*`, inglês
  caso contrário, com botão PT/EN que lembra a escolha (`localStorage`). Textos nos pares `<span lang-block="pt">` /
  `<span lang-block="en">`; a seção "O produto" lê o vetor `TABS` do script no fim do arquivo.
- `site/assets/telas/*.webp` — capturas **do ar**, das vitrines (negócios fictícios, ADR-186), tiradas em
  06/11/2026 pelo `ferra-os-web/.tmp/vitrine-ar.mjs` (Chrome com janela, ele faz o login, o script anda e fotografa);
  as portas públicas (`/p/<link>`) pelo `vitrine-porta.mjs`, sem login. Nome: `<empresa>-<tela>.webp`, `-m-` = celular.
- `site/assets/` — ícone do app (cavalo no ladrilho vermelho, do handoff da marca de 15/09), favicon igual ao do
  app, `og-image.png` (a mesma do ADR-207), `cavalo.png` do hero do handoff.
- `wrangler.jsonc` — nome `ferraia-site`, rotas `ferraia.com` e `www.ferraia.com` com `custom_domain: true`.

## Forma

A forma é a do site de marketing do pacote de marca (`FERRA-IA/knowledge-base/brand/handoff-2026-09-15/FERA
Website.dc.html`): fundo `#08080A`, Montserrat 900 em caixa alta, rótulos em IBM Plex Mono, vermelho `#E11D2E`
como único acento, sem canto arredondado, grades de 1 px. **O nome é Ferra** (decisão dele de 03/10/2026), não FERA:
o pacote entra pela forma, não pelo nome.

## Publicar

De dentro do `ferra-os-web` (que tem o `wrangler` instalado e logado por OAuth):

```powershell
cd C:\Users\jones\projetos\ferra-os-web
npx wrangler deploy --config ..\ferraia-site\wrangler.jsonc
```

Conferir com os olhos depois: `https://ferraia.com` em pt e en, a 390 e a 1366.

## Números que a página afirma (medidos em 06/11/2026; atualizar quando mudarem)

| número | de onde |
|---|---|
| 208 ADRs | `ls FERRA-IA/docs/adr/ADR-*.md` |
| 133 migrações | `ls ferra-os/supabase/migrations/*.sql` |
| 298 arquivos de teste | 179 `*.test.ts(x)` em `ferra-os-web/src` + 119 `tela/*.spec.ts` |
| 1.475 commits | `git log --oneline \| wc -l` em ferra-os-web (500) + ferra-os (262) + FERRA-IA (713) |
| 7 vitrines vivas | `ferra-os/supabase/demo/README.md`, `app.showcase_tick` (ADR-185/186) |
