numero = int(input("Por favor, entre com o número de segundos que deseja converter: "))

consSeg = 3600
consHr = 86400 

dia = int(numero / consHr)
hora = int((int(numero % consHr)) / consSeg)
minuto = int(int((int(numero % consHr)) % consSeg) / 60)
segundo = int(int((int(numero % consHr)) % consSeg) % 60)

print(dia, "dias,", hora, "horas,", minuto, "minutos e", segundo, "segundos.")
