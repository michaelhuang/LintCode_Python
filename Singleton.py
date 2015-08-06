import  threading

class Solution:
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        """Based on tornado.ioloop.IOLoop.instance() approach.

        See https://github.com/facebook/tornado
        """
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

if __name__ == '__main__':
    class A(Solution):
        pass

    class B(Solution):
        pass

    a1, a2 = A.getInstance(), A.getInstance()
    b1, b2 = B.getInstance(), B.getInstance()

    assert a1 is a2
    assert b1 is b2
    assert a1 is not b1
    assert a2 is not b2

    print id(a1), id(a2)
    print id(b1), id(b2)