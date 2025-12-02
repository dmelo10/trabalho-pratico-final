"""
Modelo de Tarefa
"""
from datetime import datetime

class Task:
    """Classe que representa uma tarefa"""
    
    def __init__(self, id=None, title='', description='', completed=False, 
                 created_at=None, category_id=None, user_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now()
        self.category_id = category_id
        self.user_id = user_id
    
    def mark_completed(self):
        """Marca a tarefa como concluída"""
        self.completed = True
    
    def mark_incomplete(self):
        """Marca a tarefa como não concluída"""
        self.completed = False
    
    def update_title(self, new_title):
        """Atualiza o título da tarefa"""
        if new_title and len(new_title.strip()) > 0:
            self.title = new_title.strip()
            return True
        return False
    
    def update_description(self, new_description):
        """Atualiza a descrição da tarefa"""
        self.description = new_description or ''
        return True
    
    def is_overdue(self):
        """Verifica se a tarefa está atrasada (exemplo de método adicional)"""
        # Implementação simplificada
        return False
    
    def to_dict(self):
        """Converte a tarefa para dicionário"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else str(self.created_at),
            'category_id': self.category_id,
            'user_id': self.user_id
        }
    
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

