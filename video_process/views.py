# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the video index.")


# 上传视频
def upload(request):
    # 从request.body中获取上传的文件
    file = request.FILES.get('file')
    # TODO：获取到文件后的后续操作
    # 输出文件名称
    print(file.name)
    # 返回上传成功的信息
    return HttpResponse(file.name)
