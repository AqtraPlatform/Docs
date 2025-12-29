# Começando

> Um ponto de entrada estruturado para novatos no Aqtra. Tom técnico. Esta página vincula documentação, tutoriais, vídeos (com transcrições) e um exemplo executável para formar um roteiro de aprendizado progressivo.

---

## O que é o Aqtra?

Aqtra é uma **plataforma low-code** para construir aplicações empresariais principalmente através de uma interface visual, com **scripting em Python** opcional para lógica avançada. Este modelo híbrido acelera a entrega para iniciantes e permite que desenvolvedores estendam e personalizem quando necessário.

**Você aprenderá a:**

- Instalar e executar o Aqtra (nuvem ou local via Docker).
- Construir uma primeira funcionalidade de ponta a ponta (modelo de dados → componente de UI → fluxo de dados → publicar).
- Usar scripts em Python onde apropriado.
- Integrar com serviços externos e APIs.

> **Público-alvo:** desenvolvedores cidadãos, desenvolvedores front‑/back‑end juniores, analistas, arquitetos, líderes de equipe.

**CTAs principais:**

- **Comece em 60 minutos →** Passo a passo da primeira funcionalidade (veja [4) Primeira vitória](#4-first-win-in-60-minutes))
- **Documentação →** [https://docs.aqtra.io/](https://docs.aqtra.io/pt/)
- **Trilha de vídeo →** [https://www.youtube.com/@Aqtra.Academy](https://www.youtube.com/@Aqtra.Academy)

**Links rápidos (cartões):**

- **Instalar** → [5) Instalar & Acessar](#5-install--access) (Nuvem / Docker)
- **Construa sua primeira tela (Fatura)** → [4) Primeira vitória](#4-first-win-in-60-minutes)
- **Noções básicas de DataFlow** → [2) Roteiro de aprendizado passo a passo](#2-stepbystep-learning-path-single-track)
- **Publicar na web** → [2) Roteiro de aprendizado passo a passo](#2-stepbystep-learning-path-single-track)

**Nesta página**

- [1) Metodologia — como usar este guia](#1-methodology--how-to-use-this-guide)
- [2) Roteiro de aprendizado passo a passo](#2-stepbystep-learning-path-single-track)
- [3) Tutoriais & Links Cruzados de Documentação](#tutorials-documentation-cross-links)
- [4) Primeira vitória em ~60 minutos](#4-first-win-in-60-minutes)
- [5) Instalar & Acessar](#5-install--access)
- [6) Conceitos Básicos (Glossário do Aqtra)](#6-core-concepts-aqtra-glossary)
- [7) Trilha de Vídeo](#7-video-track-with-transcripts--timecodes)
- [8) Biblioteca de Passos do DataFlow](#8-dataflow-step-library-quick-reference)
- [9) FAQ](#9-faq-short-practical)

---

## 1) Metodologia — como usar este guia {: #1-methodology--how-to-use-this-guide }

- **Progressão de trilha única**: um caminho unificado para todos os papéis, conceitos novos mínimos por etapa.
- **Vinculação de primeira menção**: cada conceito/elemento de UI é vinculado uma vez na primeira aparição; etapas posteriores assumem isso.
- **Profundidade just-in-time**: cada etapa referencia documentos focados e um vídeo curto com timestamps clicáveis.
- **Resultados visíveis**: cada etapa termina em um resultado concreto e testável no Workplace.
- **Mentalidade de erro primeiro**: A Etapa 10 ensina depuração sistemática/análise de logs.
- **Avaliação**: o **Capstone** (Etapa 11) valida CRUD, integração, modelagem, navegação e papéis/permissões.

### Escopo & pré-requisitos

- Acesso ao **Aqtra Studio/Workplace** (inquilino na nuvem) _ou_ uma configuração local de **Docker** (≥ 4 vCPU / 8 GB RAM).
- Navegador moderno e a capacidade de visualizar a aba **Network** das ferramentas de desenvolvedor.
- (Opcional) Familiaridade básica com JSON e APIs HTTP para a Etapa 6.

### Resultados de aprendizado (por etapa)

- **Etapa 1**: você pode acessar o Studio/Workplace.
- **Etapa 2**: você pode modelar uma entidade (Fatura) e exibi-la em um Componente visível no Workplace.
- **Etapa 3**: você pode construir um DataFlow e vinculá-lo a um Botão.
- **Etapa 4**: você pode completar CRUD e validação básica.
- **Etapa 5**: você pode adicionar lógica em Python em um fluxo.
- **Etapa 6**: você pode chamar uma API HTTP externa e mapear resultados.
- **Etapa 7**: você pode compor uma página MultiComponent com contexto de dados.
- **Etapa 8**: você pode navegar entre páginas com parâmetros de ação.
- **Etapa 9**: você pode renderizar e baixar um documento de um template.
- **Etapa 10**: você pode diagnosticar erros usando logs/ferramentas de desenvolvedor e republicar.
- **Etapa 11**: você pode entregar uma pequena funcionalidade com papéis/permissões e uma integração.

### Ciclo de feedback

- Após **Primeira vitória** e **Capstone**, capture feedback: o que estava pouco claro, onde apareceram erros e quais links/vídeos ajudaram mais; alimente isso de volta na documentação.

### Rubrica de avaliação (Capstone)

- [ ] CRUD funciona com validação e mensagens claras para o usuário.
- [ ] Chamada de API externa mapeada; falhas tratadas (timeouts/4xx/5xx).
- [ ] Template de documento renderizado; arquivo é baixável.
- [ ] Navegação via parâmetros de ação abre o registro/página correta.
- [ ] Pelo menos **2 papéis** configurados com acesso diferente.
- [ ] Todos os componentes **Publicados** sem avisos bloqueadores.

---

## 2) Roteiro de aprendizado passo a passo (trilha única)

Um caminho unificado para todos os papéis. Siga as etapas na ordem; cada etapa vincula a documentos e (opcionalmente) a um vídeo curto.

**Etapa 1 — Acessar o Aqtra (nuvem ou Docker)**
Obtenha uma instância em funcionamento (veja a Seção 4). Verifique se você pode abrir **Studio** e **Workplace**.

**Etapa 2 — Estrutura básica da primeira aplicação**
Crie um **DataModel** mínimo (por exemplo, `Invoice(number, title, totalAmount, dueDate)`) e um **Componente** para exibir/editar. Publique e adicione à navegação para que apareça no Workplace.

**Docs**: Componente → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/pt/app-development/component.html) ; Catálogo de UI → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/pt/app-development/ui-components/index.html)
**Vídeo**: Tutorial #1 → [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ) ; Tutorial #2 → [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)

**Etapa 3 — Noções básicas de DataFlow**
Adicione um **DataFlow** com estágios/passos: `Get Action Model → Update Entry → Write Response`. Vincule-o a um **Botão** e teste criar/atualizar.

**Docs**: Visão geral do Dataflow → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/pt/app-development/data-flow-components/index.html) ; Atualizar entrada → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/pt/app-development/data-flow-components/update-entry.html) ; Executar dataflow → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-dataflow.html)
**Vídeo**: Tutorial #3 — ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))

