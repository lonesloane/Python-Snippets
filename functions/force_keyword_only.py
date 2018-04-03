def fuzzy(param, shit, unknown, unclear, another, again):
    print('param:{}, shit: {}, unknown:{}, unclear:{}, another:{}, again:{}'.format(param,
                                                                                    shit,
                                                                                    unknown,
                                                                                    unclear,
                                                                                    another,
                                                                                    again))

# * as 1st parameter forces use of keyword params
def forced(*, param, shit, unknown, unclear, another, again):
    print('param:{}, shit: {}, unknown:{}, unclear:{}, another:{}, again:{}'.format(param,
                                                                                    shit,
                                                                                    unknown,
                                                                                    unclear,
                                                                                    another,
                                                                                    again))


fuzzy(1, 2, 3, 4, 5, 6) # which one is which ?

forced(param=1, shit=2, unknown=3, unclear=4, another=5, again=6)