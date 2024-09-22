from controller.api_blueprint import category_bp
from controller.category import create_category


category_bp.add_url_rule('/categories',view_func=create_category,methods=['POST'])
