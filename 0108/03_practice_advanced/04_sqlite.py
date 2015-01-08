from sqlalchemy import create_engine

engine = create_engine('sqlite://',echo=True)
connection = engine.connect()
r1 = connection.execute('select domain_id, is_edited from check_records')
