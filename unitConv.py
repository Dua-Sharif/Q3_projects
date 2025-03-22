import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: blue;
        color: white;
    }
    .stApp {
        background: linear-gradient(134deg, peach, orange)
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    h1{
        text-align: center;
        margin-bottom: 20px;
        font-size: 36px;
        color: white;
        }
        .stButton>button{
            background: linear-gradient(134deg, #0b5394, #351c75);
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        .stButton>button:hover{
            color: black;
            transform: scale(1.05);
            background: linear-gradient(45deg, #92fe9d, #00c9cf);
        }
        .result_box{
            font-size: 21px;
            font-weight: bold;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
            margin-top: 20px;
        }
        .footer{
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Unit Converter using python and streamlit</h1>", unsafe_allow_html=True)
st.write("Helpful for converting units from one to another")

conversion_type = st.selectbox("Select the conversion type", ["Length", "Weight", "Temperature", "Time"])
value = st.number_input("Enter the value to convert", min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["mm", "cm", "m", "km", "Yd", "Mi"])
    with col2:
        to_unit = st.selectbox("To", ["mm", "cm", "m", "km", "Yd", "Mi"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["mg", "g", "kg"])
    with col2:
        to_unit = st.selectbox("To", ["mg", "g", "kg"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["°C", "°F", "°K"])
    with col2:
        to_unit = st.selectbox("To", ["°C", "°F", "°K"])
elif conversion_type == "Time":
    with col1:
        from_unit = st.selectbox("From", ["ms", "s", "min", "hr"])
    with col2:
        to_unit = st.selectbox("To", ["ms", "s", "min", "hr"])

def length_converter(value, from_unit, to_unit):
    length_units = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 0.001,
        "Yd": 1.09361,
        "Mi": 0.000621371
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "mg": 1000000,
        "g": 1000,
        "kg": 1,
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "°C":
        if to_unit == "°F":
            return (value * 9/5) + 32
        elif to_unit == "°K":
            return value + 273.15
    elif from_unit == "°F":
        if to_unit == "°C":
            return (value - 32) * 5/9
        elif to_unit == "°K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "°K":  
        if to_unit == "°C":
            return value - 273.15
        elif to_unit == "°F":
            return (value - 273.15) * 9/5 + 32
    return value

def time_converter(value, from_unit, to_unit):
    time_units = {
        "ms": 1000,
        "s": 1,
        "min": 1/60,
        "hr": 1/3600
    }
    return value * time_units[from_unit] / time_units[to_unit]

if st.button("⏳Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif conversion_type == "Time":
        result = time_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result_box'>{value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
       Created by Dua Sharif    
    </div>
    """,
    unsafe_allow_html=True
)










    

