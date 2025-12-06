import mysql.connector
from mysql.connector import Error

# ==========================
# CONEXÃO
# ==========================

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="eventos_mma"  # se quiser usar m3, troque aqui
        )

        if conexao.is_connected():
            print("Conectado ao banco!")
            return conexao

    except Error as erro:
        print("Erro ao conectar:", erro)
        return None


# ==========================
# FUNÇÕES GENÉRICAS DE EXECUÇÃO
# ==========================

def executar_dml(con, sql, valores):
    """INSERT, UPDATE, DELETE"""
    try:
        cursor = con.cursor()
        cursor.execute(sql, valores)
        con.commit()
        print("Operação realizada com sucesso!")
    except Error as e:
        print("Erro na operação:", e)
    finally:
        cursor.close()

def executar_select(con, sql, valores=None):
    """SELECT com ou sem parâmetros"""
    try:
        cursor = con.cursor()
        if valores:
            cursor.execute(sql, valores)
        else:
            cursor.execute(sql)
        resultados = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
        if resultados:
            print("\nResultados:")
            print("-" * 60)
            print(" | ".join(colunas))
            print("-" * 60)
            for linha in resultados:
                print(" | ".join(str(c) for c in linha))
            print("-" * 60)
        else:
            print("Nenhum registro encontrado.")
    except Error as e:
        print("Erro ao buscar dados:", e)
    finally:
        cursor.close()


# ==========================
# CRUD - ACADEMIA
# ==========================

def criar_academia(con):
    nome = input("Nome da academia: ")
    sql = "INSERT INTO Academia (nome) VALUES (%s)"
    executar_dml(con, sql, (nome,))

def listar_academias(con):
    sql = "SELECT * FROM Academia"
    executar_select(con, sql)

def atualizar_academia(con):
    listar_academias(con)
    id_ = input("ID da academia a atualizar: ")
    nome = input("Novo nome: ")
    sql = "UPDATE Academia SET nome = %s WHERE id = %s"
    executar_dml(con, sql, (nome, id_))

