from pathlib import Path
import unicodedata

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
PASTA_DADOS = BASE_DIR / "valores_iniciais"
PASTA_DADOS_ALTERNATIVA = BASE_DIR / "valore_iniciais"
PASTA_RESULTADOS = BASE_DIR / "resultados"
ARQUIVO_ANALISE_INICIAL = PASTA_RESULTADOS / "analise_inicial.csv"
ARQUIVO_ANALISE_RESUMO = PASTA_RESULTADOS / "analise_resumo.csv"


# Limpa valores textuais e trata campos vazios.
def tratar_texto(valor):
    if pd.isna(valor):
        return None

    texto = str(valor).strip()
    if not texto:
        return None

    if "Ãƒ" in texto:
        try:
            texto = texto.encode("latin1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass

    return texto


# Remove acentos para deixar os textos padronizados.
def remover_acentos(texto):
    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFKD", texto)
        if not unicodedata.combining(caractere)
    )


# Converte diferentes formatos de data para data valida.
def parse_data(valor):
    texto = tratar_texto(valor)
    if texto is None:
        return pd.NaT

    if texto.isdigit():
        return pd.to_datetime(int(texto), unit="s", errors="coerce")

    if "-" in texto:
        return pd.to_datetime(texto, format="%Y-%m-%d", errors="coerce")

    if "/" in texto:
        return pd.to_datetime(texto, format="%d/%m/%Y", errors="coerce")

    return pd.to_datetime(texto, errors="coerce")


# Padroniza nomes de cidades.
def normalizar_cidade(cidade):
    texto = tratar_texto(cidade)
    if texto is None:
        return None
    return remover_acentos(texto).lower().title()


# Padroniza status e preenche valores faltantes.
def normalizar_status(valor):
    texto = tratar_texto(valor)
    if texto is None:
        return "nao_informado"
    return remover_acentos(texto).lower()


# Ajusta o nome do cliente.
def normalizar_nome(valor):
    texto = tratar_texto(valor)
    if texto is None:
        return "nao_informado"
    return texto.title()


# Padroniza a sigla do estado.
def normalizar_estado(valor):
    texto = tratar_texto(valor)
    if texto is None:
        return "NA"
    return remover_acentos(texto).upper()


# Converte valores monetarios em numeros.
def converter_valor(valor):
    texto = tratar_texto(valor)
    if texto is None:
        return None

    texto = texto.replace(".", "").replace(",", ".") if "," in texto else texto

    try:
        return float(texto)
    except ValueError:
        return None


# Formata datas para o padrao ano-mes-dia.
def formatar_data_serie(serie):
    return serie.dt.strftime("%Y-%m-%d").where(serie.notna(), None)


# Preenche campos vazios com um valor padrao.
def preencher_nao_informado(serie):
    serie_texto = serie.astype("string").str.strip()
    return (
        serie_texto.fillna("nao_informado")
        .replace("", "nao_informado")
        .replace("<NA>", "nao_informado")
        .replace("nan", "nao_informado")
        .replace("NaT", "nao_informado")
        .replace("None", "nao_informado")
    )


# Le um csv da pasta de entrada.
def carregar_csv(nome_arquivo):
    pasta_origem = PASTA_DADOS if PASTA_DADOS.exists() else PASTA_DADOS_ALTERNATIVA
    return pd.read_csv(pasta_origem / nome_arquivo, sep=";", dtype=str)


