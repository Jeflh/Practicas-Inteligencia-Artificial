import time

class Environment(object):
  def __init__(self,initial): # [True,True]
    self.status = initial
    self.legend = {False:"🟢 Limpia", True:"🔴 Sucia"}
      
  def __str__(self):
    output = "\n\t = Estado actual de la casa =\n" + "-" * 50 + "\n"
    output = output + str([f"{self.legend[room]}" for room in self.status])
    return output
  
  def get_environment(self,room): # Devuelve el estado de la habitación
    return(self.status[room]) 
  
  def set_environment(self,room):
    self.status[room] = False # Limipia la habitación
    

class ReflexAgent(object):
  def __init__(self,room):
    self.room = room
    self.step = +1   
    self.score = 0
  
  def __str__(self):
    return f"\n🏠 Habitación actual: {self.room + 1}"

  def precept_and_act(self,env):
    n = len(env.status)
    cleaned = 0

    print(env)
    print(self)

    if env.get_environment(self.room):
      env.set_environment(self.room)
      self.score += 5 # Puntuación por limpiar
      print(f"\n🧹 Limpiando habitación: {self.room + 1}")

    else:
      if self.room + self.step == n: # Si la habitación es la última
        self.step = -1
      elif self.room + self.step == -1: # Si la habitación es la primera 
        self.step = +1

      self.score -= 1 # Penalización por moverse
      self.room = self.room + self.step

    for room in env.status:
      if room == True:
        cleaned = 0
      else:
        cleaned += 1

    if cleaned == n:
      print('-' * 50)
      print(env)
      print("\n\t ✔️ La casa está limpia ✔️")
      print(f"\n\t 🏆 Puntuación: {self.score}")
      exit()


if __name__ == "__main__":
  house = Environment([True, True, True, True])
  vacuum = ReflexAgent(2)

  while True:
    vacuum.precept_and_act(house)
    print('-' * 50)
    time.sleep(1.5)