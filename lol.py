from selenium import webdriver
import time

summonor = input("소환사명을 입력하세요: ")
browser = webdriver.Chrome()
browser.get('https://www.op.gg/')
browser.maximize_window


most_champions = []
kda_s = []
win_rates = []
play_times = []

# 롤 전적 검색
search = browser.find_element_by_xpath('/html/body/div[2]/div[3]/form/input')
search.send_keys(summonor)
browser.find_element_by_xpath('/html/body/div[2]/div[3]/form/button[1]/i').click()

# 전적 갱신 버튼
browser.find_element_by_xpath('//*[@id="SummonerRefreshButton"]').click()

time.sleep(5)

# 소환사 티어정보
tier = browser.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]').text
print()
print("소환사명: " +summonor)
print()
print(tier)
print()

# 모스트, KDA, 승률
for index in range(1,8):
    most_champion = browser.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[{index}]/div[2]/div[1]/a').text
    most_champions.append(most_champion)
    kda = browser.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[{index}]/div[3]').text
    kda_s.append(kda)
    win_rate = browser.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div/div[{index}]/div[4]').text
    win_rates.append(win_rate)
    print("모스트"+ str(index) +": "+ most_champions[index-1],end = " ")
    print("KDA: "+ str(kda_s[index-1]),end="\n")
    print("승률: " + str(win_rates[index-1]))
    print()

# 최근 게임 기록
rec_record =browser.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[2]').text

print("최근기록: "+ rec_record)
print()

# 게임중인가?
browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[3]/dl/dd[3]/a/span').click()

time.sleep(2)

try: 
    browser.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[7]/div/p[1]')
    print("게임중이 아닙니다.")

except:
    print("게임중입니다.") 

time.sleep(2) 

# 총 플레이 타임
browser.find_element_by_xpath('//*[@id="top_ifi"]').click()

curr_handle = browser.current_window_handle 
handles = browser.window_handles

for handle in handles:
    browser.switch_to.window(handle)   # 각 핸들로 이동
   
time.sleep(2)

for i in range(1,4):
    play_time =browser.find_element_by_xpath(f'//*[@id="root"]/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/div[{i}]').text.split('\n')
    play_times.append(play_time)


print()
print("총게임시간: "+ play_times[0][0]+"일= " + play_times[1][0] +"시간= "+ play_times[2][0]+"분")

browser.switch_to.window(curr_handle)
   
     
browser.quit()