from database import db
from datetime import datetime

# `db.Model` es una clase base para todos los modelos de SQLAlchemy
# Define la clase `User` que hereda de `db.Model`
# `User` representa la tabla `users` en la base de datos
class User(db.Model):
    __tablename__ = "users"
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    fecha_nac = db.Column(db.Date, nullable=False)

    # Inicializa la clase `User`
    def __init__(self, first_name, last_name, email, contrasena, fecha_nac):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contrasena = contrasena
        self.fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos
    @staticmethod
    def get_all():
        return User.query.all()

    # Obtiene un usuario por su id
    @staticmethod
    def get_by_id(id):
        # consulta con SQLAlchemy
        return User.query.get(id)

    # Actualiza un usuario en la base de datos
    def update(self):
        db.session.commit()

    # Eliminar
    def delete(self):
        # return User.query.filter(User.id == 123).delete()
        db.session.delete()