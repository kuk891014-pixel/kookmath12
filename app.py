import streamlit as st

# 1. 페이지 기본 설정 (탭 이름, 아이콘 설정)
st.set_page_config(
    page_title="국희재수학전문학원 봉선점 예약",
    page_icon="🎓",
    layout="centered"
)

# 2. 고급스러운 스타일링 (CSS 적용)
st.markdown("""
    <style>
    /* 웹 폰트 임포트 (Noto Sans KR, Gmarket Sans) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    @font-face {
        font-family: 'GmarketSansBold';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansBold.woff') format('woff');
        font-weight: normal;
        font-style: normal;
    }

    /* 전체 배경 및 기본 폰트 설정 */
    .stApp {
        background-color: #fdfdfd; /* 아주 연한 회색 배경으로 깊이감 추가 */
        font-family: 'Noto Sans KR', sans-serif;
        color: #333;
    }
    
    /* 메인 헤더 스타일 */
    .main-header-container {
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .main-title {
        font-family: 'GmarketSansBold', sans-serif; /* 임팩트 있는 제목 폰트 */
        font-size: 2.4rem;
        color: #222;
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
    }
    .branch-name {
        display: inline-block;
        position: relative;
        color: #d4af37; /* 기본 골드 색상 */
        /* 골드 그라데이션 텍스트 효과 (일부 브라우저 지원) */
        background: linear-gradient(to right, #bf9b30, #ffd700, #bf9b30);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 서브 헤더 스타일 */
    .sub-header {
        font-size: 1.05rem;
        color: #666;
        text-align: center;
        margin-bottom: 2.5rem;
        line-height: 1.7;
        font-weight: 500;
    }
    
    /* 구분선 스타일 */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(212, 175, 55, 0.75), rgba(0, 0, 0, 0));
        margin: 2rem 0;
    }

    /* 강조 안내 박스 스타일 */
    .info-box-container {
        display: flex;
        justify-content: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #fff;
        border-left: 6px solid #d4af37; /* 골드 포인트 라인 */
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); /* 부드러운 그림자로 입체감 부여 */
        color: #444;
        font-size: 1rem;
        line-height: 1.8;
        width: 95%; /* 모바일 대응 */
        max-width: 600px;
    }
    .info-box-title {
        font-weight: 700;
        font-size: 1.1rem;
        color: #d4af37;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .info-box-icon {
        margin-right: 8px;
        font-size: 1.3rem;
    }

    /* 버튼 스타일 커스터마이징 (st.link_button 대상) */
    div[data-testid="stLinkButton"] > a {
        background: linear-gradient(to right, #d4af37, #edc967); /* 골드 그라데이션 배경 */
        color: white !important; /* 글자색 흰색 고정 */
        border: none;
        padding: 15px 30px;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 50px; /* 둥근 버튼 */
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3); /* 버튼 그림자 */
        transition: all 0.3s ease; /* 부드러운 전환 효과 */
        display: block;
        text-align: center;
        text-decoration: none;
    }
    div[data-testid="stLinkButton"] > a:hover {
        background: linear-gradient(to right, #bf9b30, #d4af37); /* 호버 시 색상 변경 */
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.5); /* 호버 시 그림자 강조 */
        transform: translateY(-2px); /* 살짝 떠오르는 효과 */
    }
    
    /* 익스팬더 (오시는 길) 스타일 */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #333;
        border: 1px solid #eee;
        border-radius: 8px;
        background-color: #fff;
    }
    .streamlit-expanderContent {
        border: 1px solid #eee;
        border-top: none;
        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
        padding: 20px;
        background-color: #fff;
    }

    /* 푸터 스타일 */
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.85rem;
        margin-top: 60px;
        border-top: 1px solid #eaeaea;
        padding-top: 30px;
        padding-bottom: 20px;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 로고 및 타이틀 영역
st.markdown("""
    <div class="main-header-container">
        <div class="main-title">국희재수학전문학원<br><span class="branch-name">봉선점 예약 센터</span></div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="sub-header">
        프리미엄 고등 전문 수학<br>
        <b>1:1 심층 Level Test 및 입학 상담</b>
    </div>
""", unsafe_allow_html=True)

st.write("---") # 커스텀 디자인된 구분선 적용됨

# 4. 안내 문구
st.markdown("""
    <div class="info-box-container">
        <div class="info-box">
            <div class="info-box-title"><span class="info-box-icon">📢</span> 예약 안내</div>
            원활하고 깊이 있는 상담을 위해<br>
            학생의 현재 학습 현황과 희망하는 상담 시간을<br>
            미리 남겨주시면 감사하겠습니다.<br>
            <br>
            아래 버튼을 클릭하시면 <b>예약 작성 페이지</b>로 이동합니다.
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. 네이버 폼 연결 버튼
st.write("") # 여백 추가
# 👇👇👇 "https://naver.me/xxxxx" 부분을 실제 원장님의 네이버 폼 주소로 꼭 바꿔주세요! 👇👇👇
naver_form_url = "https://naver.me/xLsTVmCk" 
st.link_button("📅 상담 예약 작성하기 (Click)", naver_form_url, use_container_width=True)
st.write("") # 여백 추가

# 6. 추가 정보 (선택 사항 - 아이콘 추가로 가독성 높임)
with st.expander("📍 오시는 길 및 문의 안내"):
    st.markdown("""
        <div style="padding: 10px 0;">
            <div style="margin-bottom: 15px;">
                <b>🏢 주소</b><br>
                광주광역시 남구 봉선2로 49 3층 국희재수학전문학원 봉선점 (상세 주소를 여기에 입력해주세요)
            </div>
            <div>
                <b>📞 상담 문의</b><br>
                010-6662-6542 (전화번호를 입력해주세요)
            </div>
        </div>
    """, unsafe_allow_html=True)

# 7. 푸터
st.markdown('<div class="footer">Kuk Hee Jae Math Specialist Academy<br>Bongseon Branch | Premium Education Service</div>', unsafe_allow_html=True)
