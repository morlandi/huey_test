from huey import RedisHuey

huey = RedisHuey(name="huey_test", result_store=True)  # , host='your.redis.host'