# Gera o arquivo analise_inicial.csv com os dados tratados.
def gerar_analise_inicial():
    pedidos = carregar_csv("pedidos.csv")
    clientes = carregar_csv("clientes.csv")
    entregas = carregar_csv("entregas.csv")

    pedidos["id_pedido"] = pd.to_numeric(pedidos["id_pedido"], errors="coerce").astype("Int64")
    pedidos["id_cliente"] = pd.to_numeric(pedidos["id_cliente"], errors="coerce").astype("Int64")
    pedidos["data_pedido"] = pedidos["data_pedido"].apply(parse_data)
    pedidos["valor_total"] = pedidos["valor_total"].apply(converter_valor)
    pedidos["status"] = pedidos["status"].apply(normalizar_status)

    clientes["id_cliente"] = pd.to_numeric(clientes["id_cliente"], errors="coerce").astype("Int64")
    clientes["nome"] = clientes["nome"].apply(normalizar_nome)
    clientes["cidade"] = clientes["cidade"].apply(normalizar_cidade)
    clientes["estado"] = clientes["estado"].apply(normalizar_estado)
    clientes["data_cadastro"] = clientes["data_cadastro"].apply(parse_data)

    entregas["id_entrega"] = pd.to_numeric(entregas["id_entrega"], errors="coerce").astype("Int64")
    entregas["id_pedido"] = pd.to_numeric(entregas["id_pedido"], errors="coerce").astype("Int64")
    entregas["data_prevista"] = entregas["data_prevista"].apply(parse_data)
    entregas["data_realizada"] = entregas["data_realizada"].apply(parse_data)
    entregas["status_entrega"] = entregas["status_entrega"].apply(normalizar_status)

    df = pedidos.merge(clientes, on="id_cliente", how="left")
    df = df.merge(entregas, on="id_pedido", how="left")

    df["nome"] = df["nome"].fillna("nao_informado")
    df["cidade"] = df["cidade"].fillna("nao_informado")
    df["estado"] = df["estado"].fillna("NA")
    df["status_entrega"] = df["status_entrega"].fillna("nao_informado")

    df["atraso_dias"] = (df["data_realizada"] - df["data_prevista"]).dt.days.astype("Int64")

    df_final = df[
        [
            "id_pedido",
            "id_cliente",
            "nome",
            "cidade",
            "estado",
            "data_cadastro",
            "valor_total",
            "status",
            "data_pedido",
            "data_prevista",
            "data_realizada",
            "atraso_dias",
            "status_entrega",
        ]
    ].rename(
        columns={
            "nome": "nome_cliente",
            "cidade": "cidade_normalizada",
            "status": "status_pedido",
            "data_cadastro": "data_cadastro_cliente",
            "data_prevista": "data_prevista_entrega",
            "data_realizada": "data_realizada_entrega",
        }
    )

    for coluna in [
        "data_cadastro_cliente",
        "data_pedido",
        "data_prevista_entrega",
        "data_realizada_entrega",
    ]:
        df_final[coluna] = formatar_data_serie(pd.to_datetime(df_final[coluna], errors="coerce"))

    for coluna in df_final.columns:
        df_final[coluna] = preencher_nao_informado(df_final[coluna])

    PASTA_RESULTADOS.mkdir(exist_ok=True)
    df_final.to_csv(ARQUIVO_ANALISE_INICIAL, index=False, sep=";", encoding="utf-8-sig")
    return df_final


# Deixa os textos da saida mais legiveis.
def formatar_texto(texto):
    if pd.isna(texto):
        return "Nao informado"

    return str(texto).replace("_", " ").strip().title()


# Converte numeros para texto no formato brasileiro.
def formatar_numero(valor, casas_decimais=2):
    if pd.isna(valor):
        return "Nao disponivel"

    return f"{float(valor):.{casas_decimais}f}".replace(".", ",")


# Monta uma linha da tabela de resumo.
def montar_saida(indicador, detalhe, valor, unidade, ordem):
    return {
        "ordem": ordem,
        "indicador": indicador,
        "detalhe": detalhe,
        "valor": valor,
        "unidade": unidade,
    }


# Prepara o dataframe para as analises finais.
def carregar_dados_resumo():
    df = pd.read_csv(ARQUIVO_ANALISE_INICIAL, sep=";", dtype=str)
    df["valor_total"] = pd.to_numeric(df["valor_total"], errors="coerce")
    df["atraso_dias"] = pd.to_numeric(df["atraso_dias"], errors="coerce")
    return df


# Conta quantos pedidos existem por status.
def total_pedidos_por_status(df):
    resultado = (
        df["status_pedido"]
        .fillna("nao_informado")
        .value_counts(dropna=False)
        .rename_axis("status_pedido")
        .reset_index(name="total_pedidos")
    )
    linhas = []

    for _, linha in resultado.iterrows():
        linhas.append(
            montar_saida(
                "Total de pedidos por status",
                formatar_texto(linha["status_pedido"]),
                str(int(linha["total_pedidos"])),
                "pedidos",
                1,
            )
        )

    return pd.DataFrame(linhas)


