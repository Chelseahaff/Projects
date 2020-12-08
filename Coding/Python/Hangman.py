def hangman(word):
	word_list = ["python", "java", "computer", "hacker", "painter"]
        random_number = random.randint(0, 4)
        word=word_list[random_number]
        wrong=0
	stages=  ["",
		 "_______       ",
		 "|             ",
		 "|      |      ",
		 "|      O      ",
		 "|     /|\     ",
		 "|     / \     ",
		 "|             "
		  ]
	rletters= list(word)
	board= ["_"] * len(word)
	win = false
	print("Welcome to Hangman")

	
>>> while wrong < len(stages) -1:
	print("\n")
	msg= "Guess a letter"
	char= input(msg)
	if char in rletters:
		cind= rletters.index(char)
		board[cind]= '$'
	else:
		wrong += 1
	print((" ".join(board)))
	e = wrong + 1
	print("\n".join(stages[0: e]))
	if "_" not in board:
		print("You Win!")
		print(" ".join(board))
		win = true
		break
	if not win:
		print("\n".join(stages[0: wrong]))
		print("You lose! It was {}.".format(word))

	
