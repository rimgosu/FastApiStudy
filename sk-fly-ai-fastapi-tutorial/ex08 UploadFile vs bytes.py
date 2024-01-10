"""
File parameters with UploadFile

UploadFile을 사용하는건 bytes에 대비하여 아래와 같은 장점이 있다.
스풀링 파일을 사용한다. 메모리에 저장되는 파일의 사이즈는 제한되어있고, 
사이즈의 제한이 넘으면 disk에 파일을 저장한다. 스풀링에 대한 자세한설명은 이곳을 참조하자.
(https://namu.wiki/w/%EC%8A%A4%ED%92%80%EB%A7%81)

스풀링을 사용함으로서 이미지나 비디오혹은 큰사이즈의 파일들을 메모리를 전부다 사용하지 않고 처리할 수 있다
업로드된 파일로부터 metadata를 받을 수 있다
file-like async interface를 가지고 있다
실제로 파이썬으 SpooledTemporaryFile 을 노출한다. file-like 오브젝트처럼 다른 라이브러리에 넘길 수 있다

UploadFile은 다음과 같은 attributes를 가진다.
filename : str자료형이고 파일이름을 담는다
content_type : str자료형이고 content type을 담는다. e.g image/jpeg
file : SpooledTemporaryFile(file-like object) 실제 파일 데이터이고 file-like를 expect하는 다른 함수나 라이브러리에 전달 할 수 있다

UploadFile은 하기의 async 메소드들을 가지고 있다

write(data) : data(str 또는 bytes)를 write한다
read(size) : size(int) 만큼 bytes/character 를 읽어드린다.
seek(offset) : 파일의 offset(int) 만큼 위치 이동한다
close() : 파일을 종료한다

위 함수들은 모두 async이므로 사용할 때 await를 해주어야 한다
"""

from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)