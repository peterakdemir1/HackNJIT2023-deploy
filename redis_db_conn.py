import redis
import hacknjit2023_db_constants as db_const


try:
    r = redis.Redis(
        host=db_const.HOST, 
        port=db_const.PORT,
        password=db_const.PASSWORD,
        decode_responses=True   
    )

    print('connected to redis db', f'\nping result: {r.ping()}')
except Exception as e:
    print('failed to connect to redis db')


