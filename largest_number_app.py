import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers to find the largest among them:")
    
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

if __name__ == "__main__":
    main()
