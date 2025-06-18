from datetime import datetime 

def criar_evento(nome, data_hora_str):
    return {
        'nome': nome,
        'data_hora': datetime.strptime(data_hora_str, '%Y-%m-%d %H:%M')
    }

def organizar_eventos(eventos):
    if len(eventos) <= 1:
        return eventos
    else:
        pivo_data_hora = eventos[len(eventos) // 2]['data_hora']

        menores = [evento for evento in eventos if evento['data_hora'] < pivo_data_hora]
        iguais = [evento for evento in eventos if evento['data_hora'] == pivo_data_hora]
        maiores = [evento for evento in eventos if evento['data_hora'] > pivo_data_hora]
        
        return organizar_eventos(menores) + iguais + organizar_eventos(maiores)

eventos_desordenados = [
    criar_evento("Evento 1", "2025-06-20 10:00"),
    criar_evento("Evento 2", "2025-06-18 09:00"),
    criar_evento("Evento 3", "2025-06-20 13:00"),
    criar_evento("Evento 4", "2025-06-19 14:30"),
    criar_evento("Evento 5", "2025-06-18 15:00")
]

eventos_ordenados = organizar_eventos(eventos_desordenados)

print("\nEventos ordenados por data e hora:") 
for evento in eventos_ordenados: 
    print(f"  {evento['nome']}: {evento['data_hora']}")