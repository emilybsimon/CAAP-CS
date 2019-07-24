from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class CentralCorridor(Scene):
	
	name = "central_corridor"

	def enter(self):
		print ("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
		print("You must rid them of your vesicle")
		return self.action()
		
		
	def action(self):
		print ("What will you do?")
		print ("1. Shoot at them")
		print ("2. Sneak attack")
		print ("3. Tell a joke to break the ice")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		  	choice = int(choice)
		except ValueError:
		  	print("That's not an int!")
		  	return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Quick on the draw you yank out your blaster and fire it at the Gothon.")
			print ("However, you quicky run out of ammo. whoops")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Like a world class boxer you dodge, weave, slip and slide right")
			print ("However, you were quickly spotted because you aren't as stealthy as you assumed. whoops")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Lucky for you they made you learn Gothon insults in the academy.")
			print ("They enjoyed your quick wit.")
			return self.exit_scene('laser_weapon_armory')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
			return self.exit_scene('laser_weapon_armory')
	def exit_scene(self, outcome):
		return outcome

class LaserWeaponArmory(Scene):
	
	name = "laser_weapon_armory"

	def enter(self):
		print ("You do a dive roll into the Weapon Armory, crouch and scan the room")
		print ("You see a box and decide to approach it.")
		return self.action()

	def action(self):
		print ("There's a keypad lock on the box")
		print ("The keypad requires a 3-digit code.")
		code = [int(1),int(3),int(2)]
		guesses = 0
		# loop to check three random integers, one at a time
		for i in range(3):
			print ("Enter digit %d." % (i+1))
			guess = input("[keypad]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			  	guess = int(guess)
			except ValueError:
			  	print("That's not an int!")
			  	return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("BZZZZEDDD!")
				guesses += 1
				guess =input("[keypad]> ")
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				  	guess = int(guess)
				except ValueError:
				  	print("That's not an int!")
				  	guess = -1
		
		if guesses < 10:
			print ("The container clicks open and the seal breaks, letting gas out. You faint.")
			return self.exit_scene('the_temple')
		else:
			print ("The lock buzzes one last time and then you hear a sickening noise")
			print ("You've been struck by a rock and die.")
			return self.exit_scene('death') # raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome

class Temple(Scene):
	
	name ='the_temple'

	def enter(self):
		print("You wake up and you are in a temple.")
		print("An alien is standing on the steps of the temple and approaches you.")
		return self.action()
	
	def action(self):
		print("He speaks a riddle to you in order for you to advance further on the bridge.")
		print("The riddle is as follows: You can drop me from the tallest building and I'll be fine, but if you drop me in water I die. What am I?")
		print ("What do you respond?")
		print ("1. A watch")
		print ("2. A piece of paper")
		print ("3. A balloon")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   	choice = int(choice)
		except ValueError:
		   	print("That's not an int!")
		   	return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You are incorrect.")
			print ("The alien hits you.")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("You are correct.")
			print ("The alien teleports you from the temple.")
			return self.exit_scene('the_spaceship')
		elif int(choice) == 3:
			print ("You are incorrect.")
			print ("The alien hits you.")
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
			return self.exit_scene('the_spaceship')

	def exit_scene(self, outcome):
		return outcome

class SpaceShip(Scene):
	
	name = 'the_spaceship'

	def enter(self):
		print("You are now on an alien space craft. The aliens are conducting an interview with you and prompt you with a question that determines whether you are useful to them or not.")
		return self.action()
	
	def action(self):
		print("The question is: Do you like pineapple on pizza?")
		print ("What do you respond?")
		print ("1. Yes")
		print ("2. No")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		  	choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You are incorrect.")
			print ("The alien hits you.")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("You are correct.")
			print ("The alien deems you useful and transports you to a different lab.")
			return self.exit_scene('the_lab')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene('the_lab')

	def exit_scene(self, outcome):
		return outcome

class Lab(Scene):
	
	name = 'the_lab'

	def enter(self):
		print ("You are now in a laboratory surrounded by aliens.")
		print ("There is now a puzzle in front of you that the aliens want yout to solve.")
		return self.action()

	def action(self):
		print ("The puzzle requires you to choose 1 drink out of 5.")
		good_drink = randint(1,5)
		guess = input("[drink #]> ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
			guess = int(guess)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)
		   
		if int(guess) != good_drink:
			print ("You grab drink %s and chug it."% guess)
			print ("Correct choice. Tasty!")
			return self.exit_scene('the_exit')
		else:
			print ("You grab drink %s and chug it."% guess)
			print ("This was poisoned. Oops.")
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		return outcome

class Exit(Scene):
	
	name = 'the_exit'

	def enter(self):
		print ("You now want to escape.")
		print ("Choose a door to exit.")
		return self.action()

	def action(self):
		print ("There are 3 doors.")
		good_door = randint(1,3)
		guess = input("[door #]> ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
			guess = int(guess)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)
		   
		if int(guess) != good_door:
			print ("You go to door %s and attempt to open it."% guess)
			print ("It opens and you escape to your freedom!")
			return self.exit_scene('finished')
		else:
			print ("You go to door %s and attempt to open it."% guess)
			print ("This was the wrong door. The aliens caught you in the act. Yikes")
			return self.exit_scene('death')

	def exit_scene(self, outcome):
		return outcome

class Finished(Scene):
	name= "finished"