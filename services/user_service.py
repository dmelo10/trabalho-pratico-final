"""
Serviço de gerenciamento de usuários
"""
from models.user import User

class UserService:
    """Serviço para operações relacionadas a usuários"""
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def create_user(self, name, email):
        """Cria um novo usuário"""
        if not name or len(name.strip()) == 0:
            raise ValueError("Nome do usuário é obrigatório")
        if not email or '@' not in email:
            raise ValueError("Email inválido")
        
        user = User(name=name.strip(), email=email.strip())
        return self.db_manager.save_user(user)
    
    def get_all_users(self):
        """Retorna todos os usuários"""
        return self.db_manager.get_all_users()
    
    def get_user_by_id(self, user_id):
        """Retorna um usuário por ID"""
        return self.db_manager.get_user_by_id(user_id)
    
    def update_user(self, user_id, name=None, email=None):
        """Atualiza um usuário existente"""
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        if name is not None:
            user.update_name(name)
        if email is not None:
            user.update_email(email)
        
        return self.db_manager.save_user(user)
    
    def delete_user(self, user_id):
        """Deleta um usuário"""
        return self.db_manager.delete_user(user_id)
    
    def find_user_by_email(self, email):
        """Encontra um usuário por email"""
        users = self.get_all_users()
        for user in users:
            if user.email == email:
                return user
        return None

