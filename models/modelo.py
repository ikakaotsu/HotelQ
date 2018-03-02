'''
Created on 24/07/2013

@author: otiuqx
'''
import sqlalchemy as sa
import sqlalchemy.orm as sao
import sqlalchemy.ext.declarative as sad
from sqlalchemy.ext.hybrid import hybrid_property
# from sqlalchemy.ext.hybrid import hybrid_property

maker = sao.sessionmaker(autoflush=True, autocommit=False)
DBSession = sao.scoped_session(maker)


class Base(object):
    """
       Extiende de la Clase Base
    - Provee una buena representacion cuando una instancia de una clase
    es impresa
    """

    def __repr__(self):
        return "%s(%s)" % ((self.__class__.__name__),
                           ', '.join(["%s=%r" % (key, getattr(self, key))
                                      for key in sorted(self.__dict__.keys())
                                      if not key.startswith('_')]))

DeclarativeBase = sad.declarative_base(cls=Base)
metadata = DeclarativeBase.metadata


def init_model(engine):
    """Llamame antes de usar cualquiera de las tablas o clases en el modelo """
    DBSession.configure(bind=engine)


class Usuarios(DeclarativeBase):
    """"""
    __tablename__ = "usuario"

    id = sa.Column(sa.Integer, primary_key=True)
    nombre = sa.Column(sa.Unicode(50))
    apellido = sa.Column(sa.Unicode(50))
    categoria = sa.Column(sa.Unicode)
    cuil = sa.Column(sa.Unicode(11))
    password = sa.Column(sa.Unicode, nullable=False)
    profesion = sa.Column(sa.Unicode(50))

    @hybrid_property  # Devuelve datos ya Calculados - Se puede usar Consultas
    def usuario(self):
        return "%s %s" % (self.persona.nombre, self.persona.apellido)


class Pasajero(DeclarativeBase):
    """"""
    __tablename__ = "pasajero"

    id = sa.Column(sa.Integer, primary_key=True)
    nombre = sa.Column(sa.Unicode(50))
    apellido = sa.Column(sa.Unicode(50))
    documento_tipo = sa.Column(sa.Integer)
    documento_numero = sa.Column(sa.Unicode(15))
    estado_civil = sa.Column(sa.Integer)
    ocupacion = sa.Column(sa.Unicode(50))
    domicilio = sa.Column(sa.Unicode(80))
    telefono = sa.Column(sa.Integer)
    mail = sa.Column(sa.Unicode(50))
    nacimiento = sa.Column(sa.Date)
    observaciones = sa.Column(sa.Unicode(300))
    pais = sa.Column(sa.Integer, sa.ForeignKey("pais.id"))
    provincia = sa.Column(sa.Integer, sa.ForeignKey("provincia.id"))
    localidad = sa.Column(sa.Integer, sa.ForeignKey("localidad.id"))


class CtaCte(DeclarativeBase):
    """"""
    __tablename__ = "ctacte"

    id = sa.Column(sa.Integer, primary_key=True)
    nombre = sa.Column(sa.Unicode(50))
    domicilio = sa.Column(sa.Unicode(50))
    cuit = sa.Column(sa.Unicode(13))
    observaciones = sa.Column(sa.Unicode(300))
    codigopostal = sa.Column(sa.Integer)
    ivatipo = sa.Column(sa.Integer)
    telefono = sa.Column(sa.Integer)
    fechalta = sa.Column(sa.Date)
    provincia = sa.Column(sa.Integer, sa.ForeignKey("provincia.id"))
    localidad = sa.Column(sa.Integer, sa.ForeignKey("localidad.id"))


class Pais(DeclarativeBase):
    """Tabla Pais"""
    __tablename__ = "pais"
    id = sa.Column(sa.Integer, primary_key=True)
    nombre = sa.Column(sa.Unicode)
    # OneToMany a Provincia
    relacion_provincia = sao.relationship("Provincia")

    def __repr__(self):
        """"""
        return repr(self.nombre)


class Provincia(DeclarativeBase):
    """"""
    __tablename__ = "provincia"
    id = sa.Column(sa.Integer, primary_key=True)
    nombre = sa.Column(sa.Unicode)
    pais_id = sa.Column(sa.Integer, sa.ForeignKey('pais.id'))
    # OneToMany a Localidad
    relacion_localidad = sao.relationship("Localidad")

    def __repr__(self):
        """"""
        return repr(self.nombre)


class Localidad(DeclarativeBase):
    """"""
    __tablename__ = "localidad"

    id = sa.Column(sa.Integer, primary_key=True)
    nombre = sa.Column(sa.Unicode)
    fk_provincia = sa.Column(sa.Integer, sa.ForeignKey('provincia.id'))

    def __repr__(self):
        """"""
        return repr(self.nombre)


class Registro(DeclarativeBase):
    """"""
    __tablename__ = "registro"

    id = sa.Column(sa.Integer, primary_key=True)
    pasajero_id = sa.Column(sa.Integer, sa.ForeignKey("pasajero.id"))
    fecha_ingreso = sa.Column(sa.Date)
    fecha_egreso = sa.Column(sa.Date)
    hora_ingreso = sa.Column(sa.Time)
    hora_egreso = sa.Column(sa.Time)
    nrohabitacion = sa.Column(sa.Integer)


class Articulos(DeclarativeBase):
    """"""
    __tablename__ = "articulos"

    id = sa.Column(sa.Integer, primary_key=True)
    rubro = sa.Column(sa.Unicode(100))
    articulo = sa.Column(sa.Unicode(100))
    precio = sa.Column(sa.Float)
    stock = sa.Column(sa.Integer)
    descripcion = sa.Column(sa.Unicode(100))
