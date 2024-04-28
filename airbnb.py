import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os 
from matplotlib import pyplot as plt


df=pd.read_csv("C:/Users/catch/Downloads/C__Users_catch_OneDrive_Desktop_project_din (3).csv")
din=pd.DataFrame(df)

st.set_page_config(
                    page_title="Airbnb Analysis",
                    page_icon="https://static-00.iconduck.com/assets.00/airbnb-icon-512x512-d9grja5t.png",
                    layout="wide",
                    initial_sidebar_state="collapsed"
                    )
row1 = st.columns(2)
with row1[0]:
    sub_columns = st.columns(3)

    with sub_columns[0]:
        menu = option_menu("Menu", ["Home","Analysis", "About"], 
                            icons=["house", "graph-up", "exclamation-triangle"],
                            menu_icon="cast",
                            default_index=0,
                            styles={"icon": {"color": "orange", "font-size": "20px"}}
                            )

   
if menu == "Home":
    
    st.title(":red[**WELCOME TO AIRBNB ANALYSIS:**]")
    
    st.write("## :red[Explore Insights from Airbnb Data:]")

    st.write("Welcome to our Airbnb Analysis Dashboard! This interactive tool offers a comprehensive analysis of Airbnb listings, bookings, and trends, providing valuable insights for both hosts and travelers.")

    st.write("## :red[What You Can Do:]")
    
    st.markdown("""
                <ul>
                <li style='color:red; font-size:20px; background-color: lightgrey;'> Discover Trends: Explore the latest trends in Airbnb listings, pricing, and availability.</li>
                <li style='color:red; font-size:20px; background-color: lightgrey;'>Analyze Locations: Dive into the geographical distribution of Airbnb listings and discover popular neighborhoods.</li>
                <li style='color:red; font-size:20px; background-color: lightgrey;'>Understand Guest Experience: Gain insights into guest satisfaction, reviews, and ratings.</li>
                <li style='color:red; font-size:20px; background-color: lightgrey;'>Optimize Hosting: Learn how to optimize your Airbnb listings and enhance the guest experience.</li>
                <ul>""",unsafe_allow_html=True)

    st.write("## :red[Get Started:]")
    
    st.write("Click on the tabs above to start exploring the various analyses offered by our Airbnb Analysis Dashboard. Have questions or feedback? Feel free to reach out to us using the contact information provided.")
    
    
    
