import os
import telebot

from utils import gera_horarios, gravar_consulta
from model import Consulta

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot("6558005428:AAEatQ_hrVQUV0Rv0FqKOWIGXOfmMcHtz3E")

horarios = gera_horarios()
especialidades = ['Pediatria', 'Cardiologia', 'Ortopedista']

consulta = Consulta()

especialidade_escolhida = ''
horario_escolhido = ''
nome = ''
cpf = ''


@bot.message_handler(commands=['comecar'])
def sign_handler(message):
    text = ("Olá, como posso ajudar?\nEscolha uma opção:\n "
            "*1 - Agendamento de consulta\n*"
            "*2 - Cancelamento de Consulta\n*"
            "*3- Remarcação de Consulta\n*"
            "*4 - Endereço e horário de atendimento\n* "
            "*5 - Falar com uma de nossas atendentes\n*"
            "*6 - Finalizar\n*")
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, option_choose)


def option_choose(message):
    option = message.text
    if option == '1':
        sent_msg = bot.send_message(
            message.chat.id, f"Qual seria a especialidade:\n *1 - {especialidades[0]}*\n "
                             f"*2 - {especialidades[1]}*\n *3 - {especialidades[2]}*", parse_mode="Markdown")
        bot.register_next_step_handler(
            sent_msg, escolher_especialidade)
    # elif option == '2':
    #     # cancelamento consulta
    # elif option == '3':
    #     # remarcar consulta
    elif option == '4':
        bot.send_message(message.chat.id, "Nosso Endereço: Rua de Pedra, numero 999 \n"
                                          "Horário de atendimento: só Deus sabe")
    elif option == '5':
        bot.send_message(message.chat.id, "Em breve uma atendente entrara em contato!")
    elif option == '6':
        bot.send_message(message.chat.id, "Obrigado por me utilizar!")
        bot.stop_bot()


def escolher_especialidade(message):
    consulta.set_especialidade(especialidades[(int(message.text)) - 1])
    msg = (f'Escolha entre os horarios disponiveis: *1 - {horarios[0]}*, *2 - {horarios[1]}*, *3 - {horarios[2]}*, '
           f'*4 - {horarios[3]}*, *5 - {horarios[4]}*')
    sent_msg = bot.send_message(message.chat.id, msg, parse_mode="Markdown")

    bot.register_next_step_handler(sent_msg, informar_nome)


def informar_nome(message):
    consulta.set_horario(horarios[int(message.text) - 1])
    msg = 'Informe seu nome: '
    sent_msg = bot.send_message(message.chat.id, msg)

    bot.register_next_step_handler(sent_msg, informar_cpf)


def informar_cpf(message):
    consulta.set_nome(message.text)
    msg = 'Informe seu cpf: '
    sent_msg = bot.send_message(message.chat.id, msg)

    bot.register_next_step_handler(sent_msg, gravar_infos)


def gravar_infos(message):
    consulta.set_cpf(message.text)
    gravar_consulta(consulta)
    text = ("Consulta agendada com sucesso!\nEscolha uma opção:\n "
            "*1 - Agendamento de consulta\n*"
            "*2 - Cancelamento de Consulta\n*"
            "*3- Remarcação de Consulta\n* *4 - Endereço e horário de atendimento\n*"
            "*5 - Falar com uma de nossas atendentes\n*"
            "*6 - Finalizar\n*")
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, option_choose)


bot.infinity_polling()
