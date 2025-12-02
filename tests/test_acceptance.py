"""
Testes de aceitação - Testes end-to-end
"""
import pytest
import requests
import time
from app import app
from database.db_manager import DatabaseManager

@pytest.fixture
def client():
    """Fixture para criar cliente de teste"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestAcceptance:
    """Testes de aceitação do sistema"""
    
    def test_complete_workflow(self, client):
        """
        Teste de aceitação: Fluxo completo de criação e gerenciamento de tarefas
        """
        # 1. Verificar que o sistema está funcionando
        health_response = client.get('/health')
        assert health_response.status_code == 200
        
        # 2. Criar uma nova tarefa
        create_response = client.post('/tasks',
            json={
                'title': 'Tarefa de Teste de Aceitação',
                'description': 'Esta é uma tarefa criada para teste de aceitação',
                'category_id': 1
            })
        assert create_response.status_code == 201
        task_data = create_response.get_json()
        task_id = task_data['id']
        assert task_data['title'] == 'Tarefa de Teste de Aceitação'
        assert task_data['completed'] == False
        
        # 3. Buscar a tarefa criada
        get_response = client.get(f'/tasks/{task_id}')
        assert get_response.status_code == 200
        assert get_response.get_json()['id'] == task_id
        
        # 4. Atualizar a tarefa
        update_response = client.put(f'/tasks/{task_id}',
            json={'description': 'Descrição atualizada'})
        assert update_response.status_code == 200
        assert update_response.get_json()['description'] == 'Descrição atualizada'
        
        # 5. Marcar tarefa como concluída
        complete_response = client.post(f'/tasks/{task_id}/complete')
        assert complete_response.status_code == 200
        assert complete_response.get_json()['completed'] == True
        
        # 6. Verificar que a tarefa aparece na lista de concluídas
        all_tasks_response = client.get('/tasks')
        assert all_tasks_response.status_code == 200
        tasks = all_tasks_response.get_json()
        completed_task = next((t for t in tasks if t['id'] == task_id), None)
        assert completed_task is not None
        assert completed_task['completed'] == True
        
        # 7. Deletar a tarefa
        delete_response = client.delete(f'/tasks/{task_id}')
        assert delete_response.status_code == 200
        
        # 8. Verificar que a tarefa foi deletada
        get_deleted_response = client.get(f'/tasks/{task_id}')
        assert get_deleted_response.status_code == 404
    
    def test_performance_requirement(self, client):
        """
        Teste de aceitação: Requisito de performance
        O sistema deve responder em menos de 1 segundo para operações básicas
        """
        start_time = time.time()
        response = client.get('/health')
        elapsed_time = time.time() - start_time
        
        assert response.status_code == 200
        assert elapsed_time < 1.0, f"Health check demorou {elapsed_time}s, esperado < 1s"
    
    def test_functional_requirement(self, client):
        """
        Teste de aceitação: Requisito funcional
        O sistema deve permitir criar, listar, atualizar e deletar tarefas
        """
        # Criar
        create_resp = client.post('/tasks', json={'title': 'Teste Funcional'})
        assert create_resp.status_code == 201
        task_id = create_resp.get_json()['id']
        
        # Listar
        list_resp = client.get('/tasks')
        assert list_resp.status_code == 200
        assert len(list_resp.get_json()) > 0
        
        # Atualizar
        update_resp = client.put(f'/tasks/{task_id}', json={'title': 'Atualizado'})
        assert update_resp.status_code == 200
        
        # Deletar
        delete_resp = client.delete(f'/tasks/{task_id}')
        assert delete_resp.status_code == 200