if menu=="Analysis":
    st.markdown(f""" <style>.stApp {{
                background: url('https://jayvas.com/wp-content/uploads/2020/11/airbnb-real-estate-company-1110x624.jpg');   
                background-size: cover}}
                </style>""",unsafe_allow_html=True)
    
    
    analysis = st.selectbox("Exploratory Analysis of Airbnb Listing Data", ["Countries available data",
                                                                        "Price analysis by room type",
                                                                        "Max & Min of reviews and prices",
                                                                        "Average price by Room and Property type",
                                                                        "lookout for reviews",
                                                                        "Average price for selected countries",
                                                                        "Average price for selected features",
                                                                        "Price comparision between availabilities"
                                                                        ])
    
    
    
    
    
    if analysis=="Countries available data":
       col1,col2=st.columns(2) 
       with col1:
           
        fig=px.bar(din.groupby('address')["price"].count().sort_values(ascending=False).reset_index(),
        x="address",
        y="price",
        color="address",
        title="Number of house by type",
        labels={"address":"Address","price":"Number of house"},
        template="plotly_dark")
        st.plotly_chart(fig)
       with col2:
        fig=px.pie(din.groupby("address")["price"].count().reset_index(),values="price",names="address",hole=0.3,title="Number of house by percentages",labels={"address":"Address","price":"Number of house"},template="plotly_dark")
        st.plotly_chart(fig)
        
        
    if analysis=="Price analysis by room type":
        
        sub_columns = st.columns(2)

        with sub_columns[0]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[0]:
                        xaxis = st.selectbox("", ['Room_type',
                                                  'Property_type',
                                                  
                                                  
                                                ])
        if xaxis=="Room_type":
            with sub_columns[0]:
                
                fig=px.bar(din,x="address",y="price",color="room_type",barmode="group",title="Price of house by type",height=600,width=800,template="plotly_dark",hover_data=["price"],labels={"address":"Address","price":"Price","room_type":"Room Type"})
                st.plotly_chart(fig)
            
        if xaxis=="Property_type":
            with sub_columns[0]:
                fig=px.bar(din,x="address",y="price",color="property_type",barmode="group",title="Price of house by type",height=1000,width=1000,template="plotly_dark",hover_data=["price"],labels={"address":"Address","price":"Price","room_type":"Room Type"})
                st.plotly_chart(fig)
                
                
    if analysis=="Max & Min of reviews and prices":
        sub_columns=st.columns(2)
        with sub_columns[1]:
            sub_columns_1=st.columns(2)
            with sub_columns_1[1]:
                yaxis=st.selectbox("",din["address"].unique())
                
        with sub_columns[0]:
            
            def country(cou):
                df = din[(din.review_rating >= 60) & (din.price.between(10, 4500)) & (din.address == cou)]
                ind = df.groupby(["review_rating", "address"])[["price", "review_rating"]].min()
                fig = px.line(ind, x="review_rating", y="price", title= f"{cou}'s Minimum price for 60+ star reviews")
                st.plotly_chart(fig)
                # df1 = din[(din.review_rating >= 60) & (din.price.
                ind1 = df.groupby(["review_rating", "address"])[["price", "review_rating"]].max()
                fig=px.line(ind1, x="review_rating", y="price", title=f"{cou}'s Maximum price for 60+ star reviews")
                st.plotly_chart(fig)
                
            country(yaxis)
                
     
    if analysis=="Average price by Room and Property type":
       
                
           
        sub_columns = st.columns(2)

        with sub_columns[0]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[0]:
                        yaxis=st.selectbox("",['Property_type',"Room_type"])
                
        
            
        if yaxis=="Property_type":
            with sub_columns[0]:
                fig=px.scatter(x=din["property_type"], y=din["price"], color=din["room_type"], title="Price vs Property Type", labels={"x":"Property Type", "y":"Price", "color":"Room Type"},template="plotly_dark", width=1000, height=800, color_discrete_sequence=px.colors.qualitative.Prism, color_continuous_scale=px.colors.sequential.Turbo)
                st.plotly_chart(fig)
                
        if yaxis=="Room_type":
            with sub_columns[0]:
                fig = px.scatter(x=din["room_type"], y=din["price"], color=din["room_type"], title="Price vs Room Type", width=1000, height=500, template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Light24, color_continuous_scale=px.colors.sequential.Blues, labels={"room_type":"Room Type", "price":"Price"})
                st.plotly_chart(fig)
            
            
    if analysis=="lookout for reviews":
        
        grouped_df = din.groupby(["address"])[["review_rating","price"]].mean().reset_index().sort_values(by="review_rating", ascending=False)
        fig=px.bar(grouped_df, x="address", y="review_rating", color="address", title="Number of reviews per country")
        st.plotly_chart(fig)
        fig=px.pie(grouped_df,values="review_rating",names="address",title="Average Rating of Restaurants in Each Location",hole=0.3)
        st.plotly_chart(fig)
        
    if analysis=="Average price for selected countries":
        fig=px.bar(din.groupby("address")["price"].mean().reset_index(), x="address", y="price", color="address", title="Average price by address", color_discrete_sequence=px.colors.qualitative.Bold,template="plotly_dark")
        st.plotly_chart(fig) 
        fig=px.pie(din.groupby("address")["price"].mean(), values="price", names=din.groupby("address")["price"].mean().index, title="Mean price per address", color_discrete_sequence=px.colors.sequential.RdBu, template="plotly_dark")
        st.plotly_chart(fig) 
        
    if analysis=="Average price for selected features":
    
        
            fig = fig = px.bar(din.groupby(["property_type", "room_type"])[["price"]].mean().reset_index(), x="property_type", y="price", color="room_type", color_discrete_sequence=px.colors.qualitative.Bold, title="Average Price by Property Type and Room Type", labels={"property_type": "Property Type", "price": "Price", "room_type": "Room Type"},template="plotly_dark")
            st.plotly_chart(fig)
        
        
    if analysis =="Price comparision between availabilities":
        sub_columns = st.columns(2)

        with sub_columns[0]:
                    sub_columns_1 = st.columns(2)

                    with sub_columns_1[1]:
                        yaxis=st.selectbox("",['Availability_30',"Availability_60","Availability_90","Availability_365"])
        
        if yaxis=="Availability_30":
            with sub_columns[0]:
            
                fig, ax = plt.subplots(figsize=(15, 6))
                ax.scatter(din['price'], din['availability_30'], s=32, alpha=0.8)
                ax.set_xlabel('Price')
                ax.set_ylabel('Availability (Last 30 days)')
                ax.set_title('Price vs Availability (Last 30 days)')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
                
        if yaxis=="Availability_60":
            with sub_columns[0]:
            
                fig, ax = plt.subplots(figsize=(15, 6))
                ax.scatter(din['price'], din['availability_60'], s=32, alpha=0.8)
                ax.set_xlabel('Price')
                ax.set_ylabel('Availability (Last 60 days)')
                ax.set_title('Price vs Availability (Last 60 days)')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
                
        if yaxis=="Availability_90":
            with sub_columns[0]:
            
                fig, ax = plt.subplots(figsize=(15, 6))
                ax.scatter(din['price'], din['availability_90'], s=32, alpha=0.8)
                ax.set_xlabel('Price')
                ax.set_ylabel('Availability (Last 90 days)')
                ax.set_title('Price vs Availability (Last 90 days)')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
                
        if yaxis=="Availability_365":
            with sub_columns[0]:
            
                fig, ax = plt.subplots(figsize=(15, 6))
                ax.scatter(din['price'], din['availability_365'], s=32, alpha=0.8)
                ax.set_xlabel('Price')
                ax.set_ylabel('Availability (Last 365 days)')
                ax.set_title('Price vs Availability (Last 365 days)')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
                
                
