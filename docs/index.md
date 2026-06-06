# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Workflow

```mermaid
flowchart LR
    subgraph ETL[Pipeline]
        A(Multiplos Arquivos Excel) --> B[Extract: extract_from_excel]
        B[Extract: extract_from_excel] --> |Gera uma lista de Dataframes| C[Transformation: consolidate_dataframes]
        C[Transformation: consolidate_dataframes] --> |Gera um Dataframe Consolidado| D[Load: Converte para  Excel]
        D(Load: Converte para  Excel) --> |Salva o consolidado em Excel| E(Pasta Output: Um arquivo único Excel)

    end

```

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


# Função de transformação  de dados

### ::: app.pipeline.extract.extract_from_excel
