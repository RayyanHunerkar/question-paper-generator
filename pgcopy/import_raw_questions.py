from sqlite3 import connect
import pandas as pd
from pgcopy import CopyManager
import psycopg2

if __name__ == '__main__':
    cols = ('content','difficulty','unit')
    records = pd.read_csv(r'/Users/rayyanfaisalhunerkar/Python Projects/question-paper-generator/pgcopy/Questions.csv').values.tolist()
    conn = psycopg2.connect(database = 'edas_db')
    mgr = CopyManager(conn, 'staging.raw_question', cols)
    mgr.copy(records)
    conn.commit()