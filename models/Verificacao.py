from control.MainController import db

class Verificacao(db.Model):
    __tablename__ = 'verificacao'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    isvalid = db.Column(db.Boolean, default=False)
    token = db.Column(db.String)
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'isValid': self.isvalid,
            'token': self.token
        }
    
    