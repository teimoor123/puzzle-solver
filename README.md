Introduction: Problem Domain

Puzzle solving is a typically human activity that, in recent decades, has been explored in the context of computers. There are many
potential benefits to this. For example, we can offload some puzzle-solving tasks to computers, we may better understand human
puzzle-solving by programming computer puzzle solvers, or we might generate novel puzzles using a computer program.

This project investigates a class of puzzles that have the following features in common:

full information: all information about the puzzle state at any given point is visible to the solver; there are no hidden or random aspects.

well-defined extensions: a definition of legal "extensions" from a given puzzle state to new states is given.

well-defined solution: a definition of what it means for the puzzle to be in a solved state is given.

These features are common to a very large class of puzzles: crosswords, sudoku, peg solitaire, verbal arithmetic, and so on, This
project generalizes the required features into an abstract superclass Puzzle and solving such puzzles is written in terms of this abstract class.

Particular concrete puzzles can be modelled as subclasses of Puzzle and solved using the solve method of a subclass of the solver abstract class, which will be described later.

Although there may be faster puzzle-specific solvers for a particular puzzle that take advantage of specific features of that puzzle, the general solvers built are designed to work for all puzzles of this sort.


The Puzzles

We will start by introducing how the puzzles will be represented and what specific puzzles we will consider in this project.

abstract puzzle class:
The abstract class Puzzle has the following methods: which are not implemented, but meant to be implemented in subclasses:

is _solved (abstract): returns True iff the puzzle is in a solved state.

extensions (abstract): returns a list of extensions from the current puzzle state to new states that are a single 'move' away.

fall fast (has a default implementation in Puzzle): returns True if it is clear that the puzzle can never, through a sequence of extensions, move into a solved state.

Note: each subclass will need its own init method in order to represent that particular puzzle's state information.


Sudoku

This puzzle commonly appears in print media and online. We are presented with an n x n grid with some symbols, for example digits
or letters, filled in, The symbols must be from a set of n symbols. The goal is to fill in the remaining symbols in such a way that each
row, column, and V7 X /n subsquare, contains each symbol exactly once. In order for all of that to make sense, n must be a square
integer such as 4, 9, 16, or 25,


Word Ladder

This puzzle involves transforming one word into a target word by changing one letter at a time. Each word must belong to a specified
set of valid words. Here's an example where we assume that the set of valid words is a rather large set of common English words, and
the goal is to get from the word 'cost' to the word 'save":
cost -› cast - case -› cave › save


Expression Tree Puzzle

This puzzle consists of an algebraic equation containing one or more variables, and a target value. The puzzle is solved when the
variables are assigned values such that the expression evaluates to the target value


The Solvers

Now that we know a bit about the puzzles that we will be implementing, we will turn our attention to how we will implement the solvers.

Searching

Solving a puzzle can be done by systematically searching for a solution, starting from its current state. To make this daunting task even possible, we have to be sure that we have a systematic way of exploring all possible puzzle states - without need essly revisiting the same state twice.
We implement two systematic searching techniques.

The implicit tree underlying our search

To understand our searching techniques, it helps to think of the tree that is defined by all the possible states of a puzzle: each node is one puzzle state, the root is the initial state of the puzzle, and the children of a node are its extensions (puzzle states that are one move away).

When we actually implement the algorithms, we don't need to explicitly form this tree, but it is useful to remember that it is there. 


The search algorithms

Depth-first search and breadth-first search are two approaches to searching through the space of possibilities for a solution.
With depth-first search, we search deeply before we search broadly. We exhaustively search the first subtree before considering any
other subtree, And we use the same strategy when we search that subtree: exhaustively searching its first subtree before considering
any other subtree.

With breadth-first search, we search broadly before we search deeply. We consider all puzzle states at depth 1, then all puzzle states
at depth 2, and so on until we have searched all puzzle states in our tree. A queue is helpful for keeping track of puzzles states to be checked when their turn comes. Because we consider states that are "closer" to the starting state before those that are "farther", we are guaranteed to find the shortest path to a puzzle's solution.

For both solvers, we run the risk of encountering a puzzle state that we've already seen, and which already failed to produce a solution. To avoid exploring that state all over again, we will keep track of states we've seen before and just ignore them if we encounter them
again.

For certain puzzle types, we might also be able to check whether we can quickly tell if a puzzle state is unsolvable, Such a check can
be incorporated into our search algorithms we do so in our implementation.

The Solver Class

The abstract class solver defines the interface for the following method:

solve: returns a path to a solution of a given puzzle, This method is abstract and must be implemented in a subclass.

We create two subclasses of the solver class - dfssolver, which uses the depth first search strategy in its implementation of
solve, and Bfssolver, which uses the breadth first search strategy in its implementation of solve


Note: Some of the files were provided in full by my professor. I am responsible for completing the following files:

sudoku_puzzle.py: implemented the fail_fast() and has_unique_solution() methods in the SudokuPuzzle subclass.

solver.py: implemented DfsSolver and BfsSolver sublclasses and the helper functions.

word_ladder_puzzle.py: implemented the ___str___(), ___eq___(), extensions(), is_solved(), and get_difficulty() methods in the WordLadderPuzzle sublass.

expression_tree.py: implemented the construct_from_list function and all the methods in the ExprTree class except the Visualize() method.

expression_tree_puzzle.py: implemented the ExpressionTreePuzzle sublass.

