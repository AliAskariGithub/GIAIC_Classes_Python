import streamlit as st
st.title("💪Unit Convertor")
st.markdown("#### Convert Length, Weight and Temperature")
st.write("Select the type of conversion, enter the value and click on the convert button")

category = st.selectbox("Select a Category: ", ["Length", "Weight", "Temperature", "Time", "Volume", "Area", "Speed", "Pressure", "Energy", "Power", "Data"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometer to miles":
            return value * 0.621371
        elif unit == "kilometer to meter":
            return value * 1000
        elif unit == "meter to kilometer":
            return value / 1000
        elif unit == "meter to miles":
            return value * 0.000621371
        elif unit == "miles to kilometer":
            return value * 1.60934
        elif unit == "miles to meter":
            return value / 0.000621371
        
    elif category == "Weight":
        if unit == "kilogram to pounds":
            return value * 2.20462
        elif unit == "kilogram to grams":
            return value * 1000
        elif unit == "pounds to kilogram":
            return value / 2.20462
        elif unit == "pounds to grams":
            return value * 453.592
        elif unit == "grams to kilogram":
            return value / 1000
        elif unit == "grams to pounds":
            return value / 453.592
        
    elif category == "Temperature":
        if unit == "celsius to fahrenheit":
            return (value * 9/5) + 32
        elif unit == "celcius to kelvin":
            return value + 273.15
        elif unit == "fahrenheit to celsius":
            return (value - 32) * 5/9
        elif unit == "fahrenhiet to kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit == "kelvin to celsius":
            return value - 273.15
        elif unit == "kelvin to fahrenheit":
            return (value - 273.15) * 9/5 + 32
        
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "seconds to hours":
            return value / 3600
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to seconds":
            return value * 3600
        elif unit == "hours to minutes":
            return value * 60
        
    elif category == "Volume":
        if unit == "liters to milliliters":
            return value * 1000
        elif unit == "liters to gallons":
            return value * 0.264172
        elif unit == "milliliters to liters":
            return value / 1000
        elif unit == "milliliters to gallons":
            return value * 0.000264172
        elif unit == "gallons to liters":
            return value / 0.264172
        elif unit == "gallons to milliliters":
            return value / 0.000264172
        
    elif category == "Area":
        if unit == "sq. meters to sq. feet":
            return value * 10.7639
        elif unit == "sq. meters to sq. yards":
            return value * 1.19599
        elif unit == "sq. feet to sq. meters":
            return value / 10.7639
        elif unit == "sq. feet to sq. yards":
            return value / 9
        elif unit == "sq. yards to sq. meters":
            return value / 1.19599
        elif unit == "sq. yards to sq. feet":
            return value * 9
        
    elif category == "Speed":
        if unit == "km/hr to m/s":
            return value / 3.6
        elif unit == "km/hr to miles/hr":
            return value / 1.60934
        elif unit == "m/s to km/hr":
            return value * 3.6
        elif unit == "m/s to miles/hr":
            return value * 2.23694
        elif unit == "miles/hr to km/hr":
            return value * 1.60934
        elif unit == "miles/hr to m/s":
            return value / 2.23694
        
    elif category == "Pressure":
        if unit == "pascal to atm":
            return value / 101325
        elif unit == "pascal to psi":
            return value / 6895
        elif unit == "atm to pascal":
            return value * 101325
        elif unit == "atm to psi":
            return value * 14.6959
        elif unit == "psi to pascal":
            return value * 6895
        elif unit == "psi to atm":
            return value / 14.6959
        elif unit == "torr to atm":
            return value / 760
        elif unit == "torr to pascal":
            return value * 133.322
        elif unit == "atm to torr":
            return value * 760
        elif unit == "pascal to torr":
            return value / 133.322
        elif unit == "psi to torr":
            return value * 51.715
        elif unit == "torr to psi":
            return value / 51.715
        
    elif category == "Energy":
        if unit == "joules to calories":
            return value / 4.184
        elif unit == "joules to watt-hours":
            return value / 3600
        elif unit == "calories to joules":
            return value * 4.184
        elif unit == "calories to watt-hours":
            return value / 860 
        elif unit == "watt-hours to joules":
            return value * 3600
        elif unit == "watt-hours to calories":
            return value * 860
        elif unit == "joules to kilojoules":
            return value / 1000
        elif unit == "calories to kilocalories":
            return value / 1000
        elif unit == "watt-hours to kilowatt-hours":
            return value / 1000
        elif unit == "kilojoules to joules":
            return value * 1000
        elif unit == "kilocalories to calories":
            return value * 1000
        elif unit == "kilowatt-hours to watt-hours":
            return value * 1000
        
    elif category == "Power":
        if unit == "watt to hp":
            return value / 745.7
        elif unit == "watt to kilowatt":
            return value / 1000
        elif unit == "hp to watt":
            return value * 745.7
        elif unit == "hp to kilowatt":
            return value / 1.341
        elif unit == "kilowatt to watt":
            return value * 1000
        elif unit == "kilowatt to hp":
            return value * 1.341
        elif unit == "watt to btu/hr":
            return value * 3.412
        elif unit == "hp to btu/hr":
            return value * 2545
        elif unit == "kilowatt to btu/hr":
            return value * 3412.14
        elif unit == "btu/hr to watt":
            return value / 3.412
        elif unit == "btu/hr to hp":
            return value / 2545
        
    elif category == "Data":
        if unit == "bytes to kilobytes":
            return value / 1024
        elif unit == "bytes to megabytes":
            return value / 1048576
        elif unit == "kilobytes to bytes":
            return value * 1024
        elif unit == "kilobytes to megabytes":
            return value / 1024
        elif unit == "megabytes to bytes":
            return value * 1048576
        elif unit == "megabytes to kilobytes":
            return value * 1024
        elif unit == "kilobytes to gigabytes":
            return value / 1024
        
if category == "Length":
    unit = st.selectbox("📏Select Conversation: ", ["kilometer to miles", "kilometer to meter", "meter to kilometer", "meter to miles", "miles to kilometer", "miles to meter"])
elif category == "Weight":
    unit = st.selectbox("⚖️Select Conversation: ", ["kilogram to pounds", "kilogram to grams", "pounds to kilogram", "pounds to grams", "grams to kilogram", "grams to pounds"])
elif category == "Temperature":
    unit = st.selectbox("🌡️Select Conversation: ", ["celsius to fahrenheit", "celsius to kelvin", "fahrenheit to celsius", "fahrenheit to kelvin", "kelvin to celsius", "kelvin to fahrenheit"])
elif category == "Time":
    unit = st.selectbox("⏰Select Conversation: ", ["seconds to minutes", "seconds to hours", "minutes to seconds", "minutes to hours", "hours to seconds", "hours to minutes"])
elif category == "Volume":
    unit = st.selectbox("🥛Select Conversation: ", ["liters to milliliters", "liters to gallons", "milliliters to liters", "milliliters to gallons", "gallons to liters", "gallons to milliliters"])
elif category == "Area":
    unit = st.selectbox("📐Select Conversation: ", ["sq. meters to sq. feet", "sq. meters to sq. yards", "sq. feet to sq. meters", "sq. feet to sq. yards", "sq. yards to sq. meters", "sq. yards to sq. feet"])
elif category == "Speed":
    unit = st.selectbox("🚗Select Conversation: ", ["km/hr to m/s", "km/hr to miles/hr", "m/s to km/hr", "m/s to miles/hr", "miles/hr to km/hr", "miles/hr to m/s"])
elif category == "Pressure":
    unit = st.selectbox("🌡️Select Conversation: ", ["pascal to atm", "pascal to psi", "atm to pascal", "atm to psi", "psi to pascal", "psi to atm", "torr to atm", "torr to pascal", "atm to torr", "pascal to torr", "psi to torr", "torr to psi"])
elif category == "Energy":
    unit = st.selectbox("🔋Select Conversation: ", ["joules to calories", "joules to watt-hours", "calories to joules", "calories to watt-hours", "watt-hours to joules", "watt-hours to calories", "joules to kilojoules", "calories to kilocalories", "watt-hours to kilowatt-hours", "kilojoules to joules", "kilocalories to calories", "kilowatt-hours to watt-hours"])
elif category == "Power":
    unit = st.selectbox("⚡Select Conversation: ", ["watt to hp", "watt to kilowatt", "hp to watt", "hp to kilowatt", "kilowatt to watt", "kilowatt to hp", "watt to btu/hr", "hp to btu/hr", "kilowatt to btu/hr", "btu/hr to watt", "btu/hr to hp"])
elif category == "Data":
    unit = st.selectbox("💾Select Conversation: ", ["bytes to kilobytes", "bytes to megabytes", "kilobytes to bytes", "kilobytes to megabytes", "megabytes to bytes", "megabytes to kilobytes", "kilobytes to gigabytes"])
    
value = st.number_input("Enter the value to convert: ")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
    
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        color: #888;
        padding: 10px;
        text-color: #f1f1f1;
    }
    
    .pre {
        font-family: monospace;
        position: fixed;
        bottom: 0;
        right: 0;
        width: auto;
        text-align: center;
        color: #888;
        padding: 10px;
        background-color: #ffffff;
        z-index: 0;
        border: none;
        border-left: 1px solid #f1f1f1;
        border-top-left-radius: 10px;
    }
    
    .pre a {
        color: #000;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    
    <div class="footer">
        © 2025 Convertor | All rights reserved.
    </div>
    
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .pre {
        font-family: monospace;
        position: fixed;
        bottom: 0;
        left: 0;
        width: auto;
        text-align: center;
        color: #888;
        padding: 10px;
        background-color: #ffffff;
        z-index: 0;
        border: none;
        border-right: 1px solid #f1f1f1;
        border-top-right-radius: 10px;
    }
    
    .pre a {
        color: #000;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)
