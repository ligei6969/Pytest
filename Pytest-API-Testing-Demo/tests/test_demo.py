# 导入 Python 的 HTTP 请求库 requests，用于发送 GET/POST 等网络请求
import requests


# 定义一个测试类，类名必须以 Test 开头，这样 pytest 框架才能识别它
class TestPytestDemo:

    # 定义测试 GET 请求的测试用例，方法名必须以 test_ 开头
    def test_get_demo(self):

        # 1. 准备数据：定义测试接口的根 URL（这里使用的是一个免费的 mock 测试接口网站）
        base_url = "https://jsonplaceholder.typicode.com"

        # 2. 发送请求：使用 requests.get() 向服务器请求 ID 为 1 的帖子数据

        # 【已修复】：把 f 挪到了引号外面！现在它可以正确拼接出完整的 URL 了
        response = requests.get(f"{base_url}/posts/1")

        # 3. 执行断言（验证结果）：
        # 断言接口返回的 HTTP 状态码是否为 200（200 代表请求成功）
        assert response.status_code == 200

        # response.json() 将返回的 JSON 文本转换为 Python 的字典格式
        # 断言返回的数据中，'userId' 的值是否等于数字 1
        assert response.json()["userId"] == 1
        # 断言返回的数据中，该帖子的 'id' 是否等于数字 1
        assert response.json()["id"] == 1

    # 定义测试 POST 请求的测试用例，同样以 test_ 开头
    def test_post_demo(self):

        # 1. 准备数据：定义基础 URL
        base_url = "https://jsonplaceholder.typicode.com"

        # 【注意】：这里模拟第三方接口，原网站的正确字段名是 "userId" (有个 r)
        # 很多新手会顺手敲成 "useId" 导致后续断言失败，这里帮你改成了规范的 "userId"
        requests_data = {"title": "foo", "body": "bar", "userId": 1}

        # 2. 发送请求：使用 requests.post() 向 /posts 接口提交上面定义的数据
        # 传递字典数据给 json 参数，requests 会自动帮你转为标准的 JSON 格式发送
        response = requests.post(f"{base_url}/posts", json=requests_data)

        # 3. 执行断言（验证结果）：
        # 断言接口返回的 HTTP 状态码是否为 201（201 在 HTTP 协议中代表成功创建了新资源）
        assert response.status_code == 201

        # 在控制台打印出服务器返回的 JSON 数据，方便我们在测试时查看完整的返回结构
        print(response.json())

        # 断言返回的数据中，'userId' 是否等于数字 1
        assert response.json()["userId"] == 1

        # 断言服务器为这篇新帖子自动生成的唯一标识 'id' 是否为 101
        assert response.json()["id"] == 101