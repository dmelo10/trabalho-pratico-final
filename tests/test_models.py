"""
Testes de unidade para os modelos
"""
import pytest
from datetime import datetime
from models.task import Task
from models.user import User
from models.category import Category

class TestTask:
    """Testes para o modelo Task"""
    
    def test_create_task(self):
        """Testa a criação de uma tarefa"""
        task = Task(title="Teste", description="Descrição teste")
        assert task.title == "Teste"
        assert task.description == "Descrição teste"
        assert task.completed == False
    
    def test_mark_completed(self):
        """Testa marcar tarefa como concluída"""
        task = Task(title="Teste")
        task.mark_completed()
        assert task.completed == True
    
    def test_mark_incomplete(self):
        """Testa marcar tarefa como não concluída"""
        task = Task(title="Teste", completed=True)
        task.mark_incomplete()
        assert task.completed == False
    
    def test_update_title(self):
        """Testa atualização de título"""
        task = Task(title="Título antigo")
        result = task.update_title("Novo título")
        assert result == True
        assert task.title == "Novo título"
    
    def test_update_title_empty(self):
        """Testa atualização com título vazio"""
        task = Task(title="Título original")
        result = task.update_title("")
        assert result == False
        assert task.title == "Título original"
    
    def test_update_description(self):
        """Testa atualização de descrição"""
        task = Task(title="Teste")
        result = task.update_description("Nova descrição")
        assert result == True
        assert task.description == "Nova descrição"
    
    def test_to_dict(self):
        """Testa conversão para dicionário"""
        task = Task(id=1, title="Teste", completed=True)
        task_dict = task.to_dict()
        assert task_dict['id'] == 1
        assert task_dict['title'] == "Teste"
        assert task_dict['completed'] == True

class TestUser:
    """Testes para o modelo User"""
    
    def test_create_user(self):
        """Testa a criação de um usuário"""
        user = User(name="João", email="joao@example.com")
        assert user.name == "João"
        assert user.email == "joao@example.com"
    
    def test_update_name(self):
        """Testa atualização de nome"""
        user = User(name="João")
        result = user.update_name("João Silva")
        assert result == True
        assert user.name == "João Silva"
    
    def test_update_email(self):
        """Testa atualização de email"""
        user = User(email="old@example.com")
        result = user.update_email("new@example.com")
        assert result == True
        assert user.email == "new@example.com"
    
    def test_validate_email(self):
        """Testa validação de email"""
        user = User(email="test@example.com")
        assert user.validate_email() == True
        
        user2 = User(email="invalid")
        assert user2.validate_email() == False
    
    def test_to_dict(self):
        """Testa conversão para dicionário"""
        user = User(id=1, name="João", email="joao@example.com")
        user_dict = user.to_dict()
        assert user_dict['id'] == 1
        assert user_dict['name'] == "João"
        assert user_dict['email'] == "joao@example.com"

class TestCategory:
    """Testes para o modelo Category"""
    
    def test_create_category(self):
        """Testa a criação de uma categoria"""
        category = Category(name="Trabalho", color="#007bff")
        assert category.name == "Trabalho"
        assert category.color == "#007bff"
    
    def test_update_name(self):
        """Testa atualização de nome"""
        category = Category(name="Antiga")
        result = category.update_name("Nova")
        assert result == True
        assert category.name == "Nova"
    
    def test_update_color(self):
        """Testa atualização de cor"""
        category = Category(color="#000000")
        result = category.update_color("#ffffff")
        assert result == True
        assert category.color == "#ffffff"
    
    def test_validate_color(self):
        """Testa validação de cor"""
        category = Category(color="#007bff")
        assert category.validate_color() == True
        
        category2 = Category(color="invalid")
        assert category2.validate_color() == False
    
    def test_to_dict(self):
        """Testa conversão para dicionário"""
        category = Category(id=1, name="Trabalho", color="#007bff")
        category_dict = category.to_dict()
        assert category_dict['id'] == 1
        assert category_dict['name'] == "Trabalho"
        assert category_dict['color'] == "#007bff"

