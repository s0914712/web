from browser import document, ajax, window
import json

class ImgurUploader:
    def __init__(self):
        self.client_id = 'a0f19779af81cc0'  # 請替換為您的Imgur Client ID
    
    def upload_image(self, event):
        input_elem = document['imageInput']
        if not input_elem.files:
            window.alert('請選擇一個圖片文件')
            return
        
        file = input_elem.files[0]
        reader = window.FileReader.new()
        reader.readAsDataURL(file)
        reader.bind('load', lambda e: self._send_to_imgur(e.target.result))

    def _send_to_imgur(self, base64_image):
        # 移除 data URL 的前綴
        image_data = base64_image.split(',')[1]
        
        req = ajax.Ajax()
        req.bind('complete', self._on_complete)
        req.open('POST', 'https://api.imgur.com/3/image')
        req.set_header('Authorization', f'Client-ID {self.client_id}')
        req.send({'image': image_data})

    def _on_complete(self, req):
        if req.status == 200:
            response = json.loads(req.text)
            image_url = response['data']['link']
            document['result'].innerHTML = f'上傳成功！圖片URL: <a href="{image_url}" target="_blank">{image_url}</a>'
            document['imagePreview'].attrs['src'] = image_url
        else:
            print('上傳失敗:', req.text)
            document['result'].innerHTML = '上傳失敗，請稍後再試。'

uploader = ImgurUploader()

def init():
    document['uploadButton'].bind('click', uploader.upload_image)
    document['imageInput'].bind('change', preview_image)

def preview_image(event):
    file = event.target.files[0]
    if file:
        reader = window.FileReader.new()
        reader.readAsDataURL(file)
        reader.bind('load', lambda e: setattr(document['imagePreview'], 'src', e.target.result))

# 初始化
init()
