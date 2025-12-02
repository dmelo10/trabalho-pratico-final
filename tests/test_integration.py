"""
Testes de integração
"""
import pytest
from app import app
from database.db_manager import DatabaseManager

@pytest.fixture
def client():
    """Fixture para criar cliente de teste"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestTaskAPI:
    """Testes de integração para API de tarefas"""
    
    def test_create_task_api(self, client):
        """Testa criação de tarefa via API"""
        response = client.post('/tasks', 
            json={'title': 'Nova tarefa', 'description': 'Teste'})
        assert response.status_code == 201
        data = response.get_json()
        assert data['title'] == 'Nova tarefa'
        assert 'id' in data
    
    def test_get_tasks_api(self, client):
        """Testa obter todas as tarefas via API"""
        # Criar uma tarefa primeiro
        client.post('/tasks', json={'title': 'Teste'})
        
        response = client.get('/tasks')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) > 0
    
    def test_get_task_by_id_api(self, client):
        """Testa obter tarefa por ID via API"""
        # Criar tarefa
        create_response = client.post('/tasks', json={'title': 'Teste'})
        task_id = create_response.get_json()['id']
        
        # Buscar tarefa
        response = client.get(f'/tasks/{task_id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['id'] == task_id
    
    def test_update_task_api(self, client):
        """Testa atualização de tarefa via API"""
        # Criar tarefa
        create_response = client.post('/tasks', json={'title': 'Original'})
        task_id = create_response.get_json()['id']
        
        # Atualizar tarefa
        response = client.put(f'/tasks/{task_id}',
            json={'title': 'Atualizado'})
        assert response.status_code == 200
        data = response.get_json()
        assert data['title'] == 'Atualizado'
    
    def test_delete_task_api(self, client):
        """Testa deleção de tarefa via API"""
        # Criar tarefa
        create_response = client.post('/tasks', json={'title': 'Para deletar'})
        task_id = create_response.get_json()['id']
        
        # Deletar tarefa
        response = client.delete(f'/tasks/{task_id}')
        assert response.status_code == 200
        
        # Verificar que foi deletada
        get_response = client.get(f'/tasks/{task_id}')
        assert get_response.status_code == 404
    
    def test_complete_task_api(self, client):
        """Testa completar tarefa via API"""
        # Criar tarefa
        create_response = client.post('/tasks', json={'title': 'Tarefa'})
        task_id = create_response.get_json()['id']
        
        # Completar tarefa
        response = client.post(f'/tasks/{task_id}/complete')
        assert response.status_code == 200
        data = response.get_json()
        assert data['completed'] == True

class TestCategoryAPI:
    """Testes de integração para API de categorias"""
    
    def test_create_category_api(self, client):
        """Testa criação de categoria via API"""
        response = client.post('/categories',
            json={'name': 'Nova categoria', 'color': '#ff0000'})
        assert response.status_code == 201
        data = response.get_json()
        assert data['name'] == 'Nova categoria'
    
    def test_get_categories_api(self, client):
        """Testa obter todas as categorias via API"""
        response = client.get('/categories')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

class TestHealthCheck:
    """Testes para health check"""
    
    def test_health_check(self, client):
        """Testa endpoint de health check"""
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'

