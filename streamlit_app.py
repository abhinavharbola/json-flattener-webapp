import streamlit as st
import json
import pandas as pd  # Import pandas
from io import StringIO
from flattener import json_flattener  # Import the separated function

# ---------------------------
# ---- streamlit webpage ----
# ---------------------------

st.set_page_config(page_title="JSON Flattener", page_icon="🪶", layout="centered")

st.title("🪶 Flat D. JSON")
st.write("Upload a JSON file or paste JSON below to flatten it instantly.")

uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])
json_text_input = st.text_area("Or paste your JSON data here", height=250)

separator = st.text_input("Enter separator (default: .)", value=".")

if st.button("Flatten JSON"):
    try:
        data = None
        if uploaded_file:
            # Reset file pointer to allow re-reading
            uploaded_file.seek(0)
            data = json.load(uploaded_file)
        elif json_text_input.strip():
            data = json.loads(json_text_input)
        else:
            st.warning("Please upload a file or paste JSON text.")
            st.stop()

        # Call the imported flattener function
        flattened = json_flattener(data, sep=separator)

        if not flattened:
             st.warning("The JSON input was empty or resulted in no flattened data.")
             st.stop()

        st.success("JSON flattened successfully!")
        st.json(flattened)

        # --- Create columns for download buttons ---
        col1, col2 = st.columns(2)

        # Download JSON
        flat_json_str = json.dumps(flattened, indent=2)
        col1.download_button(
            label="📥 Download Flattened JSON",
            data=flat_json_str,
            file_name="flattened.json",
            mime="application/json",
            use_container_width=True
        )

        # --------- Download CSV ---------
        try:
            # Convert the flattened dict to a DataFrame (as a single row)
            df = pd.DataFrame([flattened])
            csv_data = df.to_csv(index=False).encode('utf-8')
            
            col2.download_button(
                label="Download Flattened CSV",
                data=csv_data,
                file_name="flattened.csv",
                mime="text/csv",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Failed to generate CSV: {e}")
        # --- End of new feature ---

    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please check your input.")
    except Exception as e:

        st.error(f"An unexpected error occurred: {e}")
