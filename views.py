from core import app

import resources

app.route('/')(resources.index)

app.route('/crear')(resources.crear_receta)

app.route('/ver_receta/<id>')(resources.ver_receta)