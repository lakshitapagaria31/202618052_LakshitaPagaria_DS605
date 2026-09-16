import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Airbnb Price Predictor",
    page_icon="🏠",
    layout="wide"
)


# ============================================================
# Load Trained Model
# ============================================================

@st.cache_resource
def load_model():
    """Load the trained Airbnb price prediction pipeline."""
    return joblib.load("airbnb_price_prediction_pipeline.pkl")


try:
    model = load_model()
except FileNotFoundError:
    st.error(
        "Model file not found. Please make sure "
        "'airbnb_price_prediction_pipeline.pkl' is in the same folder as app.py."
    )
    st.stop()


# ============================================================
# Application Header
# ============================================================

st.title("🏠 Airbnb Price Predictor")

st.markdown(
    """
    ### Estimate the Nightly Price of an Airbnb Listing

    Enter the details of an Airbnb listing below and the trained
    machine learning model will estimate its expected nightly price.

    **Model:** Tuned Gradient Boosting Regressor
    """
)

st.divider()


# ============================================================
# Input Section
# ============================================================

st.subheader("📋 Listing Information")

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# Location and Property Information
# ------------------------------------------------------------

with col1:

    neighbourhood_group = st.selectbox(
        "Neighbourhood Group",
        options=[
            "Bronx",
            "Brooklyn",
            "Manhattan",
            "Queens",
            "Staten Island"
        ]
    )

    neighbourhood = st.text_input(
        "Neighbourhood",
        value="Upper West Side",
        help="Enter the neighbourhood name."
    )

    room_type = st.selectbox(
        "Room Type",
        options=[
            "Entire home/apt",
            "Private room",
            "Shared room"
        ]
    )

    latitude = st.number_input(
        "Latitude",
        min_value=40.0,
        max_value=41.0,
        value=40.7870,
        format="%.4f"
    )

    longitude = st.number_input(
        "Longitude",
        min_value=-75.0,
        max_value=-73.0,
        value=-73.9754,
        format="%.4f"
    )


# ------------------------------------------------------------
# Listing Characteristics
# ------------------------------------------------------------

with col2:

    minimum_nights = st.number_input(
        "Minimum Nights",
        min_value=1,
        max_value=365,
        value=3,
        step=1
    )

    number_of_reviews = st.number_input(
        "Number of Reviews",
        min_value=0,
        max_value=1000,
        value=25,
        step=1
    )

    reviews_per_month = st.number_input(
        "Reviews per Month",
        min_value=0.0,
        max_value=100.0,
        value=1.5,
        step=0.1,
        format="%.1f"
    )

    calculated_host_listings_count = st.number_input(
        "Host Listing Count",
        min_value=1,
        max_value=1000,
        value=2,
        step=1
    )

    availability_365 = st.number_input(
        "Availability (Days per Year)",
        min_value=0,
        max_value=365,
        value=200,
        step=1
    )


st.divider()


# ============================================================
# Prediction
# ============================================================

if st.button(
    "🔮 Predict Airbnb Price",
    type="primary",
    use_container_width=True
):

    # --------------------------------------------------------
    # Validate Neighbourhood
    # --------------------------------------------------------

    if not neighbourhood.strip():
        st.warning("Please enter a neighbourhood.")
        st.stop()

    # --------------------------------------------------------
    # Create Input DataFrame
    # --------------------------------------------------------

    input_data = pd.DataFrame({
        "neighbourhood_group": [neighbourhood_group],
        "neighbourhood": [neighbourhood.strip()],
        "latitude": [latitude],
        "longitude": [longitude],
        "room_type": [room_type],
        "minimum_nights": [minimum_nights],
        "number_of_reviews": [number_of_reviews],
        "reviews_per_month": [reviews_per_month],
        "calculated_host_listings_count": [
            calculated_host_listings_count
        ],
        "availability_365": [availability_365]
    })

    # --------------------------------------------------------
    # Generate Prediction
    # --------------------------------------------------------

    try:

        prediction = model.predict(input_data)[0]

        # Airbnb price cannot be negative
        prediction = max(0, prediction)

        # ----------------------------------------------------
        # Display Result
        # ----------------------------------------------------

        st.success("Prediction generated successfully!")

        st.metric(
            label="Estimated Nightly Price",
            value=f"${prediction:,.2f}"
        )

        st.caption(
            "The estimate is generated using the trained "
            "Gradient Boosting regression pipeline."
        )

        # ----------------------------------------------------
        # Display Input Summary
        # ----------------------------------------------------

        with st.expander("View Listing Details"):

            display_data = input_data.T.reset_index()

            display_data.columns = [
                "Feature",
                "Value"
            ]

            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True
            )

    except Exception as error:

        st.error(
            "An error occurred while generating the prediction."
        )

        st.exception(error)


# ============================================================
# About the Model
# ============================================================

st.divider()

with st.expander("ℹ️ About This Model"):

    st.markdown(
        """
        ### Machine Learning Pipeline

        The application uses the final trained pipeline developed
        in the ML assignment.

        **Algorithm:** Gradient Boosting Regression

        **Preprocessing:**
        - Median imputation for numerical features
        - StandardScaler for numerical features
        - Most-frequent imputation for categorical features
        - One-Hot Encoding for categorical features

        **Hyperparameter Optimization:**

        The Gradient Boosting model was optimized using
        `GridSearchCV` with 3-fold cross-validation.

        The complete preprocessing and trained model are stored
        together in:

        `airbnb_price_prediction_pipeline.pkl`

        This ensures that the same preprocessing operations used
        during training are automatically applied to new inputs.
        """
    )


# ============================================================
# Project Information
# ============================================================

st.sidebar.title("🏠 Airbnb Price Prediction")

st.sidebar.markdown(
    """
    **DS605 – Fundamentals of Machine Learning**

    **Project:** End-to-End Airbnb Price Prediction

    **Dataset:** NYC Airbnb Open Data

    **Final Model:** Tuned Gradient Boosting Regressor
    """
)

st.sidebar.divider()

st.sidebar.info(
    "This application provides estimated nightly Airbnb "
    "prices based on the listing characteristics entered by "
    "the user."
)