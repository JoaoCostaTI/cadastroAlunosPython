import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            tel TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data_nascimento TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            curso TEXT NOT NULL,
                            picture TEXT NOT NULL)''')
    def register_student(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES(?,?,?,?,?,?,?,?)",(estudantes))
        self.conn.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso!', 'Registro com sucesso!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        return dados

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id = ?", (id,))
        dados = self.c.fetchone()

        return dados

    def update_student(self, nova_valores):
            query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?,data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=? "
            self.c.execute(query, nova_valores)
            self.conn.commit()

            # Mostrando mensagem de sucesso
            messagebox.showinfo('Sucesso!', f'Estudante com ID: {nova_valores[8]} foi atualizado!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE ID=?", (id,))
        self.conn.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso!', f'Estudante com ID: {id} foi deletado!')

# Criando uma instancia do sistema de registro

sistema_de_registro = SistemaDeRegistro()

# INSERIR Informações dos Estudantes

#estudante = ('Souza', 'bruno.souza87@proton.me', '31991112233', 'M', '06/12/1987', 'Rua Bela Vista 99, BR', 'Computação', 'imagem10.png')

#sistema_de_registro.register_student(estudante)

# Ver todos estudantes
#todos_alunos = sistema_de_registro.view_all_students()

# Procurar um aluno especifico
#aluno = sistema_de_registro.search_student(2)

# Atualizar aluno
#estudante = ('Roberto', 'roberto.costapp@outlook.com', '31992205457', 'F', '01/08/1987', 'DR. Afonso Neves 20, BR', 'História', 'imagem3.png', 2)
#aluno = sistema_de_registro.update_student(estudante)

# Deletar um aluno
#aluno = sistema_de_registro.delete_student(2)
