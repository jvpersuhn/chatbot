from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Bot teste")

trainer = ListTrainer(chatbot)

trainer.train([
    "Ola",
    "Bom dia como posso ajudar?",
])
trainer.train([
    "Gostaria de marcar uma consulta",
    "Certo, qual seria a especialidade?",
])
trainer.train([
    "Pediatria",
    "Temos os seguintes medicos disponiveis: Medico1, Medico2, Medico3",
])
trainer.train([
    "Cardiologia",
    "Temos os seguintes medicos disponiveis: Medico1, Medico2, Medico3",
])
trainer.train([
    "Ortopedista",
    "Temos os seguintes medicos disponiveis: Medico1, Medico2, Medico3",
])
trainer.train([
    "Medico1",
    "Temos as seguintes datas: 10/10/2023 - 11:00, 11/10/2023 - 11:00, 12/10/2023 - 11:00",
])
trainer.train([
    "Medico2",
    "Temos as seguintes datas: 10/10/2023 - 15:00, 11/10/2023 - 15:00, 12/10/2023 - 15:00",
])
trainer.train([
    "Medico3",
    "Temos as seguintes datas: 10/10/2023 - 08:00, 11/10/2023 - 08:00, 12/10/2023 - 08:00",
])

exit_conditions = ("0", "sair")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(chatbot.get_response(query))