**Etapa 4 — Conclusão do CRUD**
Adicione visualizações de lista/detalhe, finalize fluxos de criar/atualizar/excluir e validações.

**Docs**: Data Grid → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/pt/app-development/ui-components/data-grid.html)
**Vídeo**: Tutorial #4 — excluir via Atualizar Entrada ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)); Tutorial #5 — filtros dinâmicos ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180))

**Etapa 5 — Scripting em Python para lógica de negócios**
Insira um passo de **Python Script** para calcular campos derivados e validar entradas.

**Docs**: Executar script → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-script.html)
**Vídeo**: Tutorial #6 — Executar Script ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370))

**Etapa 6 — Integrações externas**
Chame uma API HTTP externa de um script Python; mapeie a resposta para seu DataModel.

**Docs**: Executar chamada de API → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-api-call.html)
**Vídeo**: (Opcional) Tutorial #10 — diagnosticando incompatibilidades de payload/tipo ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! dica "Solução de problemas"
_ **Timeout/5xx**: verifique URL/método/cabeçalhos; adicione retry/backoff; registre o corpo da resposta.
_ **401/403**: forneça/atualize o token de autenticação (armazenar segredos com segurança).
_ **406/422 (incompatibilidade de tipo)**: corrija o mapeamento de campos e tipos; transforme em **Executar Script** (por exemplo, string → número/data) antes de `Update Entry`.
_ Use `context.Logger` para registrar IDs de correlação e trechos de payload.

**Etapa 7 — Páginas MultiComponent**
Componha uma página a partir de vários componentes (filtros + grade + formulário). Configure **contexto de dados** e fiação.

