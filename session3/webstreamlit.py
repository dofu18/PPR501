import streamlit as st
import re

# ===== VALIDATION FUNCTIONS =====
def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


# ===== SIGN UP LOGIC =====
def signup(email, password):
    if not is_valid_email(email):
        st.error("❌ Email không đúng định dạng")
        return

    if not is_valid_password(password):
        st.error(
            "❌ Password phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt"
        )
        return

    # Nếu pass validation
    st.success("✅ Đăng ký thành công!")
    st.balloons()


def main():
    st.title("Welcome to Web Streamlit!")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        signup(email, password)

if __name__ == "__main__":
    main()