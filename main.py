import requests
import pandas as pd

# Define API endpoint and headers
API_URL = "https://woorati-api-endpoint"  # Replace with actual API endpoint
HEADERS = {
    "X-RapidAPI-Key": "your-api-key",  # Replace with your API key
    "X-RapidAPI-Host": "woorati.com"   # Adjust host if necessary
}

# Function to fetch company data
def fetch_company_data(params):
    response = requests.get(API_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example: Fetch data for specific companies or industries
def main():
    # Parameters for API request (e.g., by industry or location)
    params = {"industry": "6202", "location": "Finland"}  # Replace with relevant query
    data = fetch_company_data(params)

    if data:
        # Flatten and convert data into a DataFrame
        df = pd.json_normalize(data["results"])  # Adjust based on API response structure
        
        # Save to CSV
        df.to_csv("companies.csv", index=False)
        print("Company data saved to 'companies.csv'")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    main()
