from Datacoll_dataclean import a
from eda_analysis import p,p1,p2,p3,p4,p5,p6,p7,p8 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def streamlit():
    tab1, tab2, tab3, tab4,tab5= st.tabs(["Home", "Geo visualization", " Website","EDA Insights","Data visualization"])

    with tab1:
        st.markdown('<h1 style="text-align: center; color: red;">Airbnb</h1>', unsafe_allow_html=True)
        option = st.selectbox("Which destination you are looking for?",['','United States', 'Turkey', 'Hong Kong', 'Australia', 'Portugal','Brazil', 'Canada', 'Spain', 'China'])
        if option:
            option1 = st.selectbox("No of Adults(Age13 or above)",['','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
            option2 = st.selectbox("No of Adults(Age13 or above)",['','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])

    with tab2:
        trace = go.Scattergeo(
            lat=list(a["longitude"]),
            lon=list(a["latitude"]),
            mode='markers', 
            marker=dict(
                size=10,
                color='red', 
                opacity=0.8,
            ),
        )

        # Define layout options
        layout = go.Layout(
            geo=dict(
                projection_type='natural earth', 
            ),
        )

        # Create the figure
        fig = go.Figure(data=[trace], layout=layout)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        df = a[a["country"] == option]
        acc = int(option1) + int(option2)
        df = df[df["accomdates"] >= acc]
        for i in range(len(df)):
            col1, col2 = st.columns(2)
            with col1:
                st.image(df.iloc[i]["image"])
            with col2:
                st.header(df.iloc[i]["name"])
                st.write(f"hosted by {df.iloc[i]["host_name"]}")
                st.write("Price")
                st.write(f"{df.iloc[i]["price"]}+taxes")
                if st.button(f"Book{i}"):
                    with st.expander("Things to know"):
                        st.write(f"Security Deposit: {df.iloc[i]["sec_dep"]}")
                        st.write(f"Guest included: {df.iloc[i]["guest"]}")
                        col3, col4, col5 = st.columns(3)
                        with col3:
                            st.write(":red[Prop Type]")
                            st.write(f"{df.iloc[i]["prop_type"]}")
                            st.write(":red[Accomdates]")
                            st.write(f"{df.iloc[i]["accomdates"]}")
                        with col4:
                            st.write(":red[Room Type]")
                            st.write(f"{df.iloc[i]["room"]}")
                            st.write(":red[No. Beds]")
                            st.write(f"{df.iloc[i]["no_of_bedrooms"]}")
                        with col5:
                            st.write(":red[Bed Type]")
                            st.write(f"{df.iloc[i]["bed"]}")
                            st.write(":red[Bathroom]")
                            st.write(f"{df.iloc[i]["no_bathroom"]}")
                        
                        st.write(f":red[Amenities]: {df.iloc[i]["amenities"]}")
                        st.write(f":red[Rules]: {df.iloc[i]["rules"]}")
                        st.write(f":red[Cancellation Policy]: {df.iloc[i]["cancel_pol"]}")
                        
                        rev = df.iloc[i]["tot_review"]
                        if rev > 0:
                            st.write(f":red[Number of reviews]: {rev}")
                            col6, col7, col8, col9, col10, col11 = st.columns(6)
                            with col6:
                               st.write(":dart:")
                               st.write(f"{df.iloc[i]["rev_acc"]}")
                            with col7:
                                st.write(":broom:️")
                                st.write(f"{df.iloc[i]["rev_clean"]}")
                            with col8:
                                st.write(":hotel:")
                                st.write(f"{df.iloc[i]["rev_checkin"]}")
                            with col9:
                                st.write(":microphone:")
                                st.write(f"{df.iloc[i]["rev_comm"]}")
                            with col10:
                                st.write(":pushpin:")
                                st.write(f"{df.iloc[i]["rev_loc"]}")
                            with col11:
                                st.write(":100:")
                                st.write(f"{df.iloc[i]["rev_val"]}")
                            st.write(f":red[Overall Review]: {df.iloc[i]["overall_rev"]}")
                        else:
                            st.write("NO Review(0)")

                        st.write(f":red[Address]: {df.iloc[i]["address"]}")

    with tab4:
        #Analysis1
        st.header(":red[Analysis of Room over Price]")
        if p < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between types of room and their prices. It is a strong evidence.           
            """.format(p))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between types of room and their prices. It is a strong evidence.           
            """.format(p))

        #Analysis2
        st.header(":red[Analysis for property and price]")
        if p1 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between types of property and their prices. It is a strong evidence.           
            """.format(p1))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between types of property and their prices. It is a strong evidence.           
            """.format(p1))
        
        #Analysis3
        st.header(":red[Analysis for bed and price]")
        if p2 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between types of bed and their prices. It is a strong evidence.           
            """.format(p2))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between types of bed and their prices. It is a strong evidence.           
            """.format(p2))

        #Analysis4
        st.header(":red[Analysis for country Over price]")
        if p3 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between different countries and their prices. It is a strong evidence.           
            """.format(p3))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between different countries and their prices. It is a strong evidence.           
            """.format(p3))

        #Analysis5
        st.header(":red[Analysis for price over room and country]")
        if p4 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between over countries, room type and their prices. It is a strong evidence.           
            """.format(p4))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between over countries, room type and their prices. It is a strong evidence.           
            """.format(p4))
        
        #Analysis6
        st.header(":red[Analysis for rules over price]")
        if p5 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between different rules and their prices. It is a strong evidence.           
            """.format(p5))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between different rules and their prices. It is a strong evidence.           
            """.format(p5))

        #Analysis7
        st.header(":red[Analysis for cancellation policy over price]")
        if p6 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between different cancellation policy and their prices. It is a strong evidence.           
            """.format(p6))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between different cancellation policy and their prices. It is a strong evidence.           
            """.format(p6))

        #Analysis8
        st.header(":red[Analysis for bedrooms over price]")
        if p7 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between different bedrooms and their prices. It is a strong evidence.           
            """.format(p7))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between different bedrooms and their prices. It is a strong evidence.           
            """.format(p7))

        #Analysis9
        st.header(":red[Analysis of bathroom over price]")
        if p8 < 0.05:
            st.markdown("""
            - P-Value- {0}
            - Reject H0
            - Dependent
            - From this we can conclude that there is a significant connection between different bathroom and their prices. It is a strong evidence.           
            """.format(p8))
        else:
            st.markdown("""
            - P-Value- {0}
            - Fail to Reject H0
            - Independent
            - From this we can conclude that there is no connection between different bathroom and their prices. It is a strong evidence.           
            """.format(p8))

    with tab5:
        st.subheader("Exploring Trends Across Countries over property, room and price")
        fig = px.sunburst(a, path=["country","prop_type","room"], values='price')
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Exploring Trends Across Countries over property")
        df = a.groupby(["country"])[["prop_type"]].count().reset_index()
        df = df.sort_values(by="prop_type")
        fig = px.bar(df,x="country",y="prop_type")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Exploring Trends Across Countries over room")
        df = a.groupby(["country"])[["room"]].count().reset_index()
        df = df.sort_values(by="room")
        fig = px.scatter(df, x='country', y='room')
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Exploring Trends Across Countries over room and property")
        option3 = st.selectbox("Please select the country",['','United States', 'Turkey', 'Hong Kong', 'Australia', 'Portugal','Brazil', 'Canada', 'Spain', 'China'])
        df = a.groupby(["country","prop_type"])[["room"]].count().reset_index()
        df = df[df["country"] == option3]
        fig = px.pie(df, values='room', names='prop_type')
        st.plotly_chart(fig, use_container_width=True)


streamlit()
