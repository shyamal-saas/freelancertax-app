import os
os.system("C:\\Users\\shyam\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe -m pip install fpdf2")

from fpdf import FPDF


def calculate_tax(country,annual_income):

    if country == "US":
       
        if annual_income <= 50000:
            print("Tax Rate: 10%. Low income bracket.")
            tax_due = annual_income * 0.10
        elif annual_income <= 100000:
            print("Tax Rate: 20%. Medium income bracket.")
            tax_due = annual_income * 0.20
        else:
            print("Tax Rate: 35%. High income bracket.")
            tax_due = annual_income * 0.35
    elif country == "UK":
       
        if annual_income <= 12570:
            print("Tax Rate: 0%. Personal Allowance.")
            tax_due = 0
        elif annual_income <= 50270:
            print("Tax Rate: 20%. Basic Rate.")
            tax_due = annual_income * 0.20
        else:
            print("Tax Rate: 40%. Higher Rate.")
            tax_due = annual_income * 0.40
    elif country == "IND":
        
        if annual_income <= 300000:
            print("Tax Rate: 0%. No tax to pay.")
            tax_due = 0
        elif annual_income <= 700000:
            print("Tax Rate: 5%. New Tax Regime.")
            tax_due = annual_income * 0.05
        else:
            print("Tax Rate: 10% or above. Progressive rates apply.")
            tax_due = annual_income * 0.10
    elif country == "AUS":
        
        if annual_income <= 18200:
            print("Tax Rate: 0%. Tax-free threshold.")
            tax_due = 0
        elif annual_income <= 45000:
            print("Tax Rate: 16%. Low income bracket.")
            tax_due = annual_income * 0.16
        else:
            print("Tax Rate: 30% or above. Medium to high bracket.")
            tax_due = annual_income * 0.30
    elif country =="UAE":
       
        if annual_income <= 375000:
            print("Tax Rate: 0%. No Corporate Tax for individuals below threshold.")
            tax_due = 0
        else:
            print("Tax Rate: 9%. Corporate Tax applies above 375,000 AED.")
            tax_due = annual_income * 0.09
    else:
        print("Sorry, this country is not supported yet!")
    return tax_due
import streamlit as st
import streamlit_authenticator as stauth
if 'app_started' not in st.session_state:
    st.session_state.app_started = False
