# -*- coding: utf-8 -*-

'''
获取课程id的json请求URL
http://api.maiziedu.com/v2/getCareerDetail/?UUID=680c2c9cc8f147dc8b157b48aa9ddfc9&careerId=13&client=android
'''

import requests
import io

# 迅雷安装位置 这里要注意:安装位置要一定是英文的路径,中文的失败
download_exe = r'D:\Thunder9.1.22.538\Program\Thunder.exe'
# 视频储存位置
download_dir = ur'E:\maizi'
# 生成一个批处理文件
urls_bat = r'E:\click_to_download.bat'
# 此处为课程id列表（例如http://www.maiziedu.com/course/874）比如我现在要下载874和928的课程
course_id_list = [874, 928]


def download(course_id):
    result = []

    url = 'http://api.maiziedu.com/v2/getCoursePlayInfo/?courseId=%d&client=android' % course_id

    r = requests.get(url)

    json_data = r.json()

    course_name = json_data['data']['course_name']

    video_list = json_data['data']['video_list']

    for video in video_list:
        video_id = video['video_id']
        video_name = video['video_name']
        video_url = video['video_url']
        cmd = ur'"%s" "%s" --file-allocation=none --max-connection-per-server=4  -d "%s\%s" -o "%d_%s.mp4"' \
              % (download_exe, video_url, download_dir, course_name, video_id, video_name)
        print cmd
        result.append(cmd)

    return result


result = []
for course_id in course_id_list:
    result = result + download(course_id)

bat_file = io.open(urls_bat, 'w+', encoding='gbk')
for cmd in result:
    bat_file.writelines(cmd + '\r\n')
bat_file.close()
