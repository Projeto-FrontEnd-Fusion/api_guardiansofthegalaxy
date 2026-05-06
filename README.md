# api_guardiansofthegalaxy
Este repositório foi criado para o desenvolvimento e manutenção da API da squad Guardiões da galaxia, concentrando a estrutura do projeto, definição de endpoints, integrações e regras de negócio necessárias para suportar as funcionalidades da aplicação. 

CODE BY DINHO - Develop



## Taskipy

O projeto utiliza o **Taskipy** para centralizar os comandos de desenvolvimento.

### Verificar instalação

Para confirmar se o Taskipy está instalado no ambiente:

```bash
poetry show taskipy
```

### Comandos disponíveis

| Comando | Descrição |
|---------|-----------|
| `poetry run task dev` | Inicia a API em modo de desenvolvimento |
| `poetry run task test` | Executa os testes automatizados |
| `poetry run task lint` | Analisa o código com lint |
| `poetry run task format` | Formata o código automaticamente |

### Exemplo de uso
```bash
poetry run task dev
```

### Vantagens dessa versão
- visual mais limpo
- leitura rápida
- padrão comum em projetos profissionais
- facilita para outros devs entenderem os scripts rapidamente

# Logging

Este projeto utiliza um sistema de logging configurável para fornecer visibilidade sobre o funcionamento da aplicação.

## 🔎 Níveis de Log

Os seguintes níveis de log estão disponíveis:

- `DEBUG` → Informações detalhadas para debug
- `INFO` → Eventos normais da aplicação
- `WARNING` → Situações inesperadas, mas não críticas
- `ERROR` → Erros que afetam uma funcionalidade
- `CRITICAL` → Erros graves que podem interromper a aplicação

---

## Configuração

### LOG_LEVEL
O nível de log pode ser configurado via variável de ambiente:

```env
LOG_LEVEL=INFO
```
### ENVIRONMENT
Define o formato dos logs:

```env
ENVIRONMENT=development
```

development → logs coloridos e mais legíveis no console

production → logs estruturados em JSON (ideal para observabilidade)

Caso não seja definido, será utilizado um valor padrão configurado na aplicação.

## Como usar o logger

Para utilizar o logger em qualquer módulo:

```bash
from app.core.logger import get_logger

logger = get_logger(__name__)

def minha_funcao():
    logger.debug("Mensagem de debug")
    logger.info("Processo iniciado")
    logger.warning("Algo inesperado aconteceu")
    logger.error("Ocorreu um erro")
    logger.critical("Erro crítico")
```

 ## Exemplo de saída no console
```text
2026-05-02 12:00:00 | INFO     | app.main           | Aplicação iniciada
2026-05-02 12:00:01 | INFO     | app.api.health     | Endpoint /health chamado
2026-05-02 12:00:02 | ERROR    | app.services.user  | Erro ao buscar usuário
```