import random

import anydbm


def test_db():
    db = anydbm.open('anydbm_db.db', flag='c')
    for i in range(0, 100):
        db[str(i)] = str(random.randint(0, 100))
    for key in db:
        print key, db[key]
    db.close()
