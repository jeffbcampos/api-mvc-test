from control.MainController import db

class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    imagem = db.Column(db.String)
    nota = db.Column(db.Integer)
    tipo = db.Column(db.String)
    id_api = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'imagem': self.imagem,
            'nota': self.nota,
            'tipo': self.tipo,
            'id_api': self.id_api,
            'id_usuario': self.id_usuario
        }