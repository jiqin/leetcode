# In a game two player fight togather, the one win will get the loser's score.
# Simulate how the score exchanged.

import sys
from unittest import TestCase, main as test_main
import optparse
import random
from copy import copy
from collections import defaultdict
from common.argument_validator import argument_validate

# ELO rating System


START_SCORE = 1400


class GameManager(object):
    def __init__(self):
        self._player_scores = []
        self._player_rand = random.Random()
        self._game_rand = random.Random()

    def player_num(self):
        return len(self._player_scores)

    @argument_validate(int)
    def init_game(self, player_num):
        self._player_scores = [START_SCORE] * player_num

    def get_two_players(self):
        """ random get two player

        :return: int, int
        """
        player_1 = self._player_rand.randint(0, self.player_num() - 1)
        player_2 = self._player_rand.randint(0, self.player_num() - 1)

        return player_1, player_2

    @argument_validate(int, int)
    def get_win_change(self, score1, score2):
        """ win change of score1

        :param score1:
        :param score2:
        :return: float
        """
        return 1.0 / (1.0 + pow(10.0, (score1 - score2) * 1.0 / 400.0))

    @argument_validate(int, int, float)
    def get_winner(self, player1, player2, player1_win_change):
        """ get winner

        :param player1:
        :param player2:
        :param player1_win_change: [0, 1]
        :return: True if player1 win, else False
        """
        N = 100
        rate = self._game_rand.randint(0, N) * 1.0 / N
        return rate <= player1_win_change

    @argument_validate(int, float)
    def get_exchange_score(self, player_win_score, player_win_change):
        """ get winner exchange score

        :param player_win_score:
        :param player_win_change:
        :return: int
        """
        if player_win_score < 2100:
            k_value = 32
        elif player_win_score < 2400:
            k_value = 24
        else:
            k_value = 16
        return int(round(k_value * (1 - player_win_change)))

    def one_game(self):
        player1, player2 = self.get_two_players()
        player1_win_change = self.get_win_change(self._player_scores[player1], self._player_scores[player2])
        is_player1_win = self.get_winner(player1, player2, player1_win_change)
        if is_player1_win:
            player_win = player1
            player_loser = player2
            win_change = player1_win_change
        else:
            player_win = player2
            player_loser = player1
            win_change = 1.0 - player1_win_change
        exchange_score = self.get_exchange_score(self._player_scores[player_win], win_change)

        self._player_scores[player_win] += exchange_score
        self._player_scores[player_loser] -= exchange_score
        if self._player_scores[player_loser] < 0:
            self._player_scores[player_loser] = 0

    def print_result(self):
        N = 100
        score_values = defaultdict(lambda: 0)
        for score in self._player_scores:
            key = score / N
            score_values[key] += 1
        score_values = [(k * N, v) for k, v in score_values.iteritems()]
        score_values.sort(key=lambda x:x[0], reverse=True)
        for score, n in score_values:
            print score, n


class TestGameManager(TestCase):
    def setUp(self):
        self.player_num = 100
        self.game_manager = GameManager()
        self.game_manager.init_game(self.player_num)

    def test_init_game(self):
        self.assertEqual(self.player_num, self.game_manager.player_num())

    def test_get_two_player(self):
        game_num = 100000
        game_num_per_player = 2 * game_num / self.player_num

        player_dict = defaultdict(lambda: 0)
        for _ in range(game_num):
            player1, player2 = self.game_manager.get_two_players()
            self.assertNotEqual(player1, player2)
            # self.assertTrue(abs(player1 - player2) < 5)
            # self.assertGreaterEqual(player1, 0)
            # self.assertLess(player1, self.game_manager.player_num())
            # self.assertGreaterEqual(player2, 0)
            # self.assertLess(player2, self.game_manager.player_num())

            player_dict[player1] += 1
            player_dict[player2] += 1

        # check the rate
        for player, n in player_dict.iteritems():
            rate = n * 1.0 / game_num_per_player
            self.assertLess(rate, 2.0, player_dict)
            self.assertGreater(rate, 0.5, player_dict)

    def test_get_win_chance(self):
        self.assertEqual(0.5, self.game_manager._get_win_chance(0, 0))


def main(player_num, game_num):
    game_manager = GameManager()
    game_manager.init_game(player_num)
    for i in range(game_num):
        game_manager.one_game()
        if (i + 1) % 10000 == 0:
            print 'process: {}/{} = {:2.3}%'.format(i, game_num, i * 100.0 / game_num)
    game_manager.print_result()


if __name__ == '__main__':
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-t', '--run_unit_test', default=False, action='store_true', help='run unit test')
    opt_parser.add_option('-n', '--player_num', type=int, default=100, help='number of players')
    opt_parser.add_option('-m', '--game_num', type=int, default=100000, help='number of games')
    args, _ = opt_parser.parse_args()
    if args.run_unit_test:
        sys.argv = sys.argv[0:1]
        test_main()
    else:
        main(args.player_num, args.game_num)
