# Aula de Pydeck

O objetivo deste repositório é conter os codigos, como também as referências utilizadas na aula.

## Como clonar o projeto

1- Clonando Repositório

```bash
https://github.com/luhborba/aula_pydeck.git
cd aula_pydeck
```

2- Ativar Ambiente e Instalar Dependências

Com `poetry`:
```bash
poetry shell
poetry install --no-root
```

Com `pip` no Windows:
```bash
python -m venv venv
venv/Scripts/activate
pip install -r requeriments.txt
```

Com `pip` no Linux:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requeriments.txt
```

3- Executando

```bash
streamlit run app.py
```

## Links Uteis

[Instalação Pyenv, Pipx e Poetry com meu xará](https://www.youtube.com/watch?v=9LYqtLuD7z4)
[Documentação Pydeck](https://deckgl.readthedocs.io/en/latest/)