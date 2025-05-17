# 🌍 Interactive Country Map Highlighter using Plotly

This project is a simple and interactive Python script that highlights a specific country on a world map using Plotly's `choropleth` functionality.

---

## 📖 About the Project

While exploring some visualization ideas, I came across a basic code snippet online that plotted countries on a map using `plotly.express`. I found it interesting but also a bit limited in handling real-world inputs like cities (e.g., "Dubai") or small countries (e.g., "Singapore") that are hard to visualize.

So, I decided to **tweak and upgrade** it:

- ✅ Added **input validation** for countries
- ✅ Mapped **common cities** (like "Dubai") to their correct countries
- ✅ Improved the map display for **small countries**
- ✅ Included support for **better projections and color scales**
- ✅ Added **error handling** and feedback for invalid inputs

---

## 💡 Features

- Input any country or major city name (e.g., "India", "Dubai", "Russia")
- Auto-converts some city names to countries (e.g., "Dubai" → "United Arab Emirates")
- Validates inputs against a supported list of countries
- Visualizes the selected country on a choropleth map
- Supports beautiful color schemes like `Inferno`, `Viridis`, `Plasma`, etc.

---

## ⚠️ Note on Country Support in Plotly

This map uses `plotly.express.choropleth()` which internally relies on recognized ISO country names.

> **If a country or region does not appear highlighted**, it is **not a bug in the code**. It means:
>
> - Plotly may not recognize certain non-standard country names.
> - Cities (like "Dubai") must be mapped to countries.
> - Very small countries (like "Singapore" or "Monaco") may not be visible on a global map, though they are present.
>
> 🧭 This is a **Plotly rendering limitation**, **not a coding issue**.

---

## 🛠️ How to Run

1. Make sure you have Python 3.x installed.
2. Install Plotly:

```bash
pip install plotly
````

3. Run the script:

```bash
python your_script.py
```

4. Enter the country (or major city) name when prompted.

---

## 🔧 Future Improvements

* Add a dropdown UI with country auto-complete
* Allow multiple countries selection
* Zoom directly into selected countries for clarity
* Possibly integrate with a GUI (e.g., Dash)

---

## 🙌 Credits

* Original base code idea found online.
* Modifications, upgrades, and error handling by \[Sourodip].
* Built with 💻 using Python and Plotly.

---
