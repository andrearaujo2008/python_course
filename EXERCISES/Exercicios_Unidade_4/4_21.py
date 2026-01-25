# Importando a biblioteca data.
import datetime

# Pegando a hora atual do sistema.
hora = datetime.datetime.now()

# Formato da hora de 12 horas.
formato_hora = hora.strftime(" %I:%M%p")

# Mostrar o resultado.
print(f" A hora atual é:{formato_hora}")
