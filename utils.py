import random
import mysql.connector



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

