import random
import mysql.connector

from model import Consulta



def gera_horarios():
    horarios = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30',
                '15:00', '15:30', '16:00', '16:30']

    r = []
    for i in range(0, 5):
        r.append(random.choice(horarios))

    return r


def gravar_consulta(consulta):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="joao1234"
    )

    mycursor = mydb.cursor()

    sql = 'Insert into public.consulta (especialidade,horario,nome,cpf) values (%s, %s,%s, %s)'
    val = (consulta.get_especialidade(), consulta.get_horario(), consulta.get_nome(), consulta.get_cpf())

    mycursor.execute(sql, val)
    mydb.commit()

def recuperar_dados(cpf):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="joao1234",
        database="mysql"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM public.consulta WHERE cpf = %s"
    adr = (cpf,)

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchone()

    consulta = Consulta()

    consulta.set_especialidade(myresult[1])
    consulta.set_horario(myresult[2])
    consulta.set_nome(myresult[3])
    consulta.set_cpf(myresult[4])

    return consulta

def deletar_consulta(cpf):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="joao1234",
        database="mysql"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM public.consulta WHERE cpf = %s"
    adr = (cpf,)

    mycursor.execute(sql, adr)

    mydb.commit()

def alterar_consulta(consulta):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="joao1234",
        database="mysql"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE public.consulta set horario = %s WHERE cpf = %s"
    adr = (consulta.get_horario(), consulta.get_cpf())

    mycursor.execute(sql, adr)

    mydb.commit()


