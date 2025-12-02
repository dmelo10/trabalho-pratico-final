"""
Serviço de gerenciamento de tarefas
"""
from models.task import Task
from datetime import datetime

class TaskService:
    """Serviço para operações relacionadas a tarefas"""
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def create_task(self, title, description='', category_id=None, user_id=1):
        """Cria uma nova tarefa"""
        if not title or len(title.strip()) == 0:
            raise ValueError("Título da tarefa é obrigatório")
        
        task = Task(
            title=title.strip(),
            description=description or '',
            completed=False,
            category_id=category_id,
            user_id=user_id
        )
        return self.db_manager.save_task(task)
    
    def get_all_tasks(self):
        """Retorna todas as tarefas"""
        return self.db_manager.get_all_tasks()
    
    def get_task_by_id(self, task_id):
        """Retorna uma tarefa por ID"""
        return self.db_manager.get_task_by_id(task_id)
    
    def update_task(self, task_id, title=None, description=None, 
                   completed=None, category_id=None):
        """Atualiza uma tarefa existente"""
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        
        if title is not None:
            task.update_title(title)
        if description is not None:
            task.update_description(description)
        if completed is not None:
            if completed:
                task.mark_completed()
            else:
                task.mark_incomplete()
        if category_id is not None:
            task.category_id = category_id
        
        return self.db_manager.save_task(task)
    
    def delete_task(self, task_id):
        """Deleta uma tarefa"""
        return self.db_manager.delete_task(task_id)
    
    def complete_task(self, task_id):
        """Marca uma tarefa como concluída"""
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_completed()
            return self.db_manager.save_task(task)
        return None
    
    def get_tasks_by_category(self, category_id):
        """Retorna tarefas de uma categoria específica"""
        all_tasks = self.get_all_tasks()
        return [task for task in all_tasks if task.category_id == category_id]
    
    def get_completed_tasks(self):
        """Retorna todas as tarefas concluídas"""
        all_tasks = self.get_all_tasks()
        return [task for task in all_tasks if task.completed]
    
    def get_pending_tasks(self):
        """Retorna todas as tarefas pendentes"""
        all_tasks = self.get_all_tasks()
        return [task for task in all_tasks if not task.completed]

