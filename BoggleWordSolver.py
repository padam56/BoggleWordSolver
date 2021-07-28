class Tree():
    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.leaf = False

    # Add a word, letter by letter
    def add(self, word):
        if len(word):
            letter = word[0] # Set the letter to be the first letter of the current word so far &
            word = word[1:]  # Truncating the word to be beginning from the next letter.
            if letter not in self.children:
                self.children[letter] = Tree(letter)
            return self.children[letter].add(word)
        else:
            self.leaf = True
            return self
    
    # Locate a letter in the tree
    def search(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter] # return the tree node representing the next letter

# Function for the actual word solver
def findWord(board, tree, validated, row, col, path=None, currLetter=None, word=None):
    letter = board[row][col]
    if path is None or currLetter is None or word is None:
        currLetter = tree.search(letter)
        path = [(row, col)]
        word = letter
    else:
        currLetter = currLetter.search(letter)
        path.append((row, col))
        word = word + letter
    
    # Base Cases
    if currLetter is None:
        return
    if currLetter.leaf:
        validated.add(word)

    # Recursive call
    for r in range(row-1, row+2): # r will go from row-1 -> row -> row+1
        for c in range(col-1, col+2):
            if (r>=0 and r<4 and c>=0 and c<4 and r != row and c != col and (r,c)):
                findWord(board, tree, validated, r, c, path[:], currLetter, word[:] ) # Taking the entire path and the entire word

def main():

    # Initialize game board based on user input
    board = [] # 2D matrix
    for i in range(0,4): # 4x4 grid
        #append empty row
        board.append([])
        for j in range(0,4):
            board[i].append(input().strip().upper()) #Removes both leading and trailing characters (spaces)

    # Print board
    for i in range(0,4):
        for j in range(0,4):
            print(board[i][j], end = " ")
        print()

    #Load dictionary-yawl.txt (yet another word list)
    dict = open('dictionary-yawl.txt', 'r')
    
    tree = Tree()
    for line in dict:
        word = line.rstrip().upper() # Removes only trailing characters
        tree.add(word)

    # Set to store strings that match valid words found in the dictionary
    validated = set()

    # Call the findWord function from each grid
    for row in range(0,4):
        for col in range(0,4):
            findWord(board, tree, validated, row, col)

    # Print out valid words
    for word in sorted(validated):
        if len(word) > 2:
            print(word)
main()