**Docs**: List View → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/pt/app-development/ui-components/list-view.html) ; Tab Control → [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/pt/app-development/ui-components/tab-control.html) ; Gráficos → [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/pt/app-development/ui-components/charts.html)
**Vídeo**: Tutorial #6 — diálogo modal + grade de atualização automática ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)); Tutorial #7 — List View ([00:59](https://youtu.be/PtAJwn07sWI?t=59)–[03:00](https://youtu.be/PtAJwn07sWI?t=180))

> **Dica de design (opcional)**: agrupe entradas relacionadas em painéis, mantenha o ritmo vertical consistente (múltiplos de 8–12px), evite o uso excessivo de gráficos—adicione-os apenas quando esclarecer tendências.

**Etapa 8 — Navegação & fiação entre páginas**
Adicione itens de menu e abra páginas com **parâmetros de ação** (transfira registro `id` da grade para o formulário).

**Docs**: Ações de botão → [https://docs.aqtra.io/app-development/ui-components/button.html](https://docs.aqtra.io/pt/app-development/ui-components/button.html)
**Vídeo**: Tutorial #12 — abrir página + mapeamento de parâmetros ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)); Tutorial #5 — Abrir aplicação da grade ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))

**Etapa 9 — Templates & geração de documentos (PDF)**
Renderize e baixe um documento de um template via DataFlow.

**Docs**: Componentes do dataflow (Renderizar Template) → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/pt/app-development/data-flow-components/index.html)
**Vídeo**: Tutorial #12 — renderizar template + download ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165); [05:20](https://youtu.be/k36-qpZa9bU?t=320)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

**Etapa 10 — Tratamento de erros & depuração**
Use a aba Network e logs do Studio para diagnosticar 4xx/5xx; corrija tipos; republicar.

**Docs**: Publicando aplicações → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/pt/app-development/publishing-applications.html)
**Vídeo**: Tutorial #10 — encontrando e corrigindo erros ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! dica "Solução de problemas"

- Siga a sequência: **Compilar → Salvar → Pronto para publicar → Publicar**; verifique se o componente está listado como _Publicado_.
- Use as ferramentas de desenvolvedor do navegador **Network** para comparar solicitação/resposta com o esquema esperado; corrija mapeamento/tipos.
  _ Se o comportamento diferir entre páginas, verifique se **todos os componentes dependentes** foram republicados juntos.
  _ Em configurações Docker, inspecione os logs do contêiner para rastreamentos de pilha e conflitos de porta.

**Etapa 11 — Capstone**
Amplie seu aplicativo em uma pequena funcionalidade (por exemplo, Mini-CRM): papéis/permissões, painel MultiComponent, uma integração, um template de documento. Documente os critérios de aceitação e faça um vídeo de demonstração curto.

[Voltar ao topo](#getting-started)

---

## 3) Tutoriais & Links Cruzados de Documentação {: #tutorials-documentation-cross-links }

**Instalação / Plataforma**

- Configurações básicas, autenticação, logs, métricas → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/pt/install1/basic-settings.html)

**Construção principal**

- Componente (criação, configurações básicas) → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/pt/app-development/component.html)
- Catálogo de componentes de UI (primeira menção) → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/pt/app-development/ui-components/index.html)
- Data Grid (primeira menção) → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/pt/app-development/ui-components/data-grid.html)
- List View / Tab Control / Gráficos (primeira menção) → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/pt/app-development/ui-components/list-view.html), [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/pt/app-development/ui-components/tab-control.html), [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/pt/app-development/ui-components/charts.html)

**Fluxos / Lógica**

- Visão geral do Dataflow → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/pt/app-development/data-flow-components/index.html)
- Atualizar Entrada (CRUD) → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/pt/app-development/data-flow-components/update-entry.html)
- Executar dataflow → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-dataflow.html)
- Executar script (Python) → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-script.html)
- Executar chamada de API → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-api-call.html)

**Publicação**

- Publicando aplicações → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/pt/app-development/publishing-applications.html)

**Tutoriais (docs)**

- Tutorial #1 → [https://docs.aqtra.io/tutorials/tutorial1.html](https://docs.aqtra.io/pt/tutorials/tutorial1.html)
- Tutorial #2 → [https://docs.aqtra.io/tutorials/tutorial2.html](https://docs.aqtra.io/pt/tutorials/tutorial2.html)
- Tutorial #3 → [https://docs.aqtra.io/tutorials/tutorial3.html](https://docs.aqtra.io/pt/tutorials/tutorial3.html)

