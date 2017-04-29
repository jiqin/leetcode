# In a game two player fight togather, the one win will get the loser's score.
# Simulate how the score exchanged.

import sys
from unittest import TestCase, main as test_main
import optparse
import random
from copy import copy
from collections import defaultdict
from common.argument_validator import argument_validate

gam_rand = random.Random()


START_SCORE = 1400


class Player(object):
    @argument_validate(int, int)
    def __init__(self, id, score=START_SCORE):
        self.id = id
        self.score = score

    @argument_validate(score=int)
    def get_score_from_player(self, player, score):
        """ get score from player

        :param player: Player, who contribute score
        :param score: int
        :return:
        """
        assert isinstance(player, Player)

        self.score += score
        player.score = max(0, player.score - score)


class PlayerScoreManager(object):
    def __init__(self):
        self._score_ids = []  # [[score, set(ids)], ...] order by score desc

    def print_me(self):
        for score, ids in self._score_ids:
            print score, len(ids)

    def add_id_score(self, id, score):
        """

        :param score: int
        :param id: int
        :return: None
        """
        assert isinstance(id, int)
        assert isinstance(score, int)
        index = self._find_score(score)
        if index < len(self._score_ids) and self._score_ids[index][0] == score:
            self._score_ids[index][1].add(id)
        else:
            self._score_ids.insert(index, [score, set([id])])

    def remove_id_score(self, id, score):
        """

        :param score: int
        :param id: int
        :return: None
        """
        assert isinstance(id, int)
        assert isinstance(score, int)

        index = self._find_score(score)
        assert index < len(self._score_ids)
        assert self._score_ids[index][0] == score

        self._score_ids[index][1].remove(id)
        if not self._score_ids[index][1]:
            self._score_ids.pop(index)

    def get_round_ids(self, id, score):
        """ Get ids whose score is near to input score

        :param score: int
        :return: list of id, [int, int, ...]
        """
        assert isinstance(score, int)

        index = self._find_score(score)
        assert index < len(self._score_ids)
        assert self._score_ids[index][0] == score

        ids = copy(self._score_ids[index][1])
        ids.remove(id)
        if index > 0:
            ids = ids.union(self._score_ids[index-1][1])
        if index < len(self._score_ids) - 1:
            ids = ids.union(self._score_ids[index+1][1])
        return list(ids)

    def _find_score(self, score):
        """ find the first value that <= input score
        :param score: int
        :return: int, index of value
        """
        assert isinstance(score, int)
        l = 0
        r = len(self._score_ids)
        while l < r:
            m = (l + r) / 2
            v = self._score_ids[m][0]
            if v > score:
                l = m + 1
            elif v == score:
                l = m
                break
            else:
                r = m
        return l


class GameManager(object):
    def __init__(self):
        self._players = []
        self._player_score_manager = PlayerScoreManager()
        self._player_rand = random.Random()

    def player_num(self):
        return len(self._players)

    def player(self, id):
        assert isinstance(id, int)
        return self._players[id]

    @argument_validate(int)
    def init_game(self, player_num):
        self._players = self._init_players(player_num)
        for player in self._players:
            self._player_score_manager.add_id_score(player.id, player.score)

    @argument_validate(int)
    def _init_players(self, player_num):
        players = []
        for i in range(player_num):
            players.append(Player(i))
        return players

    def get_two_players(self):
        """ random get two player, their scores should be almost same

        :return: (Player, Player): player1, player2
        """
        player = self.player(self._player_rand.randint(0, self.player_num() - 1))

        return player, self._get_match_player(player)

    def _get_match_player(self, player):
        """ get a match player for input player

        :param player: Player
        :return: Player
        """
        assert isinstance(player, Player)

        ids = self._player_score_manager.get_round_ids(player.id, player.score)
        assert len(ids) > 0

        new_id = ids[self._player_rand.randint(0, len(ids) - 1)]
        return self.player(new_id)

    def get_winner(self, player1, player2):
        """ get winner from player1 and player2

        :param player1: Player
        :param player2: Player
        :return: (Player, Player), (winner, loser)
        """
        assert isinstance(player1, Player)
        assert isinstance(player2, Player)

        chance = self._get_win_chance(player1.score, player2.score)
        rand_v = gam_rand.random()
        return (player1, player2) if rand_v < chance else (player2, player1)

    def _get_win_chance(self, score1, score2):
        """ get player1's win chance

        :param score1: int
        :param score2: int
        :return: float [0, 1]
        """
        total_score = (score1 + score2) * 5 + 1
        chance = 0.5 + (score1 - score2) * 1.0 / total_score
        return chance

    def one_game(self):
        player1, player2 = self.get_two_players()
        winner, loser = self.get_winner(player1, player2)
        self._player_score_manager.remove_id_score(winner.id, winner.score)
        self._player_score_manager.remove_id_score(loser.id, loser.score)

        winner.get_score_from_player(loser, 10)
        self._player_score_manager.add_id_score(winner.id, winner.score)
        self._player_score_manager.add_id_score(loser.id, loser.score)

    def print_result(self):
        self._player_score_manager.print_me()


class TestPlayerScoreManager(TestCase):
    def setUp(self):
        pass

    def test_me(self):
        def _score(id):
            return id / 10 * 10

        def _sort(values):
            values.sort()
            return values

        manager = PlayerScoreManager()
        # insert
        for i in range(100):
            manager.add_id_score(i, _score(i))
        # [[90, set(90, 91, 92, ...)], [80, set(80, 81, 82, ...)], ... [0, set(0, 1, ..., 9)]
        self.assertEqual([[i * 10, set(range(i * 10, i * 10 + 10))] for i in range(9, -1, -1)], manager._score_ids)

        for i in range(100):
            self.assertEqual(9 - i / 10, manager._find_score(i))

        self.assertEqual([i for i in range(80, 100) if i != 92], _sort(manager.get_round_ids(92, 90)))
        self.assertEqual([i for i in range(70, 100) if i != 83], _sort(manager.get_round_ids(83, 80)))
        self.assertEqual([i for i in range(0, 30) if i != 14], _sort(manager.get_round_ids(14, 10)))
        self.assertEqual([i for i in range(0, 20) if i != 5], _sort(manager.get_round_ids(5, 0)))

        # remove
        for i in range(100):
            manager.remove_id_score(i, _score(i))
        self.assertEqual([], manager._score_ids)


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

    def test_get_winner(self):
        def _test(score1, score2, score1_win_most):
            game_count = 10000
            player1 = Player(0, score1)
            player2 = Player(1, score2)
            player1_win_count = 0
            for _ in range(game_count):
                winner, _ = self.game_manager.get_winner(player1, player2)
                if winner == player1:
                    player1_win_count += 1
            if score1_win_most:
                self.assertGreater(player1_win_count, game_count / 2)
            else:
                self.assertLess(player1_win_count, game_count / 2)

        for i in range(0, 1000, 100):
            _test(i, 1100, False)
        for i in range(1200, 2000, 100):
            _test(i, 1100, True)


def main(player_num, game_num):
    game_manager = GameManager()
    game_manager.init_game(player_num)
    for i in range(game_num):
        game_manager.one_game()
        if (i + 1) % 1000 == 0:
            print 'process: {}/{} = {:2.2}%'.format(i, game_num, i * 100.0 / game_num)
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
