import streamlit as st
import random

# 영어 이름 리스트 및 의미 사전
names_meanings = {
    "James": "이름 제임스의 의미는 '대체하는 사람'입니다. 😊",
    "Mary": "이름 메리의 의미는 '사랑받는 사람'입니다. 💖",
    "John": "이름 존의 의미는 '하나님의 은혜를 받은 사람'입니다. 🙏",
    "Patricia": "이름 패트리샤의 의미는 '귀족'입니다. 👑",
    "Robert": "이름 로버트의 의미는 '밝은 명성'입니다. 🌟",
    "Jennifer": "이름 제니퍼의 의미는 '공정한 사람'입니다. ⚖️",
    "Michael": "이름 마이클의 의미는 '하나님과 같은 사람'입니다. 😇",
    "Linda": "이름 린다의 의미는 '아름다운 사람'입니다. 🌸",
    "William": "이름 윌리엄의 의미는 '결단력 있는 보호자'입니다. 🛡️",
    "Elizabeth": "이름 엘리자베스의 의미는 '하나님께 서약한 사람'입니다. 🕊️",
    "David": "이름 데이비드의 의미는 '사랑받는 사람'입니다. 💙",
    "Barbara": "이름 바바라의 의미는 '외국인 여성'입니다. 🌍",
    "Richard": "이름 리처드의 의미는 '지배적인 통치자'입니다. 👑",
    "Susan": "이름 수잔의 의미는 '백합꽃'입니다. 🌺",
    "Joseph": "이름 조셉의 의미는 '하나님이 더해주실 것입니다'입니다. ✨",
    "Jessica": "이름 제시카의 의미는 '하나님이 보신다'입니다. 👁️",
    "Thomas": "이름 토마스의 의미는 '쌍둥이'입니다. 👬",
    "Sarah": "이름 사라의 의미는 '공주'입니다. 👸",
    "Charles": "이름 찰스의 의미는 '자유로운 사람'입니다. 🕊️",
    "Karen": "이름 카렌의 의미는 '순수한 사람'입니다. 🌼",
    "Christopher": "이름 크리스토퍼의 의미는 '그리스도를 나르는 사람'입니다. ✝️",
    "Nancy": "이름 낸시의 의미는 '은혜'입니다. 🙏",
    "Daniel": "이름 다니엘의 의미는 '하나님은 나의 심판자'입니다. ⚖️",
    "Lisa": "이름 리사의 의미는 '하나님께 서약한 사람'입니다. 🕊️",
    "Diana": "이름 다이애나의 의미는 '신의 은총을 받은'입니다. 🌟"
}

# 남자 이름 리스트
male_names = [
    "James", "John", "Robert", "Michael", "William",
    "David", "Richard", "Joseph", "Thomas", "Charles",
    "Christopher", "Daniel"
]

# 여자 이름 리스트
female_names = [
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth",
    "Barbara", "Susan", "Jessica", "Sarah", "Karen",
    "Nancy", "Lisa", "Diana"
]

# 남자 배우 리스트 및 이미지 URL
male_actors = {
    "Leonardo DiCaprio": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Leonardo_DiCaprio_2014.jpg",
    "Brad Pitt": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Brad_Pitt_in_2019.jpg",
    "Robert Downey Jr.": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg",
    "Chris Hemsworth": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Chris_Hemsworth_2017.jpg"
}

# 여자 배우 리스트 및 이미지 URL
female_actors = {
    "Scarlett Johansson": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Scarlett_Johansson_in_2019.jpg",
    "Angelina Jolie": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Angelina_Jolie_2_June_2014_%28cropped%29.jpg",
    "Jennifer Lawrence": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Jennifer_Lawrence_at_2018_Tribeca.jpg",
    "Emma Watson": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Emma_Watson_2013.jpg"
}

# Streamlit 앱 설정
st.title('영어 이름 추천 챗봇')

# 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'gender' not in st.session_state:
    st.session_state.gender = ''
if 'image_choice' not in st.session_state:
    st.session_state.image_choice = ''
if 'actor_choice' not in st.session_state:
    st.session_state.actor_choice = ''
if 'recommended_name' not in st.session_state:
    st.session_state.recommended_name = ''
if 'meaning' not in st.session_state:
    st.session_state.meaning = ''

# 첫 번째 단계: 성별 선택
if st.session_state.step == 0:
    st.session_state.gender = st.selectbox('성별을 선택하세요:', ['남자', '여자'])
    if st.button('다음'):
        st.session_state.step = 1

# 두 번째 단계: 이미지 선택
elif st.session_state.step == 1:
    if st.session_state.gender == '남자':
        st.session_state.image_choice = st.radio(
            '다음 중 어떤 이미지를 상상하십니까?',
            ('부드러움', '터프함', '용감함', '지적임')
        )
    else:
        st.session_state.image_choice = st.radio(
            '다음 중 어떤 이미지를 상상하십니까?',
            ('친절함', '우아함', '귀여움', '강인함')
        )
    if st.button('다음'):
        st.session_state.step = 2

# 세 번째 단계: 배우 선택
elif st.session_state.step == 2:
    if st.session_state.gender == '남자':
        actor_choice = st.radio(
            '좋아하는 영화배우를 선택하세요:',
            list(male_actors.keys()),
            horizontal=True
        )
        st.image(male_actors[actor_choice], caption=actor_choice, width=150)
        st.session_state.actor_choice = actor_choice
    else:
        actor_choice = st.radio(
            '좋아하는 영화배우를 선택하세요:',
            list(female_actors.keys()),
            horizontal=True
        )
        st.image(female_actors[actor_choice], caption=actor_choice, width=150)
        st.session_state.actor_choice = actor_choice
    if st.button('다음'):
        st.session_state.step = 3

# 네 번째 단계: 이름 추천
elif st.session_state.step == 3:
    st.write('버튼을 클릭하여 당신에게 어울리는 영어 이름을 추천받으세요!!!')
    if st.button('이름 추천'):
        if st.session_state.gender == '남자':
            recommended_name = random.choice(male_names)
        else:
            recommended_name = random.choice(female_names)
        
        meaning = names_meanings[recommended_name]
        st.session_state.recommended_name = recommended_name
        st.session_state.meaning = meaning
        st.write(f'추천 이름: **{recommended_name}** {meaning.split(" ")[-1]}')
        st.write(meaning)
        st.session_state.step = 4

# 다섯 번째 단계: 결과 확인 및 선택
elif st.session_state.step == 4:
    st.write(f'추천 이름: **{st.session_state.recommended_name}**')
    st.write(st.session_state.meaning)
    st.write('이름이 마음에 드시나요?')
    col1, col2 = st.columns(2)
    with col1:
        if st.button('내 이름으로 채택'):
            st.balloons()
            st.session_state.step = 0
    with col2:
        if st.button('다시 추천해줘'):
            st.session_state.step = 2
