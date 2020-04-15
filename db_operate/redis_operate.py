from conf.settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class RedisOperate:

    def __init__(self, db=0):
        try:
            import redis
            self.redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=db, password=REDIS_PASSWORD, decode_responses=True)
        except self.redis.exceptions as e:
            print("redis出现异常，请注意！错误信息为%s" % e)

    def get_key(self, key):
        """
        :param key: 需要获取的key值
        :return:
        """
        mold = self.redis.type(key)
        if mold == 'zset':
            end = self.redis.zcard(key)
            return self.redis.zrevrange(key, 0, end, withscores=False, score_cast_func=int)
        elif mold == 'set':
            return self.redis.smembers(key)
        else:
            return self.redis.get(key)

    def set_key(self, key, value, ex=None, px=None, nx=None, xx=None):
        """
        :param key: key
        :param value: 值
        :param ex: 过期时间（秒）
        :param px: 过期时间（毫秒）
        :param nx: 如果设置为True，则只有name不存在时，当前set操作才执行
        :param xx: 如果设置为True，则只有name存在时，当前set操作才执行
        :return:
        """
        return self.redis.set(key, value, ex, px, nx, xx)


if __name__ == '__main__':
    print(RedisOperate().set_key("g", "c", ex=6, nx=True))


