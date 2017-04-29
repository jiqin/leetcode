import datetime


def run_test_cases(test_func, test_cases, equal_func=None, print_funcs=None, print_time=False):
    if not isinstance(test_func, (list, tuple)):
        test_func = [test_func]

    for test_case in test_cases:
        print '.' * 50
        params = test_case[0:-1]
        exp_ret = test_case[-1]
        for func in test_func:
            if print_time:
                t1 = datetime.datetime.now()
            ret = func(*params)
            if print_time:
                t2 = datetime.datetime.now()
                print 'Time: {:.6f}'.format((t2 - t1).total_seconds())

            if equal_func:
                r = equal_func(ret, exp_ret)
            else:
                r = (ret == exp_ret)

            if r:
                if not print_time:
                    print 'pass'
            else:
                for i, param in enumerate(params):
                    _print_item(param, print_funcs, i)
                    # print '-'

                _print_item(exp_ret, print_funcs, -1)
                print '.'
                _print_item(ret, print_funcs, -1)
                print '>' * 30, 'Failed'


def _print_item(item, print_funcs, index):
    if print_funcs and print_funcs[index]:
        print_funcs[index](item)
    else:
        print item


def is_matrix_equal(m1, m2):
    for i in range(0, len(m1)):
        for j in range(0, len(m1[0])):
            if m1[i][j] != m2[i][j]:
                return False
    return True


def print_matrix(m):
    for i in range(0, len(m)):
        print ''.join(m[i])
