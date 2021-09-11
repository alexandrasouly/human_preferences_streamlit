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
            ) 
        ''')

def insert_traj_pair(left_id, right_id): 
    """ Insert a pair of IDs that is yet to rate"""
    c.execute(''' INSERT INTO trajectories (left_id, right_id, preference) VALUES(?, ?, ?) ''', (left_id, right_id, 0)) 
    conn.commit()

def rate_traj_pair(left_id, right_id, preference): 
    """ Rate a pair of IDs: 1 for left, 2 for right, 3 for undecided"""

    stmt = '''UPDATE trajectories SET 'preference' = '{}' WHERE left_id = {} AND right_id = {}'''.format(preference, left_id, right_id) 
    c.execute(stmt) 
    conn.commit()

def get_all_unrated_pairs() -> List[Tuple[int]]:
    c.execute('''SELECT * FROM trajectories WHERE preference = 0''') 
    data = [] 
    for row in c.fetchall(): 

        data.append(row) 
    return data

def get_one_unrated_pair() -> Tuple(int):
    c.execute('''SELECT * FROM trajectories WHERE preference = 0 LIMIT = 1''') 
    data = [] 
    for row in c.fetchall(): 

        data.append(row) 
    return data

def delete_pair(left_id, right_id):
    """ Delete a pair of IDs - this is for testing, no actual use case"""
    c.execute('''DELETE FROM trajectories WHERE left_id = {} AND right_id = {}'''.format(left_id,right_id)) 
    conn.commit()