**Índice de vídeos (timestamps clicáveis)**

- T#3 — Noções básicas de DataFlow ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450)).
- T#4 — Excluir via Atualizar Entrada ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)).
- T#5 — Filtros da Data Grid; Abrir aplicação ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680)).
- T#6 — Executar Script; diálogo modal; grade de atualização automática ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)).
- T#10 — Depurar 500→406; corrigir tipos; republicar ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300)).
- T#12 — Renderizar template; Download; Abrir página + mapeamento ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)).

---

## 4) Primeira vitória em ~60 minutos

> Construa a mini-funcionalidade **Inventário de Faturas** de ponta a ponta.

1. **Acesse o Aqtra** (nuvem ou Docker) e abra o **Studio**.
2. **Crie o DataModel** `Invoice(number, title, totalAmount, dueDate)`.
3. **Adicione um Componente** para criar/listar faturas (primeiro uso do Data Grid).
4. **Conecte um DataFlow** — `Get Action Model → Update Entry → Write Response` (opcional **Executar Script** para validar totalAmount).
5. **Publique** e verifique no **Workplace**: crie duas faturas, edite uma.

**Docs**: Tutoriais → Construa sua primeira aplicação — [https://docs.aqtra.io/tutorials/index.html](https://docs.aqtra.io/pt/tutorials/index.html)

---

## 5) Instalar & Acessar {: #5-install--access }

Escolha uma das opções a seguir. Mantenha credenciais e chaves de licença seguras.

### Opção 1 — Nuvem (Hospedada)

- Obtenha acesso através de um parceiro de hospedagem ou compre diretamente.
- Preços & aquisição: [https://aqtra.io/#price](https://aqtra.io/#price).
- Receba uma URL de organização/inquilino e credenciais.
- Configure SSO (opcional), usuários e papéis.

### Opção 2 — Local (Docker)

**Pré-requisitos**: Docker Engine/Compose mais recente; host Linux/Windows/macOS com **4 vCPU / 8 GB RAM** no mínimo.

**Checklist**

- [ ] Instale Docker/Compose e verifique se `docker ps` funciona.
- [ ] Prepare `docker-compose.yml` e `.env` com os segredos necessários.
- [ ] Inicie o DB → `docker compose up -d db` e aguarde a prontidão.
- [ ] Inicie o app → `docker compose up -d app`.
- [ ] Acesse o **Workplace** em `http://<host>:8080/` e o **Studio** em `http://<host>:8080/studio/`.

**Docs**: Configurações básicas (arquitetura, portas, autenticação, logs, métricas) → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/pt/install1/basic-settings.html)

[Voltar ao topo](#getting-started)

---

## 6) Conceitos Básicos (Glossário do Aqtra)

Definições curtas e acionáveis.

- **Componente** — um bloco de construção de UI que renderiza dados e ações para os usuários (formulário, lista, detalhe, etc.). [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/pt/app-development/component.html)
- **DataFlow** — um fluxo direcionado de operações (por exemplo, validar → transformar → persistir → notificar) que executa em eventos de usuário ou sistema. Passos típicos: **Obter Modelo de Ação**, **Atualizar Entrada**, **Escrever Resposta**, **Executar Script**, **Executar Chamada de API**. [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/pt/app-development/data-flow-components/index.html)
- **DataModel** — a definição estruturada de entidades/atributos que a aplicação persiste e manipula.
- **MultiComponent** — uma visão composta que reúne vários Componentes (por exemplo, lista + detalhes + filtros) em uma página coesa; os elementos usam **contexto de dados** para se vincular a um componente fonte.
- **Python Script** — passo de lógica personalizada incorporado em um fluxo para transformar dados, chamar serviços ou implementar regras. [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-script.html)

---

## 7) Trilha de Vídeo (com transcrições & timestamps) {: #7-video-track-with-transcripts--timecodes }

Lista centralizada de vídeos com links profundos e timestamps. Use esses para pular diretamente para os momentos relevantes da demonstração.

- **Tutorial #1** — [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ)
- **Tutorial #2** — [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)
- **Tutorial #3** — Noções básicas de DataFlow ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))
- **Tutorial #4** — Excluir via Atualizar Entrada ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380))
- **Tutorial #5** — Filtros da Data Grid; Abrir aplicação ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))
- **Tutorial #6** — Executar Script; diálogo modal; grade de atualização automática ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020))
- **Tutorial #7** — [https://youtu.be/PtAJwn07sWI](https://youtu.be/PtAJwn07sWI)
- **Tutorial #8** — [https://youtu.be/YfqfdJpDm-k](https://youtu.be/YfqfdJpDm-k)
- **Tutorial #9/10** — Depuração & diagnósticos ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))
- **Tutorial #11** — [https://youtu.be/d-FD1ARn0h0](https://youtu.be/d-FD1ARn0h0)
- **Tutorial #12** — Renderizar template; Download; Abrir página + mapeamento ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

!!! nota "Mantenha-se atualizado"
Inscreva-se na **Aqtra Academy** no YouTube e verifique a raiz da documentação regularmente para atualizações. Novos episódios serão vinculados aqui à medida que chegarem.

[Voltar ao topo](#getting-started)

---

## 8) Biblioteca de Passos do DataFlow (referência rápida)

Alguns passos úteis que você provavelmente usará além do CRUD:

- **Atualizar Entrada** — [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/pt/app-development/data-flow-components/update-entry.html)
- **Executar dataflow** — chame outro dataflow e mescle resultados.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-dataflow.html)
- **Executar chamada de API** — configure e execute solicitação HTTP, vincule resultados.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/pt/app-development/data-flow-components/execute-api-call.html)
- **Obter entidade por id** — busque entidade por identificador via campo de catálogo.
  [https://docs.aqtra.io/app-development/data-flow-components/get-entity-by-id.html](https://docs.aqtra.io/pt/app-development/data-flow-components/get-entity-by-id.html)
- **Atualizar campo do modelo** — definir/derivar um único campo dentro do modelo.
  [https://docs.aqtra.io/workflow-components/update-model-field.html](https://docs.aqtra.io/pt/workflow-components/update-model-field.html)
- **Matemática simples** — adicione/subtraia/multiplique e escreva em um campo de destino.
  [https://docs.aqtra.io/app-development/data-flow-components/simple-math.html](https://docs.aqtra.io/pt/app-development/data-flow-components/simple-math.html)
- **Armazenar entrada sobre o bus** — crie/armazenar instância de componente de forma assíncrona.
  [https://docs.aqtra.io/app-development/data-flow-components/store-entry-over-bus.html](https://docs.aqtra.io/pt/app-development/data-flow-components/store-entry-over-bus.html)
- **Inscrever-se no conector** — por exemplo, assinatura RabbitMQ → processar → salvar.
  [https://docs.aqtra.io/app-development/data-flow-components/subscribe-to-connector.html](https://docs.aqtra.io/pt/app-development/data-flow-components/subscribe-to-connector.html)

[Voltar ao topo](#getting-started)

---

## 9) FAQ (curto, prático)

**Q: Nuvem vs local?**
A: Nuvem para o onboarding mais rápido/acesso à equipe; Docker local para offline/PoCs/ambientes restritos.

**Q: Docker falha ao iniciar ou está lento.**
A: Certifique-se de que 4 vCPU/8 GB RAM+, libere as portas de destino e verifique os logs do contêiner. Reinicie o Docker e tente compor novamente.

**Q: Onde colocar lógica personalizada?**
A: Adicione um passo de **Python Script** dentro de um **DataFlow** para validar, transformar ou chamar APIs externas.

**Q: Como chamar serviços externos?**
A: Use `http.client` de um script Python; mapeie a resposta para seu DataModel.

**Q: Principais blocos de construção?**
A: **DataModel**, **Componente**, **DataFlow**, **MultiComponent**, **Python Script**.

**Q: Erros e exceções?**
A: Use o inspetor de rede e logs do Studio; corrija incompatibilidades de tipo, republicar e re-teste. Veja o vídeo na Seção 8.

**Q: Como comprar ou obter um teste?**
A: Veja preços: [https://aqtra.io/#price](https://aqtra.io/#price). Compre via fornecedor ou diretamente; para implantações hospedadas, siga o onboarding do parceiro.

---

## 10) O que vem a seguir

- Padrões & melhores práticas (nomenclatura, versionamento, testes de fluxos).
- Integrações avançadas (SSO, bancos de dados, filas de mensagens).
- Fluxos de trabalho em equipe (revisões de código para scripts, promoção de ambiente).
- Links de comunidade & suporte (Slack/Telegram/Fórum) — _adicionar quando disponível_.