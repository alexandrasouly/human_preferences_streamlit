import sqlite3
from typing import List, Tuple 
conn = sqlite3.connect('trajectories.db') 
c = conn.cursor()

def table_exists(): 
    c.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = 'trajectories' ''') 
    if c.fetchone()[0] == 1: 
        return True 
    return False

def create_table():
    if not table_exists(): 
        c.execute(''' 
            CREATE TABLE trajectories( 
                left_id INTEGER, 
                right_id INTEGER, 
                preference INTEGER,
                unique (left_id, right_id)
            ) ''')

def insert_traj_pair(left_id:int, right_id:int): 
    """ Insert a pair of IDs that is yet to rate"""
    if left_id == right_id:
        raise Exception("The supplied IDs are the same")
    if left_id > right_id:
        left_id, right_id = right_id, left_id
    # sqlite3.IntegrityError occurs if they already exist
    c.execute(''' INSERT INTO trajectories (left_id, right_id, preference) VALUES(?, ?, ?) ''', (left_id, right_id, 0)) 
    conn.commit()

def rate_traj_pair(left_id, right_id, preference): 
    """ Rate a pair of IDs: 1 for left, 2 for right, 3 for undecided"""
    if left_id == right_id:
        raise Exception("The supplied IDs are the same")
    if left_id > right_id:
        left_id, right_id = right_id, left_id

    if get_rating_of_pair(left_id, right_id) != 0:
        raise Exception("This pair was already rated")
    stmt = '''UPDATE trajectories SET 'preference' = '{}' WHERE left_id = {} AND right_id = {}'''.format(preference, left_id, right_id) 
    c.execute(stmt) 
    conn.commit()

def get_all_unrated_pairs() -> List[Tuple[int]]:
    c.execute('''SELECT * FROM trajectories WHERE preference = 0''') 
    unrated_pairs = c.fetchall()
    return [(line[0],line[1]) for line in unrated_pairs]

def get_one_unrated_pair() -> Tuple[int]:
    c.execute('''SELECT * FROM trajectories WHERE preference = 0 LIMIT 1''') 
    unrated_pairs = c.fetchall()
    if len(unrated_pairs)==0:
        raise Exception("No unrated pair.")
    return (unrated_pairs[0][0], unrated_pairs[0][1])

def get_rating_of_pair(left_id, right_id) -> int:
    """0 for unrated, 1 for left, 2 for right, 3 for undecided"""
    if left_id == right_id:
        raise Exception("The supplied IDs are the same")
    if left_id > right_id:
        left_id, right_id = right_id, left_id

    c.execute('''SELECT * FROM trajectories WHERE left_id = {} AND right_id = {}'''.format(left_id,right_id))
    traj_pair = c.fetchall()
    if  len(traj_pair)==0:
        raise Exception("Pair not found in database")
    if  len(traj_pair)>1:
        raise Exception("Pair found twice in database - this is due to a bugnot supposed to happen.") 

    return traj_pair[0][2]

def delete_pair(left_id, right_id):
    """ Delete a pair of IDs - this is for testing, no actual use case"""
    if left_id == right_id:
        raise Exception("The supplied IDs are the same")
    if left_id > right_id:
        left_id, right_id = right_id, left_id

    c.execute('''DELETE FROM trajectories WHERE left_id = {} AND right_id = {}'''.format(left_id,right_id)) 
    conn.commit()

def return_all_data():
    c.execute('''SELECT * FROM trajectories''') 
    data = []
    for row in c.fetchall(): 
        data.append(row) 
    return data


#if __name__ == '__main__':

    # Uncomment this to create test database for videos
    # create_table()
    # insert_traj_pair(1000, 1001)
    # insert_traj_pair(1001, 1002)
    # insert_traj_pair(1003, 1004)
    # insert_traj_pair(1003, 1005)
    # insert_traj_pair(1000, 1006)