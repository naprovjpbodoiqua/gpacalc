def calculate_grade_strategy():
    print("\n--- TOOL TÍNH ĐIỂM ---")
    
    try:
        # Nhập điểm thành phần
        print("Nhập lần lượt: Giữa kỳ(20%)  Thực hành(10%)  Quizzes(5%)  Chuyên cần(5%)")
        print("Ví dụ: 7 8 9 10")
        val = list(map(float, input(">> ").split()))
        
        if len(val) != 4:
            print("Lỗi: Nhập thiếu điểm rồi fen.")
            return

        mid, prac, quiz, attend = val
        w_final = 0.6
        
        # Tính điểm tích lũy (40% đầu)
        current = (mid * 0.2) + (prac * 0.1) + (quiz * 0.05) + (attend * 0.05)
        
        print("-" * 45)
        print(f"GPA hiện tại tích luỹ được (hệ số 0.4): {current:.2f}")
        print("-" * 45)

        # Hàm tính điểm thi cần thiết
        def get_needed_score(target_gpa):
            return (target_gpa - current) / w_final

        # 1. Để qua môn (Trên F => Total >= 4.0)
        score_pass = get_needed_score(4.0)
        pass_msg = ""
        if score_pass <= 0:
            pass_msg = "Auto qua"
            score_pass = 0 # Để dùng cho mốc dưới
        elif score_pass > 10:
            pass_msg = "Không  qua môn được"
        else:
            pass_msg = f"Cần >= {score_pass:.2f} để qua môn"
            
        print(f"{pass_msg}")

        # 2. Để ĐƯỢC học cải thiện (Dưới C => 4.0 <= Total < 5.5)
        # Tức là điểm thi phải nhỏ hơn mốc đạt 5.5
        score_reach_c = get_needed_score(5.5)
        
        if score_reach_c <= 0:
            # Hiện tại đã >= 5.5 rồi, không thể xuống D được nữa
            print(f"Điểm cuối kì cần để đạt dưới C (5.5): KHÔNG THỂ ")
        elif score_pass > 10:
            print(f"Điểm cuối kì cần để đạt dưới C (5.5): KHÔNG THỂ ")
        else:
            # Vùng an toàn để cải thiện: Từ [Qua môn] đến [Sát C]
            # Lấy score_reach_c - 0.5 để minh hoạ an toàn
            safe_max = score_reach_c - 0.5
            if safe_max < score_pass:
                print(f"Điểm cuối kì cần để đạt dưới C (5.5): Rất khó căn (Vùng điểm quá hẹp)")
            else:
                print(f"Điểm cuối kì cần để đạt dưới C (5.5): Từ {score_pass:.2f} đến < {score_reach_c:.2f} (Nên thi tầm {(score_pass - 0.5):.1f} - {safe_max:.1f})")

        # 3. Để đạt B (Total >= 7.0)
        score_b = get_needed_score(7.0)
        b_msg = ""
        if score_b <= 0:
            b_msg = "Chắc chắn đạt B (hoặc hơn)"
        elif score_b > 10:
            b_msg = f"KHÔNG THỂ (Cần {score_b:.2f})"
        else:
            b_msg = f"Cần >= {score_b:.2f}"

        print(f"Điểm cuối kì cần để đạt B (7.0): {b_msg}")

    except ValueError:
        print("Lỗi: Nhập số không đúng định dạng.")

if __name__ == "__main__":
    calculate_grade_strategy()