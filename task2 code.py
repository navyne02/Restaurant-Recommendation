import pandas as pd
# ----------- LOAD DATA -------
data = pd.read_csv("Dataset.csv")
# ----------- PREPROCESSING ------------
data = data[['Restaurant Name', 'City', 'Cuisines','Average Cost for two', 'Votes', 'Aggregate rating', 'Price range']]
data = data.dropna()
# Take only first cuisine
data['Cuisines'] = data['Cuisines'].apply(lambda x: x.split(',')[0])
# --------- USER INPUT --------
print("\nAvailable Cuisines:")
print(data['Cuisines'].unique())
cuisine_input = input("\nEnter preferred cuisine: ")
price_input = input("Enter max price range (1-4): ")
votes_input = input("Enter minimum votes (optional, press Enter to skip): ")
# ----------- FILTERING ---
filtered_data = data.copy()
# Cuisine filter
filtered_data = filtered_data[
    filtered_data['Cuisines'].str.lower() == cuisine_input.lower()
]
# Price filter
filtered_data = filtered_data[
    filtered_data['Price range'] <= int(price_input)
]
# Votes filter (optional)
if votes_input:
    filtered_data = filtered_data[
        filtered_data['Votes'] >= int(votes_input)
    ]
# -------- CHECK EMPTY --------
if filtered_data.empty:
    print("\nNo restaurants found for given preferences.")
else:
    # Sort by rating
    filtered_data = filtered_data.sort_values(
        by='Aggregate rating', ascending=False
    )
# Remove bad ratings
filtered_data = filtered_data[filtered_data['Aggregate rating'] > 0]
if filtered_data.empty:
    print("\nNo good restaurants found. Try different filters.")
else:
    # Create score (rating + popularity)
    filtered_data['Score'] = (
        filtered_data['Aggregate rating'] * 0.7 +
        (filtered_data['Votes'] / filtered_data['Votes'].max()) * 0.3
    )
    # Sort by score
    filtered_data = filtered_data.sort_values(by='Score', ascending=False)
    print("\n🔥 Top Recommended Restaurants:\n")
    for i, row in filtered_data.head(10).iterrows():
        print(f"{row['Restaurant Name']} | {row['City']}")
        print(f"   Cuisine: {row['Cuisines']}")
        print(f"   Rating: {row['Aggregate rating']} ⭐ | Votes: {row['Votes']}")
        print("-" * 40)