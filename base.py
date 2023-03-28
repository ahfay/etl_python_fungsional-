from sqlalchemy import create_engine

# session PostgreSQL
engine_psg = create_engine('postgresql://******')
conn_psg = engine_psg.connect()

# session MySQL
#engine_mysql = create_engine('mysql+pymysql://********')
#conn_mysql = engine_mysql.connect()
