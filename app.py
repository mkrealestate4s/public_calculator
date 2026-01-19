import streamlit as st

st.set_page_config(page_title="상가 수익률 6% 계산기", layout="centered")

st.title("📊 상가 수익률 6% 계산기")
st.write("※ 현 임차인 기준 단순 수익률 (1차 필터용)")

def num_to_korean(num):
    units = ["", "만", "억", "조"]
    if num == 0:
        return "0원"

    result = ""
    unit_index = 0
    while num > 0:
        part = num % 10000
        if part > 0:
            result = f"{part:,}{units[unit_index]} " + result
        num //= 10000
        unit_index += 1
    return result.strip() + "원"

# ===== 입력 =====
sale_price = st.number_input("매매가격 (원)", min_value=0, step=10000000)
st.caption(f"매매가격: **{sale_price:,}원** ({num_to_korean(sale_price)})")
deposit = st.number_input("보증금 (원)", min_value=0, step=1000000)
st.caption(f"보증금: **{deposit:,}원** ({num_to_korean(deposit)})")
monthly_rent = st.number_input("월세 (원)", min_value=0, step=100000)
st.caption(f"월세: **{monthly_rent:,}원** ({num_to_korean(monthly_rent)})")

st.divider()

# ===== 계산 버튼 =====
if st.button("📌 수익률 계산하기"):

    if sale_price <= deposit or monthly_rent <= 0:
        st.error("매매가격은 보증금보다 커야 하고, 월세는 0보다 커야 합니다.")
    else:
        annual_rent = monthly_rent * 12
        real_invest = sale_price - deposit
        yield_rate = (annual_rent / real_invest) * 100

        st.subheader(f"📈 연 수익률: **{yield_rate:.2f}%**")

        # ===== 6% 이상 =====
        if yield_rate >= 6:
            st.success("✅ 수익률 6% 이상 — 검토 가능한 물건입니다.")

        # ===== 6% 미만 =====
        else:
            st.warning("⚠ 수익률 6% 미만 — 가격 조정이 필요합니다.")

            target_price = int((annual_rent / 0.06) + deposit)
            gap = sale_price - target_price

            st.write("### 🔍 수익률 6% 기준 적정 매매가격")
            st.write(f"- **적정 매매가격:** {target_price:,}원 ({num_to_korean(target_price)})")

            if gap > 0:
                st.write(f"- **가격 조정 필요:** {gap:,}원 ↓")
            else:
                st.write("- 이미 6% 이상 구조입니다.")
