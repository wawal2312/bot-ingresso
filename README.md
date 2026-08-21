# Bot Ingresso - Automacao e Monitoramento de Ingressos

> Script desenvolvido em Python para monitoramento continuo de disponibilidade, extracao de dados (web scraping) e automacao de processos em plataformas de eventos.

---

## Problema e Solucao

* **O Problema:** A alta demanda e o esgotamento rapido de ingressos tornam o monitoramento manual ineficiente, exigindo atualizacoes constantes de pagina e reacoes em segundos.
* **A Solucao:** O Bot Ingresso automatiza a verificacao periodica de lotes, identifica mudancas de status em tempo real e agiliza o fluxo de compra por meio de requisicoes automatizadas ou navegacao via WebDriver.

---

## Principais Funcionalidades

- [x] Monitoramento periodico e automatizado de disponibilidade de ingressos
- [x] Web scraping e extracao de dados em tempo real (precos, lotes e setores)
- [x] Notificacoes e alertas automáticos ao detectar liberacao de vagas
- [x] Tratamento de timeouts, mudancas de DOM e bloqueios de requisicao

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Automacao & Scraping:** Selenium / BeautifulSoup4 / Requests
* **Gerenciamento de Ambiente:** Virtualenv (venv)

---

## Estrutura do Projeto

```text
bot-ingresso/
 ├── src/
 │    ├── config.py       # Parametros de URL, seletores e credenciais
 │    ├── scraper.py      # Logica de extracao e parsing de dados
 │    └── main.py         # Loop principal de execucao e monitoramento
 ├── requirements.txt     # Dependencias do projeto
 └── README.md
