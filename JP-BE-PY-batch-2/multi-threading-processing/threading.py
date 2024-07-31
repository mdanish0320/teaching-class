import threading
import time

def walk_dog(first, last):
   time.sleep(8)
   print(f"You finish walking {first} {last}")

def take_out_trash():
   time.sleep(2)
   print("You take out the trash")

def get_mail():
   time.sleep(4)
   print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore2.join()
print("chore_1")
chore3.join()
print("chore_2")
chore1.join()
print("chore_3")

print("All chores are complete!")