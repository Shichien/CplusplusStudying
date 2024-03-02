import requests
from PIL import Image
import pytesseract

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 登录页面的 URL
login_url = 'https://service.ecnu.edu.cn/'

# 创建会话对象
session = requests.Session()
session.headers.update(headers)

# 获取验证码图片的 URL
captcha_img_url = 'https://portal1.ecnu.edu.cn/cas/code'

# 下载验证码图片
response = session.get(captcha_img_url)
image = Image.open(BytesIO(response.content))

# 使用 pytesseract 识别验证码
code = pytesseract.image_to_string(image)

# 查找并提取登录表单中的必要参数
form = soup.find('form', {'id': 'login-form'})
action = form['action']
inputs = form.find_all('input')
data = {input.get('name'): input.get('value') for input in inputs}

# 设置表单数据，包括用户名、密码和验证码
data['username'] = '10235101526'
data['password'] = 'Deralive2'
data['captcha'] = code

# 提交表单登录
response = session.post(action, data=data)

# 打印登录结果
print(response.text)

