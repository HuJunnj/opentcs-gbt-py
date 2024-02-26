import schedule
import time
import requests
from datetime import datetime

def send_post_request():
    url = 'http://localhost:55200/gbt/transportOrders/'
    # 获取当前时间
    current_time = datetime.now()
    # 将时间转换为字符串，可以使用 strftime 函数指定格式
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    orderName = 'GBT_' + time_string
    url = url + orderName
    data = {
        "incompleteName": False,
        "dispensable": False,
        "deadline": "2024-02-27T06:42:40.396Z",
        "intendedVehicle": "Vehicle-0001",
        "peripheralReservationToken": None,
        "wrappingSequence": None,
        "type": "test",
        "destinations": [
        {
                "locationName": "Location-0001",
                "operation": "loading",
                "properties": []
            },
            {
                "locationName": "Location-0003",
                "operation": "verification",
                "properties": []
            },
            {
                "locationName": "Location-0002",
                "operation": "unloading",
                "properties": []
            },
            {
                "locationName": "Location-0004",
                "operation": "parking",
                "properties": []
            }
        ],
        "properties": [
            {
                "key": "ip",
                "value": "192.168.100.2"
            }
        ],
        "dependencies": []
    }
    try:
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        # 记录请求开始时间
        start_time = time.time()
        response = requests.post(url, json=data, headers=headers, timeout=0.01)
        # 记录请求结束时间
        end_time = time.time()
        # 计算请求花费的时间
        elapsed_time = end_time - start_time
        print(f"请求花费了 {elapsed_time} 秒")
        if response.status_code == 200:
            print(f"POST request successful: {response.text}")
        else:
            print(f"POST request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending POST request: {e}")

# 每隔10分钟执行一次定时任务
# schedule.every(10).minutes.do(send_post_request)

while True:
    #schedule.run_pending()
    send_post_request()
    # 设置创建订单频率
    time.sleep(5)
