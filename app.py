"""
Aplicação principal - Sistema de Gerenciamento de Tarefas
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.task import Task
from models.user import User
from models.category import Category
from services.task_service import TaskService
from services.user_service import UserService
from services.category_service import CategoryService
from database.db_manager import DatabaseManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Inicializar banco de dados
db_manager = DatabaseManager()
db_manager.init_db()

# Inicializar serviços
task_service = TaskService(db_manager)
user_service = UserService(db_manager)
category_service = CategoryService(db_manager)

@app.route('/')
def index():
    """Página inicial"""
    tasks = task_service.get_all_tasks()
    categories = category_service.get_all_categories()
    return render_template('index.html', tasks=tasks, categories=categories)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """API: Listar todas as tarefas"""
    tasks = task_service.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/tasks', methods=['POST'])
def create_task():
    """API: Criar nova tarefa"""
    data = request.json
    task = task_service.create_task(
        title=data.get('title'),
        description=data.get('description', ''),
        category_id=data.get('category_id'),
        user_id=data.get('user_id', 1)
    )
    return jsonify(task.to_dict()), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """API: Obter tarefa por ID"""
    task = task_service.get_task_by_id(task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """API: Atualizar tarefa"""
    data = request.json
    task = task_service.update_task(
        task_id,
        title=data.get('title'),
        description=data.get('description'),
        completed=data.get('completed'),
        category_id=data.get('category_id')
    )
    if task:
        return jsonify(task.to_dict())
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """API: Deletar tarefa"""
    success = task_service.delete_task(task_id)
    if success:
        return jsonify({'message': 'Tarefa deletada com sucesso'}), 200
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    """Marcar tarefa como concluída"""
    task = task_service.complete_task(task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/categories', methods=['GET'])
def get_categories():
    """API: Listar todas as categorias"""
    categories = category_service.get_all_categories()
    return jsonify([cat.to_dict() for cat in categories])

@app.route('/categories', methods=['POST'])
def create_category():
    """API: Criar nova categoria"""
    data = request.json
    category = category_service.create_category(
        name=data.get('name'),
        color=data.get('color', '#007bff')
    )
    return jsonify(category.to_dict()), 201

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'task-manager'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

