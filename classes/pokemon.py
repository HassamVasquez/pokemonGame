

class Pokemon():
	def __init__(self, data: dict) -> None:
		self.id = data['id']
		self.name = data['name']
		self.type_1 = data['type_1']
		self.type_2 = data['type_2']
		self.hp = data['hp']
		self.attack = data['attack']
		self.generation = data['generation']
		
		self.image_path = f'{self.id}.jpg'
