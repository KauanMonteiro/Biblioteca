# Sistema de Gerenciamento de Biblioteca Digital

Plataforma web para gestão de acervo digital com empréstimo de livros eletrônicos, desenvolvida em Django. Oferece controle de usuários, categorização de conteúdos e visualização integrada de documentos.

## Funcionalidades Principais

- **Gestão de Acervo**:
  - Cadastro de livros com metadados (título, autor, ISBN)
  - Upload de arquivos em múltiplos formatos (PDF, DOCX, TXT)
  - Categorização por gêneros literários

- **Controle de Usuários**:
  - Dois perfis de acesso: Usuário comum e Administrador
  - Histórico de empréstimos individuais
  - Sistema de devolução automática

- **Operações Principais**:
  - Empréstimo digital com registro temporal
  - Busca por título e autor
  - Visualizador integrado para documentos textuais

- **Administração**:
  - Dashboard de gestão de livros e usuários
  - Exclusão/edição de registros
  - Controle de capas e arquivos digitais

## Tecnologias Utilizadas

- **Backend**: Django 4.x
- **Processamento de Documentos**: python-docx
- **Gerenciamento de Arquivos**: Pillow (imagens)
- **Frontend**: HTML5, CSS3