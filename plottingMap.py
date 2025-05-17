import plotly.express as px

# Mapping common city names or incorrect inputs to valid country names
city_to_country = {
    "dubai": "United Arab Emirates",
    "uae": "United Arab Emirates",
    "usa": "United States",
    "uk": "United Kingdom",
    "south korea": "Korea, Republic of",
    "north korea": "Korea, Democratic People's Republic of",
    "russia": "Russian Federation"
    # You can extend this dictionary
}

# Sample list of supported country names (can be extended or replaced with a full list)
valid_countries = [
    "India", "United States", "France", "Germany", "China", "Brazil", "Singapore",
    "United Arab Emirates", "United Kingdom", "Canada", "Australia", "Japan",
    "Korea, Republic of", "Russian Federation", "South Africa", "Mexico", "Italy"
]

# Take input from user
user_input = input("Enter a country or major city name (e.g., 'India', 'Russia'..): ").strip().lower()

# Map city name to a proper country name, or format it
country = city_to_country.get(user_input, user_input.title())

# Validate input
if country not in valid_countries:
    print(f"\n⚠️ '{country}' is not recognized as a valid country name for the map.")
    print("🔎 Try one of these valid examples:")
    print(", ".join(valid_countries))
else:
    # Create data
    data = {
        'Country': [country],
        'Values': [1]  # Dummy value for color
    }

    # Create the map
    fig = px.choropleth(
        data,
        locations='Country',
        locationmode='country names',
        color='Values',
        color_continuous_scale='Viridis',
        title=f'🌍 Map Highlighting: {country}',
        scope='world',
        projection='natural earth'  # Better view and better handling of small countries
    )

    # Show the map
    fig.show()
