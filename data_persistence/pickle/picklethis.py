import anydbm
import pickle
import random


def test_pickle():
    db = anydbm.open('anydbm_db.db', flag='c')
    for i in range(0, 100):
        db[str(i)] = pickle.dumps(random.randint(0, 100))
    for key in db:
        print(key, pickle.loads(db[key]))
    db.close()


def test_db():
    db = anydbm.open('anydbm_db.db', flag='c')
    for i in range(0, 100):
        db[str(i)] = str(random.randint(0, 100))
    for key in db:
        print(key, db[key])
    db.close()
