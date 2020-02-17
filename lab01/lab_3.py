import sys
sys.path.append('/home/neg6/cs344/cs344-code/tools/aima')
sys.path.append('/home/neg6/cs344/cs344-code/tools/paip')
from gps import gps

# Problem is simple maze, 3x3 grid with the start in bottom right corner, finish in the bottom left corner
#   and a blockade in the lower 2 middle spaces
# Maze is below, where X is blockade, O is available, S is starting position and F in finish position
# O O O
# O X O
# F X S

problem = {
    "start": ["0 spaces from start", "blockade left"],
    "finish": ["2 spaces from start", "blockade right"],


    "ops": [
        {
            "action": "move from bottom right to mid right",
            "preconds": [
                "0 spaces from start",
                "blockade left"
            ],
            "add": [
                "1 space from start"
            ],
            "delete": [
                "0 spaces from start"
            ]
        },
        {
            "action": "move from mid right to bottom right",
            "preconds": [
                "1 space from start",
                "blockade left"
            ],
            "add": [
                "0 spaces from start"
            ],
            "delete": [
                "1 space from start"
            ]
        },
        {
            "action": "move from mid right to top right",
            "preconds": [
                "1 space from start",
                "blockade left"
            ],
            "add": [
                "2 spaces from start",
                "no blockade"
            ],
            "delete": [
                "1 space from start",
                "blockade left"
            ]
        },
        {
            "action": "move from top right to mid right",
            "preconds": [
                "2 spaces from start",
                "no blockade"
            ],
            "add": [
                "1 spaces from start",
                "blockade left"
            ],
            "delete": [
                "2 spaces from start",
                "no blockade"
            ]
        },
        {
            "action": "move from top right to top middle",
            "preconds": [
                "2 spaces from start",
                "no blockade"
            ],
            "add": [
                "3 spaces from start",
                "blockade below"
            ],
            "delete": [
                "2 spaces from start",
                "no blockade"
            ]
        },
        {
            "action": "move from top middle to top right",
            "preconds": [
                "3 spaces from start",
                "blockade below"
            ],
            "add": [
                "2 spaces from start",
                "no blockade"
            ],
            "delete": [
                "3 spaces from start",
                "blockade below"
            ]
        },
        {
            "action": "move from top middle to top left",
            "preconds": [
                "3 spaces from start",
                "blockade below"
            ],
            "add": [
                "4 spaces from start",
                "no blockade"
            ],
            "delete": [
                "3 spaces from start",
                "blockade below"
            ]
        },
        {
            "action": "move from top left to top middle",
            "preconds": [
                "4 spaces from start",
                "no blockade"
            ],
            "add": [
                "3 spaces from start",
                "blockade below"
            ],
            "delete": [
                "4 spaces from start",
                "no blockade"
            ]
        },
        {
            "action": "move from top left to middle left",
            "preconds": [
                "4 spaces from start",
                "no blockade"
            ],
            "add": [
                "3 spaces from start",
                "blockade right"
            ],
            "delete": [
                "4 spaces from start",
                "no blockade"
            ]
        },
        {
            "action": "move from middle left to top left",
            "preconds": [
                "3 spaces from start",
                "blockade right"
            ],
            "add": [
                "4 spaces from start",
                "no blockade"
            ],
            "delete": [
                "3 spaces from start",
                "blockade right"
            ]
        },
        {
            "action": "move from middle left to bottom left",
            "preconds": [
                "3 spaces from start",
                "blockade right"
            ],
            "add": [
                "2 spaces from start"
            ],
            "delete": [
                "3 spaces from start"
            ]
        },
        {
            "action": "move from bottom left to middle left",
            "preconds": [
                "2 spaces from start",
                "blockade right"
            ],
            "add": [
                "3 spaces from start"
            ],
            "delete": [
                "2 spaces from start"
            ]
        }
    ]
}



def main():
    start = problem['start']
    finish = problem['finish']
    ops = problem['ops']
    actionSequence = gps(start, finish, ops)
    if actionSequence is None:
        print("plan failure...")
        return
    for action in actionSequence:
        print(action)

if __name__ == '__main__':
    main()