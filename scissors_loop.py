from time import sleep
from hamsa import hand
from hamsa import poses

# 复位函数：全部手指张开

def reset_hand(time=1000):
    hand.curl_pinky(1, time)
    hand.curl_ring(1, time)
    hand.curl_middle(1, time)
    hand.curl_index(1, time)
    hand.curl_thumb(1, time)
    sleep(time/1000)

if __name__ == '__main__':
    move_time = 1000  # 每次动作的持续时间（毫秒）
    delay = 2         # 每次循环之间的延时（秒）
    try:
        reset_hand(move_time)
        sleep(delay)
        while True:
            poses.peace(move_time)  # 剪刀手
            sleep(delay)
            reset_hand(move_time)  # 复位
            sleep(delay)
    except KeyboardInterrupt:
        reset_hand(move_time) 