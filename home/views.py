from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
import sqlite3
from home.models import UserName
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    # item = UserName.objects.get(id=4)
    # item.delete()

    user_list = []
    info_dic = dict()
    all_info = []
    all_user = UserName.objects.all()
    all_user = all_user.values()
    for i in all_user:
        user_list.append(i['Name'])

    for name in user_list:
        url = 'https://www.op.gg/summoner/userName='
        urls = url + name
        op_gg = requests.get(urls, verify=False)
        soup = BeautifulSoup(op_gg.content, "lxml")
        type = soup.find("div", {"class": "GameType"}).text
        time = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary '
                           '> '
                           'div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > '
                           'div.Content '
                           '> div.GameStats > div.TimeStamp > span')[0].text
        result = soup.find("div", {"class": "GameResult"}).text
        champion = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                               '-summary '
                               '> div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > '
                               'div.Content > div.GameSettingInfo > div.ChampionName > a')[0].text
        solo_rank = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                                '-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')[
            0].text
        free_rank = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                                '-summary > div.SideContent > div.sub-tier > div > div.sub-tier__rank-tier')[0].text
        info_dic['name'] = name
        info_dic['type'] = re.sub('<.+?>', '', type, 0).strip()
        info_dic['time'] = time
        info_dic['result'] = re.sub('<.+?>', '', result, 0).strip()
        info_dic['champion'] = champion
        info_dic['solo'] = solo_rank
        info_dic['free'] = free_rank
        all_info.append(info_dic)
        info_dic = {}
    return render(request, 'home.html', {'info': all_info})


@csrf_exempt
def search(request):
    search = request.GET['search2']
    url = 'https://www.op.gg/summoner/userName='
    urls = url + search
    op_gg = requests.get(urls, verify=False)
    soup = BeautifulSoup(op_gg.content, "lxml")
    info_dic = dict()
    all_info = []
    try:
        type = soup.find("div", {"class": "GameType"}).text
        time = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary '
                           '> '
                           'div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > '
                           'div.Content '
                           '> div.GameStats > div.TimeStamp > span')[0].text
        result = soup.find("div", {"class": "GameResult"}).text
        champion = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                               '-summary '
                               '> div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > '
                               'div.Content > div.GameSettingInfo > div.ChampionName > a')[0].text
        solo_rank = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                                '-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')[
            0].text
        free_rank = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                                '-summary > div.SideContent > div.sub-tier > div > div.sub-tier__rank-tier')[0].text
        info_dic['name'] = search
        info_dic['type'] = re.sub('<.+?>', '', type, 0).strip()
        info_dic['time'] = time
        info_dic['result'] = re.sub('<.+?>', '', result, 0).strip()
        info_dic['champion'] = champion
        info_dic['solo'] = solo_rank
        info_dic['free'] = re.sub('<.+?>', '', free_rank, 0).strip()
        all_info.append(info_dic)
        info_dic = {}

        return render(request, 'search.html', {'info': all_info})

    except:
        return render(request, 'search.html', {'search': search})


@csrf_exempt
def save(request):
    user = request.POST.get('btn_save', False)
    u = UserName(Name=user)
    u.save()
    a = 1
    user_list = []
    info_dic = dict()
    all_info = []
    all_user = UserName.objects.all()
    all_user = all_user.values()
    for i in all_user:
        user_list.append(i['Name'])

    for name in user_list:
        url = 'https://www.op.gg/summoner/userName='
        urls = url + name
        op_gg = requests.get(urls, verify=False)
        soup = BeautifulSoup(op_gg.content, "lxml")
        type = soup.find("div", {"class": "GameType"}).text
        time = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary '
                           '> '
                           'div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > '
                           'div.Content '
                           '> div.GameStats > div.TimeStamp > span')[0].text
        result = soup.find("div", {"class": "GameResult"}).text
        champion = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                               '-summary '
                               '> div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > '
                               'div.Content > div.GameSettingInfo > div.ChampionName > a')[0].text
        solo_rank = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                                '-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')[
            0].text
        free_rank = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout'
                                '-summary > div.SideContent > div.sub-tier > div > div.sub-tier__rank-tier')[0].text
        info_dic['name'] = name
        info_dic['type'] = re.sub('<.+?>', '', type, 0).strip()
        info_dic['time'] = time
        info_dic['result'] = re.sub('<.+?>', '', result, 0).strip()
        info_dic['champion'] = champion
        info_dic['solo'] = solo_rank
        info_dic['free'] = free_rank
        all_info.append(info_dic)
        info_dic = {}
    return render(request, 'home.html', {'info': all_info})
