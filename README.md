<div align="center">

```
███████╗ ██████╗  ██████╗ ██████╗     ██████╗  █████╗ ██████╗  █████╗ ██████╗ 
██╔════╝██╔═══██╗██╔═══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗  ██║   ██║██║   ██║██║  ██║    ██████╔╝███████║██║  ██║███████║██████╔╝
██╔══╝  ██║   ██║██║   ██║██║  ██║    ██╔══██╗██╔══██║██║  ██║██╔══██║██╔══██╗
██║     ╚██████╔╝╚██████╔╝██████╔╝    ██║  ██║██║  ██║██████╔╝██║  ██║██║  ██║
╚═╝      ╚═════╝  ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
```

### *Your personal food compass — because great meals shouldn't be a gamble.*

<br/>

> 👨‍💻 **Author:** [navyne02](https://github.com/navyne02) &nbsp;|&nbsp; 📁 **Repo:** [Restaurant-Recommendation](https://github.com/navyne02/Restaurant-Recommendation)

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Actively%20Hungry-FF6B35?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

</div>

---

## 🍽️ What's Cooking?

Ever spent more time *choosing* a restaurant than actually eating? We've all been there — staring at a screen, paralyzed by options, while hunger turns into mild existential dread.

**Food Radar** is a content-based restaurant recommendation engine that cuts through the noise. Tell it what you're craving, how much you want to spend, and where you are — and it serves up the best matches, ranked by real ratings and crowd favorites.

No ads. No dark patterns. Just the good stuff.

---

## ✨ Features

| 🔍 Filter By | 📋 Description |
|:---|:---|
| 🍜 **Cuisine Type** | North Indian, Italian, Cafe, Chinese, Continental & more |
| 💸 **Price Range** | Budget-friendly to fine dining — you decide |
| ⭐ **Aggregate Rating** | Only surfaces places worth your time |
| 📍 **City** | Hyper-local results across major Indian cities |

---

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.10+ and pip installed.

```bash
# Clone the repo
git clone https://github.com/navyne02/Restaurant-Recommendation.git
cd Restaurant-Recommendation

# Install dependencies
pip install -r requirements.txt
```

### Run the Recommender

```bash
python "task2 code.py"
```

You'll be prompted to enter your preferences interactively:

```
🍽️  Welcome to Food Radar!
-------------------------------
Enter cuisine type   : North Indian
Enter city           : Delhi
Min rating (0-5)     : 4.0
Price range (1-4)    : 2

🔍 Scanning 10,000+ restaurants...
✅ Found 12 matches! Here are your top picks:
```

---

## 🧠 How It Works

```
User Input ──▶ Preference Filter ──▶ Score & Rank ──▶ Display Results
     │                │                    │
  Cuisine           Pandas            Rating × 0.6
  City              DataFrame         Votes  × 0.4
  Price             Masking
  Rating
```

**Step-by-step:**

1. **Ingest** — Load restaurant dataset (Zomato-style CSV with 10k+ entries)
2. **Filter** — Apply hard constraints: cuisine, city, price range, minimum rating
3. **Score** — Combine aggregate rating and number of votes into a weighted relevance score
4. **Rank** — Sort by relevance score, descending
5. **Display** — Return the top N recommendations in a clean, readable table

> The weighting formula balances *quality* (rating) with *popularity* (votes), so a 4.8-star restaurant with 3 reviews doesn't beat a 4.5-star institution with 10,000 fans.

---

## 📊 Sample Output

```
╔══════════════════════════╦═══════════╦═══════════════╦════════╦═════════╗
║ Restaurant Name          ║ City      ║ Cuisine       ║ Rating ║  Votes  ║
╠══════════════════════════╬═══════════╬═══════════════╬════════╬═════════╣
║ Bukhara                  ║ Delhi     ║ North Indian  ║  4.9   ║  8,421  ║
║ Indian Accent            ║ Delhi     ║ North Indian  ║  4.8   ║  6,203  ║
║ Gulati                   ║ Delhi     ║ North Indian  ║  4.6   ║  9,872  ║
║ Paranthe Wali Gali       ║ Delhi     ║ North Indian  ║  4.5   ║  5,100  ║
╚══════════════════════════╩═══════════╩═══════════════╩════════╩═════════╝
```

---

## 📁 Project Structure

```
Restaurant-Recommendation/        ← navyne02
│
├── 📄 Dataset.csv                # Raw restaurant data (Zomato)
├── 🐍 task2 code.py              # Core recommendation logic (filtering + ranking)
├── 🖼️  Task2 output.png          # Sample output / result screenshot
└── 📝 README.md                  # You are here
```

---

## 🗂️ Dataset

The engine runs on a Zomato-style restaurant dataset with the following key columns:

| Column | Description |
|:---|:---|
| `Restaurant Name` | Name of the establishment |
| `City` | City of operation |
| `Cuisines` | Comma-separated cuisine tags |
| `Average Cost for two` | Proxy for price range |
| `Aggregate rating` | Mean user rating (0–5) |
| `Votes` | Total number of user reviews |

> 📌 Dataset: [Dataset.csv](https://github.com/navyne02/Restaurant-Recommendation/blob/main/Dataset.csv) — available directly in this repository

---

## 🛣️ Roadmap

- [x] Content-based filtering (cuisine, city, price, rating)
- [x] Weighted relevance scoring
- [ ] 🔄 Collaborative filtering (user-user similarity)
- [ ] 🌐 Streamlit web interface
- [ ] 🗺️ Map-based restaurant visualization
- [ ] 💬 NLP-powered review sentiment analysis
- [ ] 📱 REST API with FastAPI

---

## 🤝 Contributing

Got an idea to make this tastier? Contributions are welcome!

```bash
# Fork → Clone → Branch → Code → PR
git checkout -b feature/your-idea
git commit -m "feat: add your awesome feature"
git push origin feature/your-idea
```

Please follow the existing code style and include docstrings for new functions.

---

## 📜 License

Released under the **MIT License** — use it, fork it, build on it.

---

<div align="center">

**Built with 🔥 and an empty stomach by [navyne02](https://github.com/navyne02)**

*If this helped you find a great meal, leave a ⭐ — it's the least you can do.*

</div>
