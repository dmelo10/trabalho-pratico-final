# Sistema de Gerenciamento de Tarefas

Sistema web desenvolvido em Python/Flask para gerenciamento de tarefas pessoais, com suporte a categorias e funcionalidades completas de CRUD.

## 📋 Características

- ✅ Criação, edição e exclusão de tarefas
- 🏷️ Organização por categorias
- ✅ Marcação de tarefas como concluídas
- 🎨 Interface web moderna e responsiva
- 🧪 Testes automatizados (unidade, integração e aceitação)
- 🚀 Pipeline CI/CD completo
- 🐳 Containerização com Docker

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas:

- **Models**: Modelos de dados (Task, User, Category)
- **Services**: Lógica de negócio
- **Database**: Gerenciamento de dados (atualmente em memória)
- **Templates**: Interface web (HTML/CSS/JavaScript)
- **Tests**: Testes automatizados

## 📊 Estatísticas do Projeto

- **Classes/Arquivos**: 10+
- **Métodos/Funções**: 20+
- **Testes**: Cobertura completa com pytest

## 🚀 Como Executar

### Pré-requisitos

- Python 3.11+
- pip
- Git

### Instalação Local

```bash
# Clonar repositório
git clone <repository-url>
cd trabalho-pratico

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

### Executar com Docker

```bash
# Build da imagem
docker build -t task-manager .

# Executar container
docker run -p 5000:5000 task-manager
```

## 🧪 Testes

### Executar todos os testes

```bash
pytest
```

### Executar testes específicos

```bash
# Testes de unidade
pytest tests/test_models.py

# Testes de integração
pytest tests/test_integration.py

# Testes de aceitação
pytest tests/test_acceptance.py
```

### Com cobertura

```bash
pytest --cov=. --cov-report=html
```

## 📁 Estrutura do Projeto

```
trabalho-pratico/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── Dockerfile            # Configuração Docker
├── pytest.ini            # Configuração pytest
├── models/               # Modelos de dados
├── services/             # Serviços de negócio
├── database/             # Gerenciamento de banco
├── templates/            # Templates HTML
└── tests/                # Testes automatizados
```

## 🔄 CI/CD Pipeline

O pipeline automatizado (GitHub Actions) executa:

1. **Build**: Instalação de dependências
2. **Testes**: Execução de todos os testes
3. **Cobertura**: Geração de relatório
4. **Build Docker**: Criação da imagem
5. **Deploy**: Implantação automática (se testes passarem)

## 📚 API Endpoints

- `GET /` - Página inicial
- `GET /tasks` - Listar todas as tarefas
- `POST /tasks` - Criar nova tarefa
- `GET /tasks/<id>` - Obter tarefa por ID
- `PUT /tasks/<id>` - Atualizar tarefa
- `DELETE /tasks/<id>` - Deletar tarefa
- `POST /tasks/<id>/complete` - Marcar tarefa como concluída
- `GET /categories` - Listar categorias
- `POST /categories` - Criar categoria
- `GET /health` - Health check


