import time
import random
import difflib


WIN_ANSWERS = ['^-^', '*! ! !*', ':D', ':}', ':]',
              '=D', ':3', 'You WIN!','You WIN! :)',
             'WINNER!', '* WINNER *', 'You WON!']
LOOSE_ANSWERS = [':(', 'D:', '-_-', 'T-T', 'You LOOSE!',
                'You LOOSE! better luck next time',
               'haha! looser', 'You LOST!', 'Not this time']
DRAW_ANSWERS = ['O.o', ':/', '. . .', "'-'", ':P', ':?',
               "'7'", 'Welp.', 'DRAW!', 'Try again',
              'Great mins think alike', 'Could not compute', 'ERROR!']
POSSIBLE_MOVES = ['ROCK', 'SISSORS', 'PAPER']


class User:
    """Every users personal connection to the bot,
    storing information about the user"""
    def __init__(self, username, id):
        self.username = str(username)
        self.id = str(id)
        self.rps_tally = 0
        self.msg_hist = []

    def __str__(self):
        retstr = f'Name: {self.username}'
        retstr += f'\nID: {self.id}'
        retstr += f'\nRPS WINS: {self.rps_tally}'
        return retstr

    def rps(self, move):
        """Returns a nested list for every round, 
        containing a declaration of round and the result"""
        move1 = difflib.get_close_matches(move.upper(), POSSIBLE_MOVES, cutoff=0.7)[0]
        move2 = random.choice(POSSIBLE_MOVES)
        result = [f'{move1} vs {move2}', self.rps_check_win(move1, move2)]

        return result

    def rps_check_win(self, move1, move2):
        move_index = POSSIBLE_MOVES.index(move1)
        if POSSIBLE_MOVES[(move_index+1)%3] == move2:
            self.rps_tally += 1
            return random.choice(WIN_ANSWERS)
        elif POSSIBLE_MOVES[(move_index-1)%3] == move2:
            return random.choice(LOOSE_ANSWERS)
        elif move1 == move2:
            return random.choice(DRAW_ANSWERS)
    
    def log_msg(self, message):
        if not message in self.msg_hist:
            self.msg_hist.append(message)

    def ret_msg_hist(self, ammount):
        if ammount >= len(self.msg_hist):
            return self.msg_hist[:ammount]
        else: return self.msg_hist[:ammount]
