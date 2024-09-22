from flask import Blueprint
from controller.category import create_category, get_categories, get_category

#create a auth module blueprint
category_bp = Blueprint('category_bp', __name__)

category_bp.add_url_rule('/categories',view_func=create_category,methods=['POST'])
category_bp.add_url_rule('/categories',view_func=get_categories,methods=['GET'])
category_bp.add_url_rule('/categories/<int:id>',view_func=get_category,methods=['GET'])
