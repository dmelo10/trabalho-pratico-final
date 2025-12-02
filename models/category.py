"""
Modelo de Categoria
"""
from datetime import datetime

class Category:
    """Classe que representa uma categoria"""
    
    def __init__(self, id=None, name='', color='#007bff', created_at=None):
        self.id = id
        self.name = name
        self.color = color
        self.created_at = created_at or datetime.now()
    
    def update_name(self, new_name):
        """Atualiza o nome da categoria"""
        if new_name and len(new_name.strip()) > 0:
            self.name = new_name.strip()
            return True
        return False
    
    def update_color(self, new_color):
        """Atualiza a cor da categoria"""
        if new_color and new_color.startswith('#'):
            self.color = new_color
            return True
        return False
    
    def validate_color(self):
        """Valida o formato da cor hexadecimal"""
        return self.color.startswith('#') and len(self.color) == 7
    
    def to_dict(self):
        """Converte a categoria para dicionário"""
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else str(self.created_at)
        }
    
    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}', color='{self.color}')"

