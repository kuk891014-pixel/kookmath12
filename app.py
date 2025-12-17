import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="국희재수학전문학원 봉선점 예약",
    page_icon="🎓",
    layout="centered"
)

# 2. 고급스러운 스타일링 (블랙 & 골드)
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .stApp {
        background-color: #ffffff;
    }
    
    /* 메인 헤더 */
    .main-header {
        font-family: 'Helvetica', 'Malgun Gothic', sans-serif;
        font-size: 2.0rem;
        color: #000000;
        text-align: center;
        font-weight: 800;
        margin-top: 1rem;
        letter-spacing: -1px;
    }
    
    /* 서브 헤더 */
    .sub-header {
        font-size: 1.0rem;
        color: #555555;
        text-align: center;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* 강조 박스 */
    .info-box {
        background-color: #f8f9fa;
        border-left: 5px solid #d4af37; /* 골드 라인 */
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
        color: #333;
        font-size: 0.95rem;
    }

    /* 버튼 스타일 (Streamlit 기본 버튼 덮어쓰기 안됨 -> st.link_button 사용) */
    
    /* 푸터 */
    .footer {
        text-align: center;
        color: #888;
        font-size: 0.8rem;
        margin-top: 50px;
        border-top: 1px solid #eee;
        padding-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 로고 및 타이틀 영역
st.markdown('<div class="main-header">국희재수학전문학원<br><span style="color:#d4af37;">봉선점</span> 예약 센터</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">프리미엄 고등 전문 수학<br><b>Level Test 및 입학 상담</b></div>', unsafe_allow_html=True)

st.write("---")

# 4. 안내 문구
st.markdown("""
    <div class="info-box">
        <b>📢 예약 안내</b><br>
        원활한 상담을 위해 학생의 학습 현황과<br>
        희망하는 상담 시간을 미리 남겨주세요.<br>
        <br>
        아래 버튼을 누르시면 <b>예약 작성 페이지</b>로 이동합니다.
    </div>
""", unsafe_allow_html=True)

# 5. 네이버 폼 연결 버튼 (여기에 원장님의 네이버 폼 주소를 넣으세요!)
# 👇👇👇 "https://naver.me/xxxxx" 부분을 실제 주소로 바꿔주세요 👇👇👇
naver_form_url = "https://naver.me/5owC88zV" 

st.link_button("📅 상담 예약 작성하기 (Click)", naver_form_url, use_container_width=True)

# 6. 추가 정보 (선택 사항)
st.write("")
st.write("")
with st.expander("📍 오시는 길 및 문의"):
    st.write("**주소:** 광주광역시 남구 봉선동 (상세주소 입력)")
    st.write("**상담 문의:** 010-XXXX-XXXX")

# 7. 푸터
st.markdown('<div class="footer">Kuk Hee Jae Math Specialist Academy<br>Bongseon Branch</div>', unsafe_allow_html=True)