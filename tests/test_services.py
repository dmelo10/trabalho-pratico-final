"""
Testes de unidade para os serviços
"""
import pytest
from services.task_service import TaskService
from services.user_service import UserService
from services.category_service import CategoryService
from database.db_manager import DatabaseManager

class TestTaskService:
    """Testes para o TaskService"""
    
    def setup_method(self):
        """Configuração antes de cada teste"""
        self.db_manager = DatabaseManager()
        self.db_manager.init_db()
        self.service = TaskService(self.db_manager)
    
    def test_create_task(self):
        """Testa criação de tarefa"""
        task = self.service.create_task("Nova tarefa", "Descrição")
        assert task.id is not None
        assert task.title == "Nova tarefa"
        assert task.description == "Descrição"
    
    def test_create_task_empty_title(self):
        """Testa criação com título vazio"""
        with pytest.raises(ValueError):
            self.service.create_task("")
    
    def test_get_all_tasks(self):
        """Testa obter todas as tarefas"""
        self.service.create_task("Tarefa 1")
        self.service.create_task("Tarefa 2")
        tasks = self.service.get_all_tasks()
        assert len(tasks) == 2
    
    def test_get_task_by_id(self):
        """Testa obter tarefa por ID"""
        task = self.service.create_task("Teste")
        found = self.service.get_task_by_id(task.id)
        assert found is not None
        assert found.id == task.id
    
    def test_update_task(self):
        """Testa atualização de tarefa"""
        task = self.service.create_task("Original")
        updated = self.service.update_task(task.id, title="Atualizado")
        assert updated.title == "Atualizado"
    
    def test_delete_task(self):
        """Testa deleção de tarefa"""
        task = self.service.create_task("Para deletar")
        result = self.service.delete_task(task.id)
        assert result == True
        assert self.service.get_task_by_id(task.id) is None
    
    def test_complete_task(self):
        """Testa completar tarefa"""
        task = self.service.create_task("Tarefa")
        completed = self.service.complete_task(task.id)
        assert completed.completed == True
    
    def test_get_completed_tasks(self):
        """Testa obter tarefas concluídas"""
        task1 = self.service.create_task("Tarefa 1")
        task2 = self.service.create_task("Tarefa 2")
        self.service.complete_task(task1.id)
        completed = self.service.get_completed_tasks()
        assert len(completed) == 1
        assert completed[0].id == task1.id
    
    def test_get_pending_tasks(self):
        """Testa obter tarefas pendentes"""
        task1 = self.service.create_task("Tarefa 1")
        task2 = self.service.create_task("Tarefa 2")
        self.service.complete_task(task1.id)
        pending = self.service.get_pending_tasks()
        assert len(pending) == 1
        assert pending[0].id == task2.id

class TestUserService:
    """Testes para o UserService"""
    
    def setup_method(self):
        """Configuração antes de cada teste"""
        self.db_manager = DatabaseManager()
        self.db_manager.init_db()
        self.service = UserService(self.db_manager)
    
    def test_create_user(self):
        """Testa criação de usuário"""
        user = self.service.create_user("João", "joao@example.com")
        assert user.id is not None
        assert user.name == "João"
        assert user.email == "joao@example.com"
    
    def test_create_user_invalid_email(self):
        """Testa criação com email inválido"""
        with pytest.raises(ValueError):
            self.service.create_user("João", "email-invalido")
    
    def test_find_user_by_email(self):
        """Testa encontrar usuário por email"""
        user = self.service.create_user("João", "joao@example.com")
        found = self.service.find_user_by_email("joao@example.com")
        assert found is not None
        assert found.id == user.id

class TestCategoryService:
    """Testes para o CategoryService"""
    
    def setup_method(self):
        """Configuração antes de cada teste"""
        self.db_manager = DatabaseManager()
        self.db_manager.init_db()
        self.service = CategoryService(self.db_manager)
    
    def test_create_category(self):
        """Testa criação de categoria"""
        category = self.service.create_category("Nova categoria", "#ff0000")
        assert category.id is not None
        assert category.name == "Nova categoria"
        assert category.color == "#ff0000"
    
    def test_find_category_by_name(self):
        """Testa encontrar categoria por nome"""
        category = self.service.create_category("Categoria Única Teste")
        found = self.service.find_category_by_name("Categoria Única Teste")
        assert found is not None
        assert found.id == category.id

