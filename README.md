# lol
해당 코드는 selenium 라이브러리를 연습하기 위해서 만들었습니다.

기능 : selenium 라이브러리를 활용하여 op.gg 사이트에서 각종 데이터를 불러옵니다.

코드를 실행하기 앞서 크롬의 버젼을 살펴야합니다.

오른쪽 상단에 . 3개 버튼을 누르고 설정에 들어가서 현재 자신의 크롬 버젼을 확인합니다.

해당 버젼에 맞는 크롬 드라이버를 설치해야 selenium이 정상 작동하기 때문에 이 과정이 필요합니다.

확인했다면 구글 검색창에 크롬드라이버를 치고 홈페이지에 들어가서 자신의 버젼에 맞게 설치해줍니다.

이 파일을 lol.py가 들어간 디렉토리에 넣어주면 됩니다.

이제 코드를 실행 해봅시다.
코드를 실행하면 터미널에 "소환사명을 입력하세요: " 라고 뜨고 데이터를 불러올 롤 닉네임을 적어줍니다.
그럼 selenium을 통해 op.gg 사이트에서 닉네임을 자동으로 검색하고 
전적 갱신버튼을 누른다음 해당 닉네임의 승패, 현재 게임 여부,챔피언 모스트(5개까지), 롤 플레이 시간을 터미널 창에 불러옵니다.

