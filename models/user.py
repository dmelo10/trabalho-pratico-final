"""
Modelo de Usuário
"""
from datetime import datetime

class User:
    """Classe que representa um usuário"""
    
    def __init__(self, id=None, name='', email='', created_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at or datetime.now()
    
    def update_name(self, new_name):
        """Atualiza o nome do usuário"""
        if new_name and len(new_name.strip()) > 0:
            self.name = new_name.strip()
            return True
        return False
    
    def update_email(self, new_email):
        """Atualiza o email do usuário"""
        if new_email and '@' in new_email:
            self.email = new_email.strip()
            return True
        return False
    
    def validate_email(self):
        """Valida o formato do email"""
        return '@' in self.email and '.' in self.email.split('@')[1]
    
    def to_dict(self):
        """Converte o usuário para dicionário"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else str(self.created_at)
        }
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

