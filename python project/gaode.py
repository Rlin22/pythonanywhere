# 准备工作
import requests,json
import pandas as pd
from PIL import Image
from io import BytesIO
LJY_key="65b04d34830504b4f0a6fe32550d797a"

# 地理编码函数
def geocode(address):# address填写规则遵循：国家、省份、城市、区县、城镇、乡村、街道、门牌号码、屋邨、大厦，如：北京市朝阳区阜通东大街6号。
    """高德api地理编码"""
    url = "https://restapi.amap.com/v3/geocode/geo?parameters"
    params = {
    'key':LJY_key,
    'address':address,
}
    response = requests.get(url,params=params)
    date = response.json()['geocodes'][0]['location']
    return date

# 逆地理编码函数
def regeocode(location,extensions="base",radius=None):
    """高德api逆地理编码"""
    url = "https://restapi.amap.com/v3/geocode/regeo?parameters"
    params = {
        'key':LJY_key,
        'location':location,# 1.1函数所求出的经纬度信息
        'extensions':extensions,# extensions 参数默认取值是 base，也就是返回基本地址信息；extensions 参数取值为 all 时会返回基本地址信息、附近 POI 内容、道路信息以及道路交叉口信息。
        'radius':radius,# 搜索半径 radius取值范围在0~3000，默认是1000。单位：米
        'output':'json'
    }
    response = requests.get(url,params=params)
    date = response.json()
    return date

# 步行路径规划函数
def walking(origin,destination):
    """步行路径规划"""
    url = "https://restapi.amap.com/v3/direction/walking?parameters"
    params = {
        'key':LJY_key,
        'origin':origin,# 起点（经纬度信息）
        'destination':destination,# 终点（经纬度信息）
        'output':'json'
    }
    response = requests.get(url,params=params)
    date = response.json()
    return date

# 公交路径规划函数
def bus(origin,destination,city,cityd=None,extensions='base',strategy=None,nightflag=0,date=None,time=None):
    """公交路径规划"""
    url = "https://restapi.amap.com/v3/direction/transit/integrated?parameters"
    params = {
        'key':LJY_key,
        'origin':origin,# 起点 （经纬度）
        'destination':destination,# 终点（经纬度）
        'city':city,# 公交查询所在城市
        'cityd':cityd,# 跨城公交选填
        'extensions':extensions,# 返回结果详情
        'strategy':strategy,# 换成策略0：最快捷模式1：最经济模式2：最少换乘模式3：最少步行模式5：不乘地铁模式
        'nightflag':nightflag,# 是否记夜班车
        'date':date,# 发车日期
        'time':time,# 发车时间
        'output':'json'
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# 驾车路径规划函数
def car(origin,destination,strategy=10,waypoints=None,avoidpolygons=None,):
    """驾车路径规划"""
    url = "https://restapi.amap.com/v3/direction/driving?parameters"
    params = {
        'key':LJY_key,
        'origin':origin,# 起点
        'destination':destination,# 终点
        'strategy':strategy,# 路径策略
        'waypoints':waypoints,# 需要途经的地点
        'avoidpolygons':avoidpolygons,# 避让区域
        'output':'json'
    }
    response = requests.get(url,params=params)
    date = response.json()
    return date

# 行政区域查询函数
def district(keywords,subdistrict=None,page=None,offset=None,extensions='base',filter=None):
    """行政区域查询"""
    url = "https://restapi.amap.com/v3/config/district?parameters"
    params = {
        'key':LJY_key,
        'keywords':keywords,# 关键词
        'subdistrict':subdistrict,
        'page':page,
        'offset':offset,
        'extensions':extensions,
        'filter':filter,
        'output':'json'
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# 关键字搜索函数
def key_text(keywords,types,city=None,citylimit=None,children=None,page=None,extensions='base'):
    """关键字搜索"""
    url = "https://restapi.amap.com/v3/place/text?parameters"
    params = {
        'key':LJY_key,
        'keywords':keywords,
        'types':types,
        'city':city,
        'citylimit':citylimit,
        'children':children,
        'page':page,
        'extensions':extensions,
        'output':'json'
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# 周边搜索函数
def around_text(location,keywords=None,types=None,city=None,redius=None,sortrule=None,offset=None,page=None,extensions='base'):
    """周边搜索"""
    url = "https://restapi.amap.com/v3/place/around?parameters "
    params = {
        'key':LJY_key,
        'keywords':keywords,
        'location':location,
        'types':types,
        'city':city,
        'redius':redius,
        'sortrule':sortrule,
        'offset':offset,
        'page':page,
        'extensions':extensions,
        'output':'json'
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# 多边形搜索函数
def polygon_text(polygon,keywords=None,types=None,page=None,extensions=None):
    """多边形搜索函数"""
    url = "https://restapi.amap.com/v3/place/polygon?parameter"
    params = {
        'key':LJY_key,
        'keywords':keywords,
        'types':types,
        'page':page,
        'extensions':extensions,
        'output':'json',
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# IP定位函数
def ip(ip):
    """IP定位"""
    url = "https://restapi.amap.com/v3/ip?parameters"
    params = {
        'key':LJY_key,
        'ip':ip,
        'output':'json',
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# 静态地图函数
def staticmap(location,zoom,size=None,scale=1,markers=None,labels=None,paths=None,traffic=0):
    """静态地图函数"""
    url = "https://restapi.amap.com/v3/staticmap?parameters"
    params = {
        'key':LJY_key,
        'location':location,
        'zoom':zoom,
        'size':size,
        'scale':scale,
        'markers':markers,
        'labels':labels,
        'paths':paths,
        'traffic':traffic,
        'output':'json'
    }
    response = requests.get(url,params=params)
    data = Image.open(BytesIO(response.content))
    return data

# 坐标转化函数
def convert(locations,coordsys=None):
    """坐标转化"""
    url = "https://restapi.amap.com/v3/assistant/coordinate/convert?parameters"
    params = {
        'key':LJY_key,
        'locations':locations,
        'coordsys':coordsys,
        'output':'json',
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# 天气查询函数
def weatherinfo(city,extensions=None):
    """天气查询"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        'key':LJY_key,
        'city':city,
        'extensions':extensions,
        'output':'json',
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data

# 输入提示函数
def inputtips(keywords,types=None,location=None,city=None):
    """输入提示"""
    url = "https://restapi.amap.com/v3/assistant/inputtips?parameters"
    params = {
        'key':LJY_key,
        'keywords':keywords,
        'types':types,
        'location':location,
        'city':city,
        'output':'json',
    }
    response = requests.get(url,params=params)
    data = response.json()
    return data