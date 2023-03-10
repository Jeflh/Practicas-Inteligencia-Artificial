import time

class Environment(object):
  def __init__(self,initial): # [True,True]
    self.status = initial
    self.legend = {False:"馃煝 Limpia", True:"馃敶 Sucia"}
      
  def __str__(self):
    output = "\n\t = Estado actual de la casa =\n" + "-" * 50 + "\n"
    output = output + str([f"{self.legend[room]}" for room in self.status])
    return output
  
  def get_environment(self,room): # Devuelve el estado de la habitaci贸n
    return(self.status[room]) 
  
  def set_environment(self,room):
    self.status[room] = False # Limipia la habitaci贸n
    

class ReflexAgent(object):
  def __init__(self,room):
    self.room = room
    self.step = +1   
    self.score = 0
  
  def __str__(self):
    return f"\n馃彔 Habitaci贸n actual: {self.room + 1}"

  def precept_and_act(self,env):
    n = len(env.status)
    cleaned = 0

    print(env)
    print(self)

    if env.get_environment(self.room):
      env.set_environment(self.room)
      self.score += 5
      print(f"\n馃Ч Limpiando habitaci贸n: {self.room + 1}")

    else:
      if self.room + self.step == n: # Si la habitaci贸n es la 煤ltima
        self.step = -1
      elif self.room + self.step == -1: # Si la habitaci贸n es la primera 
        self.step = +1

      self.room = self.room + self.step

    for room in env.status:
      if room == True:
        cleaned = 0
      else:
        cleaned += 1

    if cleaned == n:
      print('-' * 50)
      print(env)
      print("\n\t 鉁旓笍 La casa est谩 limpia 鉁旓笍")
      print(f"\n\t 馃弳 Puntuaci贸n: {self.score}")
      exit()


if __name__ == "__main__":
  house = Environment([True, True, True, True])
  vacuum = ReflexAgent(2)

  while True:
    vacuum.precept_and_act(house)
    print('-' * 50)
    time.sleep(1.5)