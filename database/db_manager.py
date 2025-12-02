"""
Gerenciador de banco de dados (simulado em memória)
"""
from models.task import Task
from models.user import User
from models.category import Category

class DatabaseManager:
    """Gerenciador de banco de dados em memória"""
    
    def __init__(self):
        self.tasks = []
        self.users = []
        self.categories = []
        self.task_counter = 0
        self.user_counter = 0
        self.category_counter = 0
    
    def init_db(self):
        """Inicializa o banco de dados com dados de exemplo"""
        # Criar usuário padrão
        default_user = User(id=1, name='Usuário Padrão', email='user@example.com')
        self.users.append(default_user)
        self.user_counter = 1
        
        # Criar categorias padrão
        default_categories = [
            Category(id=1, name='Trabalho', color='#007bff'),
            Category(id=2, name='Pessoal', color='#28a745'),
            Category(id=3, name='Urgente', color='#dc3545')
        ]
        self.categories.extend(default_categories)
        self.category_counter = 3
    
    def save_task(self, task):
        """Salva ou atualiza uma tarefa"""
        if task.id is None:
            self.task_counter += 1
            task.id = self.task_counter
            self.tasks.append(task)
        else:
            # Atualizar tarefa existente
            for i, t in enumerate(self.tasks):
                if t.id == task.id:
                    self.tasks[i] = task
                    break
        return task
    
    def get_all_tasks(self):
        """Retorna todas as tarefas"""
        return self.tasks.copy()
    
    def get_task_by_id(self, task_id):
        """Retorna uma tarefa por ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def delete_task(self, task_id):
        """Deleta uma tarefa"""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False
    
    def save_user(self, user):
        """Salva ou atualiza um usuário"""
        if user.id is None:
            self.user_counter += 1
            user.id = self.user_counter
            self.users.append(user)
        else:
            # Atualizar usuário existente
            for i, u in enumerate(self.users):
                if u.id == user.id:
                    self.users[i] = user
                    break
        return user
    
    def get_all_users(self):
        """Retorna todos os usuários"""
        return self.users.copy()
    
    def get_user_by_id(self, user_id):
        """Retorna um usuário por ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def delete_user(self, user_id):
        """Deleta um usuário"""
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        return False
    
    def save_category(self, category):
        """Salva ou atualiza uma categoria"""
        if category.id is None:
            self.category_counter += 1
            category.id = self.category_counter
            self.categories.append(category)
        else:
            # Atualizar categoria existente
            for i, c in enumerate(self.categories):
                if c.id == category.id:
                    self.categories[i] = category
                    break
        return category
    
    def get_all_categories(self):
        """Retorna todas as categorias"""
        return self.categories.copy()
    
    def get_category_by_id(self, category_id):
        """Retorna uma categoria por ID"""
        for category in self.categories:
            if category.id == category_id:
                return category
        return None
    
    def delete_category(self, category_id):
        """Deleta uma categoria"""
        for i, category in enumerate(self.categories):
            if category.id == category_id:
                del self.categories[i]
                return True
        return False