if menu=="About":
    
    with row1[1]:
        
        st.write("## :red[About]")
        
        
        st.write("Welcome to our Airbnb Analysis App! This interactive tool is designed to provide insights and visualizations derived from an in-depth analysis of Airbnb data. Below, we'll provide you with an overview of what you can expect from this app.")
        
        st.subheader(":red[Insights Offered:]")
        
        st.markdown("***:green[Price Analysis:]*** Explore the distribution of listing prices, identify factors influencing pricing, and discover how prices vary across different locations and property types.")
        st.markdown("***:green[Location Analysis:]*** Visualize the geographical distribution of Airbnb listings, discover popular neighborhoods, and analyze average prices by location.")
                
        st.markdown("***:green[Guest Experience:]*** Dive into guest reviews and ratings, understand what factors contribute to guest satisfaction, and uncover trends in booking behavior.")
        st.markdown("***:green[Host Insights:]*** Gain insights into host characteristics, including the distribution of hosts by number of listings, host responsiveness, and superhost status.")
                                    
        st.subheader(":red[How to Use:]")    
        
        st.markdown("""
                    <ul>
                    <li font-size:20px; background-color: lightgrey;'> Navigate through the different tabs and interactive widgets to explore the various analyses offered by the app.</li>
                    <li font-size:20px; background-color: lightgrey;'> Use the filters and dropdowns to customize your analysis based on your preferences. Feel free to interact with the visualizations and explore the insights provided.</li>
                    <ul>""",unsafe_allow_html=True)
        
        st.subheader(":red[Contact us:]") 
        
        st.markdown('''If you have any questions, feedback, or suggestions for improvement, please don't hesitate to reach out to us at :orange[9876543210].  We value your input and are continuously striving to enhance the functionality and usability of this app.''')                       