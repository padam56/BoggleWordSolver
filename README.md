# BoggleWordSolver

A Boggle Word Solver implemented in Python by defining various functions that loads a 4x4 game board based on input. It recursively searches in all allowed directions for plausible words using Depth First Traversal (backtracking), and then prints out the valid words based on length constraints by cross-checking whether the word exists in the stored dictionary. Here, I'll be storing the dictionary in a retrieval TRIE data structure format which makes more efficient for lookups.