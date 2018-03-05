'''
Created on 25/07/2013

@author: otiuqx
'''

import modelos.modelo as db
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func


def conectaraBD():
    """
    Conectarse a Postgresql y devolver la Session al objeto
    """
    engine = db.sa.create_engine('postgresql+psycopg2://postgres:'
                                 'tfortrue@localhost:5432/hotel', echo=True)
    db.init_model(engine)
    session = db.DBSession()
    setupDatabase(engine)
    return session


def setupDatabase(engine):
    """Configura la BD, esto no afectara las tablas existentes"""
    db.metadata.create_all(engine)  # @UndefinedVariable
    print ("db created")


def obtenerPaises(session):
    result = session.query(db.Pais.nombre).all()
    return result


def obtenerProvincias(session, opcion):
    result = session.query(db.Provincia.nombre).filter_by(pais_id=opcion).all()
    return result


def obtenerLocalidades(session, opcion):
    result = session.query(db.Localidad.nombre).\
        filter_by(fk_provincia=opcion).all()

    return result


def obtenerPasajeros(session):
    result = session.query(db.Pasajero.id,
                           db.Pasajero.documento_numero,
                           db.Pasajero.nombre,
                           db.Pasajero.apellido,
                           db.Pasajero.observaciones).\
        order_by(db.Pasajero.apellido).all()

    return result


def obtenerCtaCte(session):
    """"""
    result = session.query(db.CtaCte).order_by('id').all()
    return result


def consultaPais(session, p):
    result = session.query(db.Pais.nombre).filter_by(id=p).first()
    return result[0]


def consultaProvincia(session, p):
    result = session.query(db.Provincia.nombre).filter_by(id=p).first()
    return result[0]


def consultaLocalidad(session, l):
    result = session.query(db.Localidad.nombre).filter_by(id=l).first()
    return result[0]


def consultaPasajero(session, codigo):
    result = session.query(db.Pasajero.nombre,
                           db.Pasajero.apellido,
                           db.Pasajero.documento_tipo,
                           db.Pasajero.documento_numero,
                           db.Pasajero.estado_civil,
                           db.Pasajero.ocupacion,
                           db.Pasajero.domicilio,
                           db.Pasajero.telefono,
                           db.Pasajero.mail,
                           db.Pasajero.nacimiento,
                           db.Pasajero.observaciones,
                           db.Pasajero.pais,
                           db.Pasajero.provincia,
                           db.Pasajero.localidad).\
        filter(db.Pasajero.id == int(codigo)).all()
    return result


def consultaCtaCte(session, codigo):
    result = session.query(db.CtaCte.nombre, db.CtaCte.domicilio,
                           db.CtaCte.cuit, db.CtaCte.observaciones,
                           db.CtaCte.codigopostal, db.CtaCte.ivatipo,
                           db.CtaCte.telefono, db.CtaCte.fechalta,
                           db.CtaCte.provincia, db.CtaCte.localidad).\
        filter(db.CtaCte.id == int(codigo)).all()
    return result


def consultaXAyN(session, a):
    try:
        result = session.query(db.Pasajero.id).filter(
            func.lower(db.Pasajero.apellido + str(" ") +
                       db.Pasajero.nombre) == func.lower(a)).first()
        aux = str('%' + a + '%')
        result2 = session.query(db.Pasajero.id).\
            filter(db.Pasajero.apellido.ilike(aux)).first()
        if (result is None) & (result2 is not None):
            result = result2[0]
        elif (result2 is None) & (result is not None):
            result = result[0]
        else:
            result = 0
        return result
    except (NameError, ValueError):
        print ("Ocurrio un error")


def agrmodCtaCte(session, data, codigo=None):
    """Agregar o Editar una Cuenta Corriente"""
    try:
        if codigo is not None:
            ctacte = session.query(db.CtaCte).filter(
                db.CtaCte.id == int(codigo)).one()
        else:
            ctacte = db.CtaCte()

        ctacte.nombre = data["ctacte"]["nombre"]
        ctacte.domicilio = data["ctacte"]["domicilio"]
        ctacte.cuit = data["ctacte"]["cuit"]
        ctacte.observaciones = data["ctacte"]["obs"]
        ctacte.codigopostal = data["ctacte"]["codpos"]
        ctacte.ivatipo = data["ctacte"]["ivatipo"]
        ctacte.telefono = data["ctacte"]["telefono"]
        ctacte.fechalta = data["ctacte"]["falta"]
        ctacte.provincia = data["ctacte"]["provincia"]
        ctacte.localidad = data["ctacte"]["localidad"]

        session.add(ctacte)
    except IntegrityError as e:
        print ("IntegrityError", e)
        session.rollback()

    session.commit()


def agrmodPasajero(session, data, codigo=None):
    """Agregar o Editar un Pasajero"""
    try:
        if codigo is not None:
            pasajero = session.query(db.Pasajero).filter(
                db.Pasajero.id == int(codigo)).one()
        else:
            pasajero = db.Pasajero()

        pasajero.nombre = data["pasajero"]["nombre"]
        pasajero.apellido = data["pasajero"]["apellido"]
        pasajero.documento_tipo = data["pasajero"]["doctipo"]
        pasajero.documento_numero = data["pasajero"]["docnumero"]
        pasajero.estado_civil = data["pasajero"]["ecivil"]
        pasajero.ocupacion = data["pasajero"]["ocupacion"]
        pasajero.domicilio = data["pasajero"]["domicilio"]
        pasajero.telefono = data["pasajero"]["telefono"]
        pasajero.mail = data["pasajero"]["mail"]
        pasajero.nacimiento = data["pasajero"]["nacimiento"]
        pasajero.observaciones = data["pasajero"]["obs"]

        pasajero.pais = data["pasajero"]["pais"]
        pasajero.provincia = data["pasajero"]["provincia"]
        pasajero.localidad = data["pasajero"]["localidad"]

        session.add(pasajero)
    except IntegrityError as e:
        print ("IntegrityError", e)
        session.rollback()

    session.commit()


def obtenerId(session, tipo):
    """"""
    if tipo == 'p':
        result = session.query(db.Pasajero.id).order_by(db.Pasajero.id.desc()
                                                        ).first()
    else:
        result = session.query(db.CtaCte.id).order_by(db.CtaCte.id.desc()
                                                      ).first()
    if result is None:
        result = 1
    else:
        result = result[0] + 1
    return result


def registro(session, data):
    """"""
    try:
        registro = db.Registro()
        registro.fecha_ingreso = data["registro"]["fingreso"]
        registro.hora_ingreso = data["registro"]["hingreso"]
        registro.fecha_egreso = data["registro"]["fegreso"]
        registro.hora_egreso = data["registro"]["hegreso"]
        registro.nrohabitacion = data["registro"]["nrohabitacion"]
        registro.persona_id = data["registro"]["codigo"]

        session.add(registro)

    except IntegrityError as e:
        print ("IntegrityError", e)
        session.rollback()

    session.commit()


def pruebasSQL(session, data):
    """"""
    result = session.query(db.Pasajero.id).filter(
             func.lower(db.Pasajero.apellido + str(" ") +
                        db.Pasajero.nombre) == func.lower(data)).first()
    return result
