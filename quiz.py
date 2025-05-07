import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random
lifeline_used = False
pygame.mixer.init()
pygame.mixer.music.load("Audio/background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

questions = {
    "Easy": [
        {"question": "What is the fastest land animal?", "options": ["Cheetah", "Lion", "Horse", "Eagle"], "answer": "Cheetah"},
        {"question": "Which animal is known as the king of the jungle?", "options": ["Tiger", "Lion", "Elephant", "Gorilla"], "answer": "Lion"},
        {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippo"], "answer": "Blue Whale"},
        {"question": "Which bird is a universal symbol of peace?", "options": ["Dove", "Eagle", "Sparrow", "Owl"], "answer": "Dove"},
        {"question": "What do pandas mainly eat?", "options": ["Bamboo", "Meat", "Fruits", "Grass"], "answer": "Bamboo"},
        {"question": "What is the tallest land animal?", "options": ["Elephant", "Giraffe", "Ostrich", "Camel"], "answer": "Giraffe"},
        {"question": "Which animal is small, hops, and loves carrots?", "options": ["Rabbit", "Kangaroo", "Hare", "Squirrel"], "answer": "Rabbit"},
        {"question": "What do cats love to chase?", "options": ["Dogs", "Mice", "Birds", "Fish"], "answer": "Mice"},
        {"question": "Which animal barks?", "options": ["Cat", "Dog", "Cow", "Horse"], "answer": "Dog"},
        {"question": "What do fish breathe with?", "options": ["Gills", "Lungs", "Nose", "Mouth"], "answer": "Gills"},
        {"question": "Which animal is famous for having a long trunk?", "options": ["Elephant", "Giraffe", "Horse", "Camel"], "answer": "Elephant"},
        {"question": "What is a baby sheep called?", "options": ["Lamb", "Kid", "Calf", "Foal"], "answer": "Lamb"},
        {"question": "Which animal lives in a shell?", "options": ["Crab", "Fish", "Octopus", "Whale"], "answer": "Crab"},
        {"question": "What is a baby kangaroo called?", "options": ["Cub", "Joey", "Calf", "Pup"], "answer": "Joey"},
        {"question": "Which animal is known as man's best friend?", "options": ["Cat", "Dog", "Elephant", "Parrot"], "answer": "Dog"},
        {"question": "What is a baby dog called?", "options": ["Puppy", "Cub", "Calf", "Foal"], "answer": "Puppy"},
        {"question": "Which animal is famous for its black-and-white fur?", "options": ["Tiger", "Zebra", "Panda", "Dalmatian"], "answer": "Panda"},
        {"question": "Which bird is known for its ability to mimic human speech?", "options": ["Parrot", "Crow", "Eagle", "Sparrow"], "answer": "Parrot"},
        {"question": "Which animal has black and white stripes?", "options": ["Tiger", "Zebra", "Giraffe", "Leopard"], "answer": "Zebra"},
        {"question": "What do bees produce?", "options": ["Milk", "Honey", "Wax", "Silk"], "answer": "Honey"},
        {"question": "What do frogs start their life as?", "options": ["Egg", "Fish", "Tadpole", "Baby Frog"], "answer": "Tadpole"}
    ],
    "Medium": [
        {"question": "What is the only mammal capable of true flight?", "options": ["Bat", "Owl", "Flying Squirrel", "Eagle"], "answer": "Bat"},
        {"question": "Which animal is known to laugh when tickled?", "options": ["Monkey", "Hyena", "Rat", "Dolphin"], "answer": "Rat"},
        {"question": "What is the only marsupial found in North America?", "options": ["Kangaroo", "Koala", "Opossum", "Wombat"], "answer": "Opossum"},
        {"question": "Which animal is known as the Ship of the Desert?", "options": ["Horse", "Camel", "Elephant", "Donkey"], "answer": "Camel"},
        {"question": "Which bird lays the largest egg?", "options": ["Eagle", "Penguin", "Ostrich", "Duck"], "answer": "Ostrich"},
        {"question": "Which bird cannot fly?", "options": ["Eagle", "Parrot", "Penguin", "Owl"], "answer": "Penguin"},
        {"question": "Which animal is the largest land carnivore?", "options": ["lion", "Polar Bear", "Tiger", "Wolf"], "answer": "Polar Bear"},
        {"question": "What is the slowest animal in the world?", "options": ["Snail", "Sloth", "Turtle", "Koala"], "answer": "Sloth"},
        {"question": "Which sea creature has three hearts?", "options": ["Octopus", "Dolphin", "Shark", "Starfish"], "answer": "Octopus"},
        {"question": "Which animal has the strongest bite force?", "options": ["Lion", "Tiger", "Crocodile", "Hippopotamus"], "answer": "Crocodile"},
        {"question": "What is the only bird that can fly backward?", "options": ["Hummingbird", "Eagle", "Ostrich", "Penguin"], "answer": "Hummingbird"},
        {"question": "Which mammal lays eggs?", "options": ["Platypus", "Kangaroo", "Koala", "Opossum"], "answer": "Platypus"},
        {"question": "What is the largest living primate?", "options": ["Gorilla", "Orangutan", "Chimpanzee", "Bonobo"], "answer": "Gorilla"},
        {"question": "What is the largest species of penguin?" , "options": ["Emperor Penguin", "King Penguin", "Gentoo Penguin", "Adelie Penguin"], "answer": "Emperor Penguin"},
        {"question": "Which animal has the longest pregnancy?" , "options": ["Elephant", "Blue Whale", "Giraffe", "Orca"], "answer": "Elephant"},
        {"question": "Which animal can sleep standing up but can’t dream unless it lies down?" , "options": ["Horse", "Cow", "Elephant", "Giraffe"], "answer": "Horse"},
        {"question": "Which insect has been around for over 300 million years?" , "options": ["Btterfly", "Dragonfly", "Beetle", "Ant"], "answer": "Dragonfly"},
    ],
    "Hard": [
        {"question": "Which animal is known for changing its color for camouflage?", "options": ["Octopus", "Chameleon", "Peacock", "Jellyfish"], "answer": "Chameleon"},
        {"question": "What is the only marsupial found in North America?", "options": ["Kangaroo", "Koala", "Opossum", "Wombat"], "answer": "Opossum"},
        {"question": "Which animal can survive being frozen solid and thawed back to life?", "options": ["Wood Frog", "Turtle", "Snake", "Fish"], "answer": "Wood Frog"},
        {"question": "Which creature has the highest voltage electric shock?", "options": ["Electric Eel", "Electric Ray", "Electric Catfish", "Electric Skate"], "answer": "Electric Eel"},
        {"question": "What is the only bird known to have nostrils at the tip of its beak?", "options": ["Pelican", "Kiwi", "Toucan", "Puffin"], "answer": "Kiwi"},
        {"question": "Which animal has the most powerful punch in the animal kingdom?", "options": ["Gorilla", "Kangaroo", "Elephant", "Mantis Shrimp"], "answer": "Mantis Shrimp"},
        {"question": "Which mammal has the longest gestation period?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "Elephant"},
        {"question": "What is the world's smallest reptile?", "options": ["Chameleon", "Gecko", "Anole", "Leaf-tailed Gecko"], "answer": "Anole"},
        {"question": "Which animal has fingerprints nearly identical to humans, often confusing crime scene investigators?", "options": ["Chimpanzee", "Gorilla", "Orangutan", "Bonobo"], "answer": "Koala"},
        {"question": "Which fish is known to create underwater crop circles as part of its mating ritual?", "options": ["Pufferfish", "Angelfish", "Clownfish", "Parrotfish"], "answer": "Pufferfish"},
        {"question": "Which animal can hold its breath the longest?", "options": ["Elephant Seal", "Whale", "Dolphin", "Sea Otter"], "answer": "Elephant Seal"},
        {"question": "Which animal's blood is used to detect bacterial contamination in medicine?", "options": ["Horseshoe Crab", "Lobster", "Crab", "Shrimp"], "answer": "Horseshoe Crab"},
        {"question": "What is the only venomous primate in the world?", "options": ["Lemur", "Tarsier", "Loris", "Slow Loris"], "answer": "Slow Loris"},
        {"question": "Which animal has the highest blood pressure?", "options": ["Giraffe", "Elephant", "Horse", "Human"], "answer": "Giraffe"},
        {"question": "Which mammal lays eggs instead of giving birth to live young?", "options": ["Platypus", "Kangaroo", "Koala", "Opossum"], "answer": "Platypus"},
        {"question": "What is the rarest big cat species in the wild?", "options": ["Tiger", "Lion", "Jaguar", "Snow Leopard"], "answer": "Snow Leopard"},
        {"question": "Which animal is known to be biologically immortal?", "options": ["Lobster", "Turtle", "Whale", "Shark"], "answer": "Jellyfish"},
        {"question": "What animal has the strongest bite force in the world?", "options": ["Lion", "Tiger", "Crocodile", "Hippopotamus"], "answer": "Crocodile"},
        {"question": "Which bird can fly the longest distance without stopping?", "options": ["Albatross", "Eagle", "Pigeon", "Sparrow"], "answer": "Albatross"},
        {"question": "What type of animal is a gavial?", "options": ["Fish", "Bird", "Reptile", "Mammal"], "answer": "Reptile"},
        {"question": "Which animal has the most teeth?", "options": ["Snail", "Crocodile", "Shark", "Dolphin"], "answer": "Snail"},
        {"question": "Which animal has the largest eyes relative to its body size?", "options": ["Owl", "Chameleon", "Tarsier", "Lemur"], "answer": "Tarsier"},
        {"question": "What is the largest living primate?", "options": ["Gorilla", "Orangutan", "Chimpanzee", "Bonobo"], "answer": "Gorilla"},
        {"question": "Which animal has the longest tongue relative to its body size?", "options": ["Chameleon", "Anteater", "Frog", "Snake"], "answer": "Chameleon"},
        {"question": "What is the smallest mammal in the world?", "options": ["Bat", "Mouse", "Shrew", "Rat"], "answer": "Shrew"},
        {"question": "Which animal is known as the ghost of the mountains?", "options": ["Snow Leopard", "Polar Bear", "Arctic Fox", "Yeti"], "answer": "Snow Leopard"},
        {"question": "What is the largest living reptile?", "options": ["Snake", "Lizard", "Crocodile", "Turtle"], "answer": "Crocodile"},
        {"question": "Which animal has the longest neck?", "options": ["Elephant", "Giraffe", "Ostrich", "Camel"], "answer": "Giraffe"},
    ],
}

current_difficulty = ""
current_question_index = 0
score = 0
time_left = 10
timer_id = None

root = tk.Tk()
root.title("Animal Quiz Game")
root.geometry("626x417")
root.resizable(False, False)

bg_image = Image.open("Photos/background.png").resize((626, 417))
bg_photo = ImageTk.PhotoImage(bg_image)
title_image = Image.open("Photos/title.png").resize((350, 150))
title_photo = ImageTk.PhotoImage(title_image)

gold_badge = Image.open("Photos/Gold.png").resize((100,100))
gold_badge_photo = ImageTk.PhotoImage(gold_badge)

silver_badge = Image.open("Photos/Silver.png").resize((100,100))
silver_badge_photo = ImageTk.PhotoImage(silver_badge)

bronze_badge = Image.open("Photos/Bronze.png").resize((100,100))
bronze_badge_photo = ImageTk.PhotoImage(bronze_badge)

def load_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            scores = [line.strip().split(": ") for line in file.readlines()]
            scores = [(name, int(score)) for name, score in scores]
            scores.sort(key=lambda x: x[1], reverse=True)
    except FileNotFoundError:
        scores = []

    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=626, height=417, highlightthickness=0)
    canvas.place(x=0, y=0)

    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    tk.Label(root, text="🏆 Top 5 Scorers", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

    for i, (name, score) in enumerate(scores[:5]):
        tk.Label(root, text=f"{i+1}. {name}: {score}", font=("Arial", 10), bg="white").pack()

    back_button = tk.Button(root, text="Back to Home", font=("Arial", 14), bg="gray", fg="white", width=12, height=2, command=load_home_page)
    back_button.pack(side="bottom", pady=20, anchor="center")

leaderboard_button = tk.Button(root, text="Leaderboard", font=("Arial", 14), bg="gray", fg="white", width=12, height=2, command=load_leaderboard)
leaderboard_button.pack(pady=20)



def set_volume(value):
    volume = float(value) / 100
    pygame.mixer.music.set_volume(volume)


def load_settings_page():
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=626, height=417, highlightthickness=0)
    canvas.place(x=0, y=0)

    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    tk.Label(root, text="Game Volume", font=("Arial", 14), bg="white").pack(pady=10)
    volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=set_volume)
    volume_slider.set(pygame.mixer.music.get_volume() * 100)
    volume_slider.pack(pady=10)

    tk.Label(root, text="Credits", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
    tk.Label(root, text="Developer: Erica Hermosada", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
    tk.Label(root, text="The Animal Quiz Game is an interactive and educational\n"
                        "application designed to test and enhance users' knowledge\n"
                        "about various animals.", font=("Arial", 12), bg="white", justify="center").pack(pady=10)

    back_button = tk.Button(root, text="Back to Home", font=("Arial", 14), bg="gray", fg="white", width=12, height=2, command=load_home_page)
    back_button.pack(pady=20)




def load_home_page():
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=626, height=417, highlightthickness=0)
    canvas.place(x=0, y=0)

    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    canvas.create_image(150, 100, image=title_photo, anchor="nw")

    start_button = tk.Button(root, text="Start Game", font=("Arial", 14), bg="lightblue", fg="black",
                             command=load_quiz_page, width=12, height=2)
    start_button.place(x=250, y=300)

    leaderboard_button = tk.Button(root, text="🏆 Leaderboard", font=("Arial", 12), bg="gold", fg="black",
                                   command=load_leaderboard)
    leaderboard_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    settings_button = tk.Button(root, text="⚙️", font=("Arial", 14), bg="gray", fg="white",
                                command=load_settings_page)
    settings_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

def load_quiz_page():
    for widget in root.winfo_children():
        widget.destroy()
    
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    difficulty_label = tk.Label(root, text="Select Difficulty", font=("Arial", 20, "bold"), bg="white")
    difficulty_label.pack(pady=20)

    tk.Button(root, text="Easy", font=("Arial", 14), bg="green", fg="white", width=12, height=2,
              command=lambda: start_game("Easy")).pack(pady=10)
    tk.Button(root, text="Medium", font=("Arial", 14), bg="orange", fg="white", width=12, height=2,
              command=lambda: start_game("Medium")).pack(pady=10)
    tk.Button(root, text="Hard", font=("Arial", 14), bg="red", fg="white", width=12, height=2,
              command=lambda: start_game("Hard")).pack(pady=10)
    
    tk.Button(root, text="Back", font=("Arial", 14), bg="gray", fg="white", width=12, height=2,
              command=load_home_page).pack(pady=20)

def start_game(difficulty):
    global current_difficulty, current_question_index, score
    current_difficulty = difficulty
    current_question_index = 0
    score = 0

    random.shuffle(questions[current_difficulty])

    load_question()

def use_fifty_fifty(correct_answer, buttons, lifeline_button):
    global lifeline_used

    if lifeline_used:
        return

    wrong_answers = [btn for btn in buttons if btn.cget("text") != correct_answer]

    if len(wrong_answers) > 2:
        to_remove = random.sample(wrong_answers, 2)
        for btn in to_remove:
            btn.config(state=tk.DISABLED)

    lifeline_button.config(state=tk.DISABLED)
    lifeline_used = True

def load_question():
    global time_left, timer_id, lifeline_used
    if timer_id:
        root.after_cancel(timer_id)

    for widget in root.winfo_children():
        widget.destroy()

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    question_data = questions[current_difficulty][current_question_index]
    question_text = question_data["question"]
    options = question_data["options"]

    tk.Label(root, text=question_text, font=("Arial", 16, "bold"), bg="white").pack(pady=20)

    random.shuffle(options)

    option_buttons = []

    for option in options:
        btn = tk.Button(root, text=option, font=("Arial", 14), width=20, height=2,
                  command=lambda o=option: check_answer(o)) 
        btn.pack(pady=5)
        option_buttons.append(btn)

    lifeline_button = tk.Button(root, text="50-50", font=("Arial", 14), bg="purple", fg="white", width=12, height=2,
                            command=lambda: use_fifty_fifty(question_data["answer"], option_buttons, lifeline_button))
    lifeline_button.place(x=450, y=200)

    if lifeline_used:
        lifeline_button.config(state=tk.DISABLED)

    time_left = 10
    global timer_label
    timer_label = tk.Label(root, text=f"Time Left: {time_left}s", font=("Arial", 14), fg="red", bg="white")
    timer_label.pack(pady=10)
    
    update_timer()

def update_timer():
    global time_left, timer_id
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left}s")
        timer_id = root.after(1000, update_timer)
    else:
        check_answer(None)

def check_answer(selected_option):
    global score, current_question_index
    correct_answer = questions[current_difficulty][current_question_index]["answer"]
    if selected_option == correct_answer:
        score += 1

    next_question()

def next_question():
    global current_question_index
    current_question_index += 1

    if current_question_index < len(questions[current_difficulty]):
        load_question()
    else:
        show_score()

def show_score():
    for widget in root.winfo_children():
        widget.destroy()

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(root, text=f"Your Score: {score}/{len(questions[current_difficulty])}", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

    tk.Label(root, text="Enter Your Name:", font=("Arial", 14), bg="white").pack(pady=5)
    name_entry = tk.Entry(root, font=("Arial", 14))
    name_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), width=12, height=2, command=lambda: save_score(name_entry.get()))
    submit_button.pack(pady=10)

    total_questions = len(questions[current_difficulty])
    if score == total_questions:
        badge_img = gold_badge_photo
    elif score >= total_questions // 2:
        badge_img = silver_badge_photo
    else:
        badge_img = bronze_badge_photo

    badge_label = tk.Label(root, image=badge_img, bg="white")
    badge_label.pack(pady=10)

def save_score(name):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score}\n")
    load_home_page()


def on_close():
    pygame.mixer.music.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

load_home_page()
root.mainloop()
