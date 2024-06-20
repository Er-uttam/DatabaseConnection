#CREATING THE TABLE
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS team_data (team text, country text,
             season inteSger, total_goals integer
             );''')

conn.commit()

print("Table created successfully")
# conn.close()

#INSERTING THE VALUES
conn.execute("INSERT INTO team_data VALUES('Real Madrid','Spain',2019,53);")
conn.execute("INSERT INTO team_data VALUES('Barcelona','Spain',2019,47);")
conn.execute("INSERT INTO team_data VALUES('Arsenal','UK',2019,52);")
conn.execute("INSERT INTO team_data VALUES('Barcelona','Spain',2019,45);")
conn.execute("INSERT INTO team_data VALUES('Arsenal','UK',2019,50);")

conn.commit()

# Average goal by team

conn = sqlite3.connect('test.db')
cursor = conn.execute(f'''SELECT team,
                      AVG(total_goals)AS avg_goals
                      FROM team_data
                      GROUP BY team;''')
print(list(cursor))
for row in cursor:
    print(row)
# conn.close()

#Now ,the correct query , using the appropriate sub query

conn = sqlite3.connect('test.db')
cursor = conn.execute(''' SELECT team_name , avg_goals
                      FROM(
                      SELECT team AS team_name,
                      AVG(total_goals) AS avg_goals
                      FROM team_data
                      GROUP BY team) tp
                      WHERE avg_goals > 50; ''')

for row in cursor:
    print(row)
conn.close()