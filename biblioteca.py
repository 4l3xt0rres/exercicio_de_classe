class Biblioteca:
    def _init_(self, titulo, autor, ano_que_foi_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_que_foi_publicado = ano_que_foi_publicado
        self.disponivel = True
        
    
    def exibir_informacoes(self):
        print('Titulo:', self.titulo)
        print('Autor:', self.autor)
        print('ano da publicação:', self.ano_que_foi_publicado)
        print('Disponível:', 'sim' if self.disponivel else 'não')

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'o livro {self.titulo} foi emprestado com sucesso')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'o livro {self.titulo} foi devolvido com sucesso')