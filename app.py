import streamlit as st
import openai

# API 키 설정 (실제 API 키는 환경 변수나 다른 안전한 방법으로 관리하는 것이 좋습니다)
openai.api_key = "your-openai-api-key"

# 예시 데이터 (드롭다운에서 선택할 수 있는 항목들)
genres = ["판타지 🏰", "공상과학 🚀", "로맨스 💖", "미스터리 🔍", "공포 👻"]
worlds = ["중세 왕국 🌍", "우주 탐험 🌌", "현대 도시 🏙️", "좀비 아포칼립스 🧟", "미래 도시 🌆"]
sidekicks = ["용감한 전사 ⚔️", "AI 로봇 🤖", "귀여운 동물 🐶", "슬픈 과거를 가진 인물 😔"]

# 사용자 입력 받기
def get_user_input():
    protagonist = st.text_input("주인공의 이름을 입력하세요:")
    theme = st.text_input("소설의 주제를 입력하세요:")

    # 드롭다운 선택: 장르
    genre = st.selectbox("소설의 장르를 선택하세요:", genres)
    st.markdown(f"**선택한 장르**: {genre}")

    # 드롭다운 선택: 세계관
    world = st.selectbox("세계관을 선택하세요:", worlds)
    st.markdown(f"**선택한 세계관**: {world}")

    # 드롭다운 선택: 조연
    sidekick = st.selectbox("조연을 선택하세요:", sidekicks)
    st.markdown(f"**선택한 조연**: {sidekick}")

    return protagonist, theme, genre, world, sidekick

def generate_story(protagonist, theme, genre, world, sidekick):
    # 장르, 세계관, 조연에 대한 선택 값을 텍스트로 변환
    genre = genre.split(' ')[0]  # 이모티콘을 제외한 장르 이름만 추출
    world = world.split(' ')[0]
    sidekick = sidekick.split(' ')[0]

    prompt = f"""
    주인공은 {protagonist}이고, 주제는 {theme}입니다.
    장르는 {genre}이며, 세계관은 {world}입니다.
    조연은 {sidekick}이며, 이들의 이야기를 바탕으로 소설을 생성해주세요.
    """

    # 최신 API 방식으로 수정
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 최신 모델 명칭
        messages=[
            {"role": "system", "content": "You are a story generator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    story = response['choices'][0]['message']['content'].strip()
    return story

def main():
    st.title("소설 생성기 ✨")

    protagonist, theme, genre, world, sidekick = get_user_input()

    if st.button("소설 생성"):
        if protagonist and theme and genre and world and sidekick:
            story = generate_story(protagonist, theme, genre, world, sidekick)
            st.subheader("생성된 소설:")
            st.write(story)

if __name__ == "__main__":
    main()

