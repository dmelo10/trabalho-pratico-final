"""
Serviço de gerenciamento de categorias
"""
from models.category import Category

class CategoryService:
    """Serviço para operações relacionadas a categorias"""
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def create_category(self, name, color='#007bff'):
        """Cria uma nova categoria"""
        if not name or len(name.strip()) == 0:
            raise ValueError("Nome da categoria é obrigatório")
        if not color.startswith('#'):
            color = '#007bff'
        
        category = Category(name=name.strip(), color=color)
        return self.db_manager.save_category(category)
    
    def get_all_categories(self):
        """Retorna todas as categorias"""
        return self.db_manager.get_all_categories()
    
    def get_category_by_id(self, category_id):
        """Retorna uma categoria por ID"""
        return self.db_manager.get_category_by_id(category_id)
    
    def update_category(self, category_id, name=None, color=None):
        """Atualiza uma categoria existente"""
        category = self.get_category_by_id(category_id)
        if not category:
            return None
        
        if name is not None:
            category.update_name(name)
        if color is not None:
            category.update_color(color)
        
        return self.db_manager.save_category(category)
    
    def delete_category(self, category_id):
        """Deleta uma categoria"""
        return self.db_manager.delete_category(category_id)
    
    def find_category_by_name(self, name):
        """Encontra uma categoria por nome"""
        categories = self.get_all_categories()
        for category in categories:
            if category.name.lower() == name.lower():
                return category
        return None

