"""
Copyright Ionut Soran 2022. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
"""
from layout.setup_layout import CrosswordWidget

if __name__ == "__main__":  # pragma: no cover
    """
    TODO add docstring
    """
    # cw = Crossword(cell_x=90, cell_y=90)
    # cw.run()
    cw = CrosswordWidget()
    cw.run()
    # conn = psycopg2.connect("dbname='pupikii' user='postgres' host='172.17.0.2' password='postgres' port='5432'")
    # cur = conn.cursor()
    # # cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    # # conn.commit()
    # cur.close()
    # conn.close()
    # time.sleep(3)