# Calcula o ticket medio por estado.
def ticket_medio_por_estado(df):
    resultado = (
        df.groupby("estado", dropna=False)["valor_total"]
        .mean()
        .round(2)
        .reset_index(name="ticket_medio")
    )
    resultado["estado"] = resultado["estado"].fillna("Nao informado").replace("NA", "Nao informado")

    linhas = []

    for _, linha in resultado.iterrows():
        linhas.append(
            montar_saida(
                "Ticket medio por estado",
                linha["estado"],
                formatar_numero(linha["ticket_medio"]),
                "R$",
                2,
            )
        )

    return pd.DataFrame(linhas)


# Calcula o percentual de entregas no prazo e com atraso.
def percentual_entregas(df):
    entregas_realizadas = df[df["atraso_dias"].notna()].copy()

    if entregas_realizadas.empty:
        return pd.DataFrame(
            [
                montar_saida("Percentual de entregas", "No prazo", formatar_numero(0), "%", 3),
                montar_saida("Percentual de entregas", "Com atraso", formatar_numero(0), "%", 3),
            ]
        )

    total = len(entregas_realizadas)
    no_prazo = (entregas_realizadas["atraso_dias"] <= 0).sum()
    com_atraso = (entregas_realizadas["atraso_dias"] > 0).sum()

    return pd.DataFrame(
        [
            montar_saida(
                "Percentual de entregas",
                "No prazo",
                formatar_numero(round((no_prazo / total) * 100, 2)),
                "%",
                3,
            ),
            montar_saida(
                "Percentual de entregas",
                "Com atraso",
                formatar_numero(round((com_atraso / total) * 100, 2)),
                "%",
                3,
            ),
        ]
    )


# Lista as 3 cidades com maior volume de pedidos.
def top_3_cidades(df):
    resultado = (
        df[df["cidade_normalizada"].notna() & (df["cidade_normalizada"] != "nao_informado")]
        ["cidade_normalizada"]
        .value_counts()
        .head(3)
        .rename_axis("cidade_normalizada")
        .reset_index(name="total_pedidos")
    )
    linhas = []

    for posicao, (_, linha) in enumerate(resultado.iterrows(), start=1):
        linhas.append(
            montar_saida(
                "Top 3 cidades com maior volume de pedidos",
                f"{posicao}o lugar - {linha['cidade_normalizada']}",
                str(int(linha["total_pedidos"])),
                "pedidos",
                4,
            )
        )

    return pd.DataFrame(linhas)


# Calcula a media de atraso dos pedidos atrasados.
def media_atraso(df):
    pedidos_atrasados = df[df["atraso_dias"] > 0]
    media = pedidos_atrasados["atraso_dias"].mean()

    return pd.DataFrame(
        [
            montar_saida(
                "Media de atraso para pedidos com atraso",
                "Pedidos com atraso",
                str(int(round(media))) if pd.notna(media) else "0",
                "dias",
                5,
            )
        ]
    )


# Junta todos os resultados e salva o resumo final.
def salvar_resultados(resultados):
    resultado_final = pd.concat(resultados, ignore_index=True)
    resultado_final = resultado_final.sort_values(["ordem", "indicador", "detalhe"]).drop(columns=["ordem"])
    resultado_final.to_csv(ARQUIVO_ANALISE_RESUMO, sep=";", index=False, encoding="utf-8-sig")


# Gera o arquivo analise_resumo.csv a partir da analise inicial.
def gerar_analise_resumo():
    df = carregar_dados_resumo()

    resultados = [
        total_pedidos_por_status(df),
        ticket_medio_por_estado(df),
        percentual_entregas(df),
        top_3_cidades(df),
        media_atraso(df),
    ]

    salvar_resultados(resultados)


# Executa as duas etapas em sequencia.
def pipeline():
    gerar_analise_inicial()
    gerar_analise_resumo()
    print(f"Pipeline executado com sucesso! Arquivos gerados em: {PASTA_RESULTADOS}")


if __name__ == "__main__":
    pipeline()
