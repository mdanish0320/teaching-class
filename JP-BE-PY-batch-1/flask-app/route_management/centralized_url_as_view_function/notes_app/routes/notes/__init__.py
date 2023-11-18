from .add_new_note import note_bp as add_note_bp
from .assign_note import note_bp as assign_note_bp
from .get_category_notes import note_bp as get_cat_notes_bp
from .get_notes import note_bp as get_notes_bp

notes_router_list = []
notes_router_list.append(add_note_bp)
notes_router_list.append(assign_note_bp)
notes_router_list.append(get_cat_notes_bp)
notes_router_list.append(get_notes_bp)
