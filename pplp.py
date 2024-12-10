import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Streamlit app
st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# User input
input_temp = st.number_input("Enter the temperature value:", value=0.0)
input_unit = st.selectbox("Select the input unit:", ["Celsius", "Fahrenheit", "Kelvin"])
output_unit = st.selectbox("Select the output unit:", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion logic
if st.button("Convert"):
    if input_unit == output_unit:
        st.success(f"The temperature is the same: {input_temp:.2f} {output_unit}")
    else:
        if input_unit == "Celsius" and output_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(input_temp)
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            result = celsius_to_kelvin(input_temp)
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            result = fahrenheit_to_celsius(input_temp)
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            result = fahrenheit_to_kelvin(input_temp)
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            result = kelvin_to_celsius(input_temp)
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            result = kelvin_to_fahrenheit(input_temp)
        
        st.success(f"The converted temperature is: {result:.2f} {output_unit}")
