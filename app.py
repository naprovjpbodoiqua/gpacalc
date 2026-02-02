import streamlit as st

# Cấu hình trang
st.set_page_config(page_title=" Grade Calculator", page_icon="🎓")

st.title("Grade Calculator")
st.write("Tool tính điểm")

# Tạo 4 cột để nhập điểm cho đẹp
col1, col2, col3, col4 = st.columns(4)

with col1:
    mid = st.number_input("Giữa kỳ (20%)", min_value=0.0, max_value=10.0, step=0.1, value=7.0)
with col2:
    prac = st.number_input("Thực hành (10%)", min_value=0.0, max_value=10.0, step=0.1, value=8.0)
with col3:
    quiz = st.number_input("Quizzes (5%)", min_value=0.0, max_value=10.0, step=0.1, value=9.0)
with col4:
    attend = st.number_input("Chuyên cần (5%)", min_value=0.0, max_value=10.0, step=0.1, value=10.0)

# Trọng số
w_final = 0.6
current = (mid * 0.2) + (prac * 0.1) + (quiz * 0.05) + (attend * 0.05)

st.divider()

# Hiển thị điểm tích lũy
st.subheader(f"Điểm bộ phận (hệ số 0.4): :blue[{current:.2f}]")
st.caption(f"Bạn cần thêm bao nhiêu điểm thi (hệ số 0.6) để đạt mục tiêu?")

# Hàm tính logic
def get_needed_score(target_gpa):
    return (target_gpa - current) / w_final

# --- Xử lý hiển thị kết quả ---
col_res1, col_res2 = st.columns(2)

# 1. Mục tiêu qua môn (D - 4.0)
score_pass = get_needed_score(4.0)
with col_res1:
    st.info(" Qua môn (>= 4.0)")
    if score_pass <= 0:
        st.success("✅ Đã qua môn")
        score_pass = 0
    elif score_pass > 10:
        st.error(f"❌ No hope (Cần {score_pass:.2f})")
    else:
        st.warning(f"Cần thi >= **{score_pass:.2f}**")

# 2. Mục tiêu B (7.0)
score_b = get_needed_score(7.0)
with col_res2:
    st.info("⭐ Đạt B (>= 7.0)")
    if score_b <= 0:
        st.success("✅ Chắc chắn B")
    elif score_b > 10:
        st.error(f"❌ Không thể (Cần {score_b:.2f})")
    else:
        st.warning(f"Cần thi >= **{score_b:.2f}**")

# 3. Chiến thuật né C (Dưới 5.5)
st.divider()
st.subheader(" Chiến thuật: Né C để học cải thiện")
score_reach_c = get_needed_score(5.5)

if score_reach_c <= 0:
    st.error("Không thể về D.")
elif score_pass > 10:
    st.error(" Đã trượt, không còn cơ hội.")
else:
    safe_max = score_reach_c - 0.1
    if safe_max < score_pass:
        st.warning("Rất dễ dính C!")
    else:
        st.success(f"🎯 Để đạt D/D+ , điểm thi cần trong khoảng:")
        st.markdown(f"### `{score_pass:.2f}` $\le$ Điểm Thi $<$ `{score_reach_c:.2f}`")
        st.caption(f"(Lời khuyên : Thi tầm {score_pass+0.5:.2f} đến {safe_max-0.5:.2f})")

# Nút tác giả (Credit)
st.write("---")
st.caption(" by na")