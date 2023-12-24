"""
This module contains the abstract Solver class and its two subclasses, which
find solutions to puzzles, step by step.
"""

from __future__ import annotations

from typing import List, Optional, Set, Dict

from adts import Queue

from puzzle import Puzzle


class Solver:
    """"
    A solver for full-information puzzles. This is an abstract class
    and purely provides the interface for our solve method.
    """

    # Note the optional parameter seen and its type.
    # Implementations of this method in the two subclasses should use seen
    # to keep track of all puzzle states that you encounter during the
    # solution process.
    def solve(self, puzzle: Puzzle,
              seen: Optional[Set[str]] = None) -> List[Puzzle]:
        """
        Return a list of puzzle states representing a path to a solution of
        <puzzle>. The first element in the list should be <puzzle>, the
        second element should be a puzzle that is in <puzzle>.extensions(),
        and so on. The last puzzle in the list should be such that it is in a
        solved state.

        In other words, each subsequent item of the returned list should take
        the puzzle one step closer to a solution, which is represented by the
        last item in the list.

        Return an empty list if the puzzle has no solution.

        <seen> is either None (default) or a set of puzzle states' string
        representations, whose puzzle states can't be any part of the path to
        the solution.
        """
        raise NotImplementedError

class DfsSolver(Solver):
    """"
    A solver for full-information puzzles that uses
    a depth first search strategy.
    """

    def solve(self, puzzle: Puzzle,
              seen: Optional[Set[str]] = None) -> List[Puzzle]:
        """
        Return a list of puzzle states representing a path to a solution of
        <puzzle>. The first element in the list should be <puzzle>, the
        second element should be a puzzle that is in <puzzle>.extensions(),
        and so on. The last puzzle in the list should be such that it is in a
        solved state.

        In other words, each subsequent item of the returned list should take
        the puzzle one step closer to a solution, which is represented by the
        last item in the list.

        Return an empty list if the puzzle has no solution.

        <seen> is either None (default) or a set of puzzle states' string
        representations, whose puzzle states can't be any part of the path to
        the solution.
        """
        if puzzle.is_solved():
            return [puzzle]
        if seen is None:
            seen = set()
        rslt = [puzzle]
        seen = seen.union({str(puzzle)})
        for extension in puzzle.extensions():
            if str(extension) not in seen and not extension.fail_fast():
                x = self.solve(extension, seen)
                if x != []:
                    rslt.extend(x)
                    return rslt
            seen = seen.union({str(extension)})
        return []

class BfsSolver(Solver):
    """"
    A solver for full-information puzzles that uses
    a breadth first search strategy.
    """

    def solve(self, puzzle: Puzzle, seen: Optional[Set[str]] = None)\
            -> List[Puzzle]:
        """
        Return a list of puzzle states representing a path to a solution of
        <puzzle>. The first element in the list should be <puzzle>, the
        second element should be a puzzle that is in <puzzle>.extensions(),
        and so on. The last puzzle in the list should be such that it is in a
        solved state.

        In other words, each subsequent item of the returned list should take
        the puzzle one step closer to a solution, which is represented by the
        last item in the list.

        Return an empty list if the puzzle has no solution.

        <seen> is either None (default) or a set of puzzle states' string
        representations, whose puzzle states can't be any part of the path to
        the solution.
        """
        if puzzle.is_solved():
            return [puzzle]
        next_state = Queue()
        next_state.enqueue(puzzle)
        paths = {}
        if seen is None:
            seen = set()
        while not next_state.is_empty():
            temp = next_state.dequeue()
            if str(temp) not in seen and not temp.fail_fast():
                x = _ext_checker(temp, next_state, paths, puzzle, seen)
                if x is not None:
                    return x
                seen = seen.union({str(temp)})
        return []
                

#===Helper Functions===

def _list_path(extension: Puzzle, puzzle: Puzzle, paths: Dict) -> List[Puzzle]:
    """
    Return a list starting with extension puzzle and based on paths.
    """
    rslt = [extension]
    while rslt[-1] != puzzle:
        rslt.append(paths[str(extension)])
        extension = paths[str(extension)]
    rslt.reverse()
    return rslt


def _ext_checker(temp: Puzzle, next_state: Queue, paths: Dict, puzzle: Puzzle,
                 seen: set) -> Optional[List[Puzzle], None]:
    """
    Return a list of the path if an extension in temp is solved and add each
    extension puzzle to paths and next_state if not in seen.
    """
    for extension in temp.extensions():
        if str(extension) not in seen:
            next_state.enqueue(extension)
            paths[str(extension)] = temp
            if extension.is_solved():
                return _list_path(extension, puzzle, paths)
    return None


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={'pyta-reporter': 'ColorReporter',
                                'allowed-io': [],
                                'allowed-import-modules': ['doctest',
                                                           'python_ta',
                                                           'typing',
                                                           '__future__',
                                                           'puzzle',
                                                           'adts'],
                                'disable': ['E1136'],
                                'max-attributes': 15}
                        )
