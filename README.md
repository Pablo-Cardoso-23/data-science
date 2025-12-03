**Projeto: Data Science Prático (exercícios do livro "Data Science do Zero")**

- **Foco:**: Repositório dedicado a exercícios práticos e scripts que acompanham o livro *Data Science do Zero*. O objetivo é manter implementações pequenas e didáticas para cada capítulo, organizadas na pasta `activities/`.

**Conteúdo Atual**
- **Pasta:**: `activities/` — contém scripts por atividade/capítulo.
- **Exemplo:**: `activities/friendship_pairs.py` — script que demonstra análise simples de rede social e operações de dados: cálculo de número de amigos, amigos-de-amigos (FOAF), interesses comuns, agrupamento de salários por tempo de experiência, e contagem de palavras em tópicos de interesse.

**Como usar**
- **Requisito:**: Python 3.8+ recomendado.
- **Executar um script:**: Rode diretamente o arquivo com Python. Exemplo:

```bash
python activities/friendship_pairs.py
```

**Convenções e estrutura**
- **Nome dos arquivos:**: usar `capitulo_##_<tema>.py` ou `atividade_<capitulo>_<tema>.py` (ex.: `capitulo_03_friendship_pairs.py`) para facilitar ordenação e associação ao capítulo.
- **Localização:**: todo código de exercícios fica em `activities/`.
- **Formato dos scripts:**: scripts pequenos, com função `if __name__ == "__main__":` para execução direta; preferir funções reutilizáveis para testes posteriores.
- **Dependências:**: se algum exercício precisar de bibliotecas externas (pandas, numpy, etc.), adicione um `requirements.txt` ou atualize o `pyproject.toml`.

**Contribuindo**
- **Adicionar nova atividade:**: crie um arquivo em `activities/` seguindo as convenções de nome e inclua um comentário no topo indicando o capítulo e o objetivo do exercício.
- **Pull requests:**: Descreva o capítulo/tema e um breve resumo do que o script faz.

**Próximos passos sugeridos**
- Adicionar um `requirements.txt` com dependências comuns.
- Padronizar nomes dos arquivos existentes (opcional).
- Incluir testes simples para scripts críticos.

**Contato / Notas**
- Este repositório serve como um caderno de estudos práticos. Se quiser, posso:
