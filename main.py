import random
import json
import datetime

current_time = datetime.datetime.now()
print(current_time)
secret = random.randint(1,30)
attempts = 0
name = input("Enter your name:")
wrong_guesses = []

with open("score.txt","r") as score_file:
    score_list = json.loads(score_file.read())
    score_data = {"attempts":attempts, "date":datetime.datetime.now(), "name":name, "secret":secret}
    score_top = sorted(score_list, key=lambda i: i["attempts"])[:3]
    print("Top 3 results are:")
    for score in score_top:
        print(str(score))

for score_dict in score_list:
     print("Player " +score_dict.get("name") + " had " + str(score_dict.get("attempts")) + " attempts" + " at date " + score_dict.get("date") + " when secret number was " + str(score_dict.get("secret")))


while True:

    guess = int(input("Guess the secret number between 1 and 30:"))
    attempts = attempts + 1

    if guess == secret:
        score_list.append({"attempts":attempts, "date":str(datetime.datetime.now(),), "name":name, "secret":secret, "wrong_guesses":wrong_guesses})

        with open("score.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
            print("You have guessed it correctly. Congrats!")
            print("Attempts needed: " + str(attempts))
            print("Wrong guesses are: " + str(wrong_guesses))
        break
    elif guess > secret:
        print("Your guess is not correct. Try something smaller.")
        wrong_guesses.append(guess)
    elif guess < secret:
        print("Your guess is not correct. Try something bigger.")
        wrong_guesses.append(guess)