from core import app

import resources

app.route('/')(resources.index)

app.route('/crear')(resources.crear_receta)