def deletar_academia(con):
    listar_academias(con)
    id_ = input("ID da academia a excluir: ")
    sql = "DELETE FROM Academia WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_academia(con):
    while True:
        print("\n--- MENU ACADEMIA ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_academia(con)
        elif op == '2':
            listar_academias(con)
        elif op == '3':
            atualizar_academia(con)
        elif op == '4':
            deletar_academia(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - CATEGORIA
# ==========================

def criar_categoria(con):
    nome = input("Nome da categoria: ")
    limite_peso = input("Limite de peso (kg): ")
    sql = "INSERT INTO Categoria (nome, limite_peso) VALUES (%s, %s)"
    executar_dml(con, sql, (nome, limite_peso))

def listar_categorias(con):
    sql = "SELECT * FROM Categoria"
    executar_select(con, sql)

def atualizar_categoria(con):
    listar_categorias(con)
    id_ = input("ID da categoria a atualizar: ")
    nome = input("Novo nome: ")
    limite_peso = input("Novo limite de peso: ")
    sql = "UPDATE Categoria SET nome = %s, limite_peso = %s WHERE id = %s"
    executar_dml(con, sql, (nome, limite_peso, id_))

def deletar_categoria(con):
    listar_categorias(con)
    id_ = input("ID da categoria a excluir: ")
    sql = "DELETE FROM Categoria WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_categoria(con):
    while True:
        print("\n--- MENU CATEGORIA ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_categoria(con)
        elif op == '2':
            listar_categorias(con)
        elif op == '3':
            atualizar_categoria(con)
        elif op == '4':
            deletar_categoria(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - LUTADOR
# ==========================

def criar_lutador(con):
    print("Cadastre o lutador:")
    listar_academias(con)
    id_academia = input("ID da academia: ")
    listar_categorias(con)
    id_categoria = input("ID da categoria: ")
    nome = input("Nome: ")
    altura = input("Altura (m): ")
    envergadura = input("Envergadura (m): ")
    tem_luta = input("Tem luta marcada? (s/n): ").lower()
    tem_luta_marcada = 1 if tem_luta == 's' else 0
    posicao = input("Posição no ranking (ou deixe vazio): ")
    posicao_ranking = posicao if posicao != "" else None

    sql = """
        INSERT INTO Lutador
        (id_academia, id_categoria, nome, altura, envergaura, tem_luta_marcada, posicao_ranking)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    executar_dml(con, sql, (id_academia, id_categoria, nome, altura, envergadura, tem_luta_marcada, posicao_ranking))

def listar_lutadores(con):
    sql = "SELECT l.*, c.nome as cateoria_peso  FROM Lutador l JOIN Categoria c ON (c.id = l.id_categoria);"
    executar_select(con, sql)

def atualizar_lutador(con):
    listar_lutadores(con)
    id_ = input("ID do lutador a atualizar: ")
    nome = input("Novo nome: ")
    altura = input("Nova altura: ")
    envergadura = input("Nova envergadura: ")
    tem_luta = input("Tem luta marcada? (s/n): ").lower()
    tem_luta_marcada = 1 if tem_luta == 's' else 0
    posicao = input("Nova posição no ranking (ou vazio): ")
    posicao_ranking = posicao if posicao != "" else None

    sql = """
        UPDATE Lutador
        SET nome = %s, altura = %s, envergaura = %s,
            tem_luta_marcada = %s, posicao_ranking = %s
        WHERE id = %s
    """
    executar_dml(con, sql, (nome, altura, envergadura, tem_luta_marcada, posicao_ranking, id_))

def deletar_lutador(con):
    listar_lutadores(con)
    id_ = input("ID do lutador a excluir: ")
    sql = "DELETE FROM Lutador WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_lutador(con):
    while True:
        print("\n--- MENU LUTADOR ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_lutador(con)
        elif op == '2':
            listar_lutadores(con)
        elif op == '3':
            atualizar_lutador(con)
        elif op == '4':
            deletar_lutador(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - CARD
# ==========================

def criar_card(con):
    nome = input("Nome do card: ")
    data_evento = input("Data do evento (AAAA-MM-DD): ")
    sql = "INSERT INTO Card (nome, data_evento) VALUES (%s, %s)"
    executar_dml(con, sql, (nome, data_evento))

def listar_cards(con):
    sql = "SELECT * FROM Card"
    executar_select(con, sql)

def atualizar_card(con):
    listar_cards(con)
    id_ = input("ID do card a atualizar: ")
    nome = input("Novo nome: ")
    data_evento = input("Nova data (AAAA-MM-DD): ")
    sql = "UPDATE Card SET nome = %s, data_evento = %s WHERE id = %s"
    executar_dml(con, sql, (nome, data_evento, id_))

def deletar_card(con):
    listar_cards(con)
    id_ = input("ID do card a excluir: ")
    sql = "DELETE FROM Card WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_card(con):
    while True:
        print("\n--- MENU CARD ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_card(con)
        elif op == '2':
            listar_cards(con)
        elif op == '3':
            atualizar_card(con)
        elif op == '4':
            deletar_card(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - ÁRBITRO
# ==========================

def criar_arbitro(con):
    nome = input("Nome do árbitro: ")
    altura = input("Altura (m): ")
    limite_peso = input("Limite de peso (kg): ")
    numero_doc = input("Número do documento: ")
    sql = "INSERT INTO Arbitro (nome, altura, limite_peso, numero_doc) VALUES (%s, %s, %s, %s)"
    executar_dml(con, sql, (nome, altura, limite_peso, numero_doc))

def listar_arbitros(con):
    sql = "SELECT * FROM Arbitro"
    executar_select(con, sql)

def atualizar_arbitro(con):
    listar_arbitros(con)
    id_ = input("ID do árbitro a atualizar: ")
    nome = input("Novo nome: ")
    altura = input("Nova altura: ")
    limite_peso = input("Novo limite de peso: ")
    numero_doc = input("Novo documento: ")
    sql = """
        UPDATE Arbitro
        SET nome = %s, altura = %s, limite_peso = %s, numero_doc = %s
        WHERE id = %s
    """
    executar_dml(con, sql, (nome, altura, limite_peso, numero_doc, id_))

def deletar_arbitro(con):
    listar_arbitros(con)
    id_ = input("ID do árbitro a excluir: ")
    sql = "DELETE FROM Arbitro WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_arbitro(con):
    while True:
        print("\n--- MENU ÁRBITRO ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_arbitro(con)
        elif op == '2':
            listar_arbitros(con)
        elif op == '3':
            atualizar_arbitro(con)
        elif op == '4':
            deletar_arbitro(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - LUTA
# ==========================

def criar_luta(con):
    numero_rounds = input("Número de rounds: ")
    listar_arbitros(con)
    id_arbitro = input("ID do árbitro: ")
    listar_cards(con)
    id_card = input("ID do card: ")
    sql = "INSERT INTO Luta (numero_rounds, id_arbitro, id_card) VALUES (%s, %s, %s)"
    executar_dml(con, sql, (numero_rounds, id_arbitro, id_card))

def listar_lutas(con):
    sql = "SELECT l.id, lut.nome as nome_lutador, l.numero_rounds, a.nome as nome_arbitiro, c.nome as nome_card FROM Luta l JOIN arbitro a ON (l.id_arbitro = a.id) JOIN card c ON (c.id = l.id_card) JOIN participa p ON (l.id = p.id_luta) JOIN lutador lut on (lut.id = p.id_lutador);"
    executar_select(con, sql)

def atualizar_luta(con):
    listar_lutas(con)
    id_ = input("ID da luta a atualizar: ")
    numero_rounds = input("Novo número de rounds: ")
    listar_arbitros(con)
    id_arbitro = input("Novo ID de árbitro: ")
    listar_cards(con)
    id_card = input("Novo ID de card: ")
    sql = """
        UPDATE Luta
        SET numero_rounds = %s, id_arbitro = %s, id_card = %s
        WHERE id = %s
    """
    executar_dml(con, sql, (numero_rounds, id_arbitro, id_card, id_))

def deletar_luta(con):
    listar_lutas(con)
    id_ = input("ID da luta a excluir: ")
    sql = "DELETE FROM Luta WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_luta(con):
    while True:
        print("\n--- MENU LUTA ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_luta(con)
        elif op == '2':
            listar_lutas(con)
        elif op == '3':
            atualizar_luta(con)
        elif op == '4':
            deletar_luta(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - PARTICIPA (Lutador x Luta)
# ==========================

def criar_participa(con):
    listar_lutadores(con)
    id_lutador = input("ID do lutador: ")
    listar_lutas(con)
    id_luta = input("ID da luta: ")
    sql = "INSERT INTO Participa (id_lutador, id_luta) VALUES (%s, %s)"
    executar_dml(con, sql, (id_lutador, id_luta))

def listar_participa(con):
    sql = "SELECT * FROM Participa"
    executar_select(con, sql)

def atualizar_participa(con):
    listar_participa(con)
    id_ = input("ID do registro em Participa a atualizar: ")
    listar_lutadores(con)
    id_lutador = input("Novo ID do lutador: ")
    listar_lutas(con)
    id_luta = input("Novo ID da luta: ")
    sql = "UPDATE Participa SET id_lutador = %s, id_luta = %s WHERE id = %s"
    executar_dml(con, sql, (id_lutador, id_luta, id_))

def deletar_participa(con):
    listar_participa(con)
    id_ = input("ID do registro em Participa a excluir: ")
    sql = "DELETE FROM Participa WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_participa(con):
    while True:
        print("\n--- MENU PARTICIPA ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_participa(con)
        elif op == '2':
            listar_participa(con)
        elif op == '3':
            atualizar_participa(con)
        elif op == '4':
            deletar_participa(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - JUIZ
# ==========================

def criar_juiz(con):
    nome = input("Nome do juiz: ")
    numero_doc = input("Documento do juiz: ")
    sql = "INSERT INTO Juiz (nome, numero_doc) VALUES (%s, %s)"
    executar_dml(con, sql, (nome, numero_doc))

def listar_juizes(con):
    sql = "SELECT * FROM Juiz"
    executar_select(con, sql)

def atualizar_juiz(con):
    listar_juizes(con)
    id_ = input("ID do juiz a atualizar: ")
    nome = input("Novo nome: ")
    numero_doc = input("Novo documento: ")
    sql = "UPDATE Juiz SET nome = %s, numero_doc = %s WHERE id = %s"
    executar_dml(con, sql, (nome, numero_doc, id_))

def deletar_juiz(con):
    listar_juizes(con)
    id_ = input("ID do juiz a excluir: ")
    sql = "DELETE FROM Juiz WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_juiz(con):
    while True:
        print("\n--- MENU JUIZ ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_juiz(con)
        elif op == '2':
            listar_juizes(con)
        elif op == '3':
            atualizar_juiz(con)
        elif op == '4':
            deletar_juiz(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# CRUD - JULGA (Juiz x Luta)
# ==========================

def criar_julga(con):
    listar_juizes(con)
    id_juiz = input("ID do juiz: ")
    listar_lutas(con)
    id_luta = input("ID da luta: ")
    pontuacao = input("Pontuação (ex: 29-28): ")
    sql = "INSERT INTO julga (id_juiz, id_luta, pontuacao) VALUES (%s, %s, %s)"
    executar_dml(con, sql, (id_juiz, id_luta, pontuacao))

def listar_julga(con):
    sql = "SELECT jg.id, jz.nome as nome_juiz, jg.id_luta, jg.pontuacao FROM julga jg JOIN Juiz jz ON (jg.id_juiz = jz.id);"
    executar_select(con, sql)

def atualizar_julga(con):
    listar_julga(con)
    id_ = input("ID do registro em julga a atualizar: ")
    listar_juizes(con)
    id_juiz = input("Novo ID do juiz: ")
    listar_lutas(con)
    id_luta = input("Novo ID da luta: ")
    pontuacao = input("Nova pontuação: ")
    sql = "UPDATE julga SET id_juiz = %s, id_luta = %s, pontuacao = %s WHERE id = %s"
    executar_dml(con, sql, (id_juiz, id_luta, pontuacao, id_))

def deletar_julga(con):
    listar_julga(con)
    id_ = input("ID do registro em julga a excluir: ")
    sql = "DELETE FROM julga WHERE id = %s"
    executar_dml(con, sql, (id_,))

def menu_julga(con):
    while True:
        print("\n--- MENU JULGA ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Opção: ")
        if op == '1':
            criar_julga(con)
        elif op == '2':
            listar_julga(con)
        elif op == '3':
            atualizar_julga(con)
        elif op == '4':
            deletar_julga(con)
        elif op == '0':
            break
        else:
            print("Opção inválida.")


# ==========================
# MENU PRINCIPAL
# ==========================

def menu_principal(con):
    while True:
        print("\n=========== MENU PRINCIPAL ===========")
        print("1 - Academia")
        print("2 - Categoria")
        print("3 - Lutador")
        print("4 - Card")
        print("5 - Árbitro")
        print("6 - Luta")
        print("7 - Participa (Lutador x Luta)")
        print("8 - Juiz")
        print("9 - julga (Juiz x Luta)")
        print("0 - Sair")
        op = input("Opção: ")

        if op == '1':
            menu_academia(con)
        elif op == '2':
            menu_categoria(con)
        elif op == '3':
            menu_lutador(con)
        elif op == '4':
            menu_card(con)
        elif op == '5':
            menu_arbitro(con)
        elif op == '6':
            menu_luta(con)
        elif op == '7':
            menu_participa(con)
        elif op == '8':
            menu_juiz(con)
        elif op == '9':
            menu_julga(con)
        elif op == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


# ==========================
# MAIN
# ==========================

def main():
    con = conectar()
    if con:
        menu_principal(con)
        con.close()
        print("Conexão encerrada.")


if __name__ == "__main__":
    main()