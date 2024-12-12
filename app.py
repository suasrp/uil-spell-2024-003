import streamlit as st

# Function to safely access secrets with a fallback if a key doesn't exist
def get_secret(key, default=None):
    return st.secrets.get(key, default)

# Access credentials securely from st.secrets (with safe fallback)
USER_CREDENTIALS = {
    "user5a": get_secret("user5a"),
    "user5b": get_secret("user5b"),
    "user5c": get_secret("user5c"),
    "user5t": get_secret("user5t"),
    "user6a": get_secret("user6a"),
    "user6b": get_secret("user6b"),
    "user6c": get_secret("user6c"),
    "user6t": get_secret("user6t"),
}

# Check if any secret is missing
missing_secrets = [key for key, value in USER_CREDENTIALS.items() if value is None]
if missing_secrets:
    st.error(f"Missing secrets: {', '.join(missing_secrets)}. Please check your secrets configuration.")
    st.stop()

def login():
    """Function to handle user login"""
    st.title("Login Page")
    
    # If the user is already logged in, don't show the login form
    if "username" in st.session_state:
        st.success(f"Welcome, {st.session_state['username']}!")
        # Redirect to the Vercel URL after successful login
        st.experimental_rerun()  # Rerun to load the main app
        st.experimental_redirect("https://spulflaskt05df.vercel.app")
        return True

    # Display login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Authentication logic: Check if username and password are correct
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            # Store username in session state
            st.session_state["username"] = username
            st.session_state["logged_in"] = True
            st.experimental_rerun()  # Rerun the app to load the main app after login
            return True
        else:
            st.error("Invalid username or password")
    
    return False

def main_app():
    """Main application to show after successful login"""
    st.title("Main Application")
    st.write("You are now logged in and can interact with the main app!")
    if st.button("Log out"):
        st.session_state.clear()  # Clear session state on logout
        st.experimental_rerun()  # Rerun to go back to login page

def main():
    """Main function to handle page logic"""
    if not login():
        main_app()  # Show the main app if logged in
    else:
        pass

if __name__ == "__main__":
    main()