if not st.session_state.app_started:
    st.markdown(
        """
        <div style='text-align: center; padding: 10px;'>
            <h1 style='font-family: "Helvetica Neue", sans-serif; font-size: 50px; font-weight: 800; background: linear-gradient(45deg, #FF4B4B, #FF8533); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0;'>
                ⚡ FREELANCERTAX
            </h1>
            <p style='font-family: "Helvetica Neue", sans-serif; font-size: 16px; font-weight: 500; color: #A0AEC0; letter-spacing: 2px; margin-top: 5px; text-transform: uppercase;'>
                The Global Freelancer Tax Engine
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("---")

    st.markdown(
        """
        <style>
        div.stButton {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        div.stButton > button:first-child {
            background: linear-gradient(45deg, #FF8533, #FF4B4B);
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 25px;
            border: none;
            padding: 12px 40px;
            width: auto;
            box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
            transition: 0.3s;
        }
        div.stButton > button:first-child:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 20px rgba(255, 133, 51, 0.6);
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    if st.button("ENTER FREELANCERTAX 🚀", use_container_width=True):
        st.session_state.app_started = True
        st.rerun()
    st.stop()


credentials = {
    "usernames": {
        "shyam": {
            "name": "Shyam",
            "password": "123"
        }
    }
}


authenticator = stauth.Authenticate(
    credentials,
    cookie_name="freelancertax_cookie",
    key="abcdef",
    cookie_expiry_days=30
)
import streamlit_authenticator as stauth


credentials = {
    "usernames": {
        "shyam": {
            "name": "Shyam",
            "password": "123"
        }
    }
}





if 'app_started' not in st.session_state:
     st.session_state.app_started = False
if not st.session_state.app_started:
    st.markdown(
        """
        <div style='text-align: center; padding: 10px;'>
            <h1 style='font-family: "Helvetica Neue", sans-serif; font-size: 50px; font-weight: 800; background: linear-gradient(45deg, #FF4B4B, #FF8533); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0;'>
                ⚡ FREELANCERTAX
            </h1>
            <p style='font-family: "Helvetica Neue", sans-serif; font-size: 16px; font-weight: 500; color: #A0AEC0; letter-spacing: 2px; margin-top: 5px; text-transform: uppercase;'>
                The Global Freelancer Tax Engine
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("---")
        
    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background: linear-gradient(45deg, #FF8533, #FF4B4B);
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 10px;
            border: none;
            padding: 12px;
            transition: 0.3s;
        }
        div.stButton > button:first-child:hover {
            transform: scale(1.02);
            background: linear-gradient(45deg, #FF4B4B, #FF8533);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

      
authenticator.login()


if st.session_state.get("authentication_status") == True:
    st.write(f'Welcome *{st.session_state["name"]}*')
    
    if "invoice_count" not in st.session_state:
        st.session_state.invoice_count = 0
    if "is_paid" not in st.session_state:
        st.session_state.is_paid = False
    if not st.session_state.is_paid:
        remaining = 3 - st.session_state.invoice_count
        st.success(f"🎁 **Free Trial Active:** You have **{remaining} out of 3** free calculations remaining.")
        st.progress(st.session_state.invoice_count / 3)
   

    if st.session_state.invoice_count >= 3 and not st.session_state.is_paid:
        st.error("⚠️ Your Free Trial Has Expired!")
        st.markdown(
            """
            <div style='background-color: #ffcccc; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #ff4b4b;'>
                <h3 style='color: #cc0000; margin-top: 0;'>🔒 Access Locked</h3>
                <p style='color: #333; font-size: 16px;'>You have reached your limit of 5 free tax calculations. To continue using FreelancerTax with unlimited access, please upgrade to the Premium Plan.</p>
                <h2 style='color: #111;'>Price: $10 /Monthly </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    
        
        if st.button("🔔 UPGRADE TO PREMIUM ($10/mo)", use_container_width=True):
            st.session_state.is_paid = True
            st.success("Payment Successful! Access Granted.")
            st.rerun()
            
        st.stop()
        if not st.session_state.is_paid:
            remaining = 5 - st.session_state.invoice_count
            st.success(f"🎁 **Free Trial Active:** You have **{remaining} out of 5** free calculations remaining.")
            st.progress(st.session_state.invoice_count / 5)

    

    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
    st.stop()
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
    st.stop()  
 


country_input = st.selectbox("Select your country:", ["US", "UK", "IND", "AUS", "UAE"])
income_input = st.number_input("Enter your annual income ($):", min_value=0.0, value=50000.0)
final_tax = calculate_tax(country_input, income_input)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=16)
pdf.set_font("Helvetica", "B", 24)
pdf.cell(200, 10, text="FREELANCERTAX  |  Tax Engine ", ln=True, align='C')
pdf.set_font("Helvetica", size=16)
pdf.cell(200, 10, text="OFFICIAL FREELANCER TAX INVOICE", ln=True, align='C')
pdf.cell(200, 10, text=f"Country: {country_input}", ln=True)
pdf.cell(200, 10, text=f"Annual Income: ${income_input}", ln=True)
pdf.cell(200,10, text=f"Calculated Tax Due: ${final_tax}", ln=True)
net_income = income_input - final_tax
pdf.cell(200, 10, text=f"Net Income (Take-Home Pay): ${net_income}", ln=True)
st.download_button(label="Download PDF Invoice", data=bytes(pdf.output()), file_name="tax_invoice.pdf", mime="application/pdf")
st.markdown("---")
st.caption("ℹ️ :red[**Disclaimer: This app provides estimated tax calculations for informational purposes only. Please consult a certified tax professional or accountant in your country for official tax filings and legal compliance.**]")
st.session_state.invoice_count += 1
st.markdown(
        """
        <style>
        div.stDownloadButton {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 20px;
        }
        div.stDownloadButton > button {
            background: linear-gradient(45deg, #FF8533, #FF4B4B) !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
            border-radius: 10px !important;
            border: none !important;
            padding: 10px 25px !important;
            box-shadow: 0px 4px 12px rgba(255, 75, 75, 0.3) !important;
            transition: 0.3s !important;
        }
        div.stDownloadButton > button:hover {
            transform: scale(1.03) !important;
            box-shadow: 0px 6px 18px rgba(255, 133, 51, 0.5) !important;
        }
                form div.stButton > button {
            background: linear-gradient(45deg, #FF8533, #FF4B4B) !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
            border-radius: 10px !important;
            border: none !important;
            padding: 10px 25px !important;
            width: 100% !important;
            box-shadow: 0px 4px 12px rgba(255, 75, 75, 0.3) !important;
            transition: 0.3s !important;
        }
        form div.stButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0px 6px 18px rgba(255, 133, 51, 0.5) !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown(
        """
        <style>
        form[data-testid="stForm"] button[type="submit"], 
        .stLoginForm button[type="submit"],
        button[type="submit"] {
            background: linear-gradient(45deg, #FF8533, #FF4B4B) !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
            border-radius: 10px !important;
            border: none !important;
            padding: 10px 25px !important;
            width: 100% !important;
            box-shadow: 0px 4px 12px rgba(255, 75, 75, 0.3) !important;
            transition: 0.3s !important;
        }
        form[data-testid="stForm"] button[type="submit"]:hover,
        .stLoginForm button[type="submit"]:hover,
        button[type="submit"]:hover {
            transform: scale(1.02) !important;
            box-shadow: 0px 6px 18px rgba(255, 133, 51, 0.5) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

