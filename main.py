from biblioteca import Biblioteca

library = []

livro1 = Biblioteca("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Biblioteca("1984", "George Orwell", 1949)
livro3 = Biblioteca("Dom Quixote", "Alexsandro dos Santos", 1605)

library.append(livro1)
library.append(livro2)
library.append(livro3)

for livro in library:
    livro.exibir_informacoes()
    print('-'*30)


livro2.emprestar()
print('-'*30)

livro3.autor = 'Miguel de Cervantes'

print('lista final de livros em library: ')
print('-'*30)
for livro in library:
    livro.exibir_informacoes()
print('-'*30)
