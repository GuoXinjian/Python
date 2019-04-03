import Douyu
import Stream
import Huya
import Panda
import Egame
import Zhanqi
import Huomao
import time

while True:

    Stream.streaminsert('douyu',Douyu.douyu(5))
    Stream.streaminsert("huya",Huya.huya(5))
    Stream.streaminsert("panda",Panda.panda(3))
    Stream.streaminsert("egame_qq",Egame.egame(3))
    Stream.streaminsert("zhanqi",Zhanqi.zhanqi(2))
    Stream.streaminsert("huomao",Huomao.huomao(2))
    time.sleep(25)