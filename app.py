import streamlit as st

st.set_page_config(page_title="상가 수익률 계산기", layout="centered")

st.title("📊 상가 수익률 6% 계산기")
st.write("※ 현 임차인 기준 단순 수익률 (1차 필터용)")

sale_price = st.number_input("매매가격 (원)", min_value=0, step=10000000)
deposit = st.number_input("보증금 (원)", min_value=0, step=1000000)
monthly_rent = st.number_input("월세 (원)", min_value=0, step=100000)

if sale_price > deposit and monthly_rent > 0:
    annual_rent = monthly_rent * 12
    real_invest = sale_price - deposit
    yield_rate = (annual_rent / real_invest) * 100

    st.divider()
    st.subheader(f"📌 연 수익률: **{yield_rate:.2f}%**")

    if yield_rate >= 6:
        st.success("✅ 6% 이상 물건 (검토 대상)")
    else:
        st.error("❌ 6% 미만 (가격 협상 또는 제외)")
