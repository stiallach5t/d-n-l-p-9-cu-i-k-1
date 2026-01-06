import streamlit as st
from PIL import Image

# Cấu hình trang web
st.set_page_config(
    page_title="Duyên Hải Miền Trung - to4lol.xyz",
    page_icon="🌊",
    layout="wide"
)

# Tùy chỉnh giao diện bằng CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTitle {
        color: #1E3A8A;
        font-family: 'Helvetica Neue', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Thanh điều hướng (Sidebar) giống mục lục thuyết trình
st.sidebar.title("📌 Nội dung bài giảng")
selection = st.sidebar.radio("Chọn chương:", [
    "1. Giới thiệu chung", 
    "2. Thế mạnh Kinh tế", 
    "3. Du lịch & Văn hóa", 
    "4. Hạ tầng & Tương lai"
])

# --- PHẦN 1: GIỚI THIỆU ---
if selection == "1. Giới thiệu chung":
    st.title("🌊 Duyên hải Miền Trung: Tiềm năng & Thách thức")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        Vùng Duyên hải Miền Trung bao gồm 14 tỉnh thành từ Thanh Hóa đến Bình Thuận. 
        Đây là 'mặt tiền' của Việt Nam hướng ra Biển Đông, đóng vai trò chiến lược trong an ninh quốc phòng và kinh tế biển.
        
        * **Diện tích:** Chiếm khoảng 28% diện tích cả nước.
        * **Bờ biển:** Dài hơn 1.900 km.
        """)
    with col2:
        # Sử dụng ảnh minh họa từ URL để tránh lỗi file local
        st.image("https://images.unsplash.com/photo-1559592413-7ece35936503?auto=format&fit=crop&w=800", 
                 caption="Vẻ đẹp bờ biển Miền Trung")

# --- PHẦN 2: KINH TẾ ---
elif selection == "2. Thế mạnh Kinh tế":
    st.title("📈 Phát triển Kinh tế Trọng điểm")
    
    tab1, tab2, tab3 = st.tabs(["Kinh tế biển", "Công nghiệp", "Nông nghiệp"])
    
    with tab1:
        st.subheader("Hệ thống Cảng biển")
        st.write("Với các cảng nước sâu như Nghi Sơn, Vũng Áng, Tiên Sa, Quy Nhơn, Cam Ranh...")
    
    with tab2:
        st.subheader("Khu kinh tế & Công nghiệp")
        st.info("Lọc hóa dầu Nghi Sơn, Dung Quất là trụ cột năng lượng quốc gia.")
        # Ví dụ biểu đồ đơn giản
        st.bar_chart({"Tỉ trọng GDP (%)": [15, 25, 30, 20, 10]})

# --- PHẦN 3: DU LỊCH ---
elif selection == "3. Du lịch & Văn hóa":
    st.title("🏛️ Con đường Di sản Miền Trung")
    st.write("Miền Trung là nơi tập trung nhiều di sản văn hóa thế giới nhất Việt Nam.")
    
    cols = st.columns(3)
    with cols[0]:
        st.image("https://images.unsplash.com/photo-1583417319070-4a69db38a482?auto=format&fit=crop&w=400", caption="Cố đô Huế")
    with cols[1]:
        st.image("https://images.unsplash.com/photo-1599708153386-62bf3f035773?auto=format&fit=crop&w=400", caption="Hội An")
    with cols[2]:
        st.image("https://images.unsplash.com/photo-1504457047772-27fb18144da9?auto=format&fit=crop&w=400", caption="Bà Nà Hills")

# --- PHẦN 4: HẠ TẦNG ---
elif selection == "4. Hạ tầng & Tương lai":
    st.title("🚀 Tầm nhìn đến 2030")
    st.success("Mục tiêu: Trở thành vùng kinh tế năng động, hiện đại và thích ứng tốt với biến đổi khí hậu.")
    
    st.markdown("""
    * **Giao thông:** Cao tốc Bắc-Nam, Đường ven biển quốc gia.
    * **Năng lượng:** Phát triển mạnh điện gió và điện mặt trời tại Ninh Thuận, Bình Thuận.
    * **Website:** Được vận hành tại địa chỉ **to4lol.xyz**
    """)
    st.balloons() # Hiệu ứng chúc mừng khi kết thúc bài thuyết trình

# Chân trang
st.sidebar.markdown("---")
st.sidebar.write("💻 Website phát triển bởi Tổ 4")
st.sidebar.info("Domain: to4lol.xyz")