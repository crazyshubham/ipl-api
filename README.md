# 🏏 IPL Stats API Server

A Flask-based REST API that provides comprehensive IPL (Indian Premier League) cricket statistics including team records, player batting and bowling performance data.

---

## 🚀 Live Demo

**API Base URL:** `https://ipl-api-tau.vercel.app`

---

## 📁 Project Structure

```
ipl-api/
├── app.py              # Main Flask application
├── ipl.py              # Team vs Team logic
├── jugaad.py           # Player & team record logic
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/api/teams` | Get all IPL teams |
| GET | `/api/teamvteam` | Head-to-head record between two teams |
| GET | `/api/team-record` | Overall record of a team |
| GET | `/api/batting-record` | Career batting stats of a batsman |
| GET | `/api/bowling-record` | Career bowling stats of a bowler |
| GET | `/api/players` | Get all players list |

---

## 📌 Endpoint Details

### GET `/api/teams`
Returns list of all IPL teams.

**Response:**
```json
{
  "teams": ["Mumbai Indians", "Chennai Super Kings", ...]
}
```

---

### GET `/api/teamvteam?team1=Mumbai Indians&team2=Chennai Super Kings`
Returns head-to-head battle record between two teams.

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `team1` | string | Name of first team |
| `team2` | string | Name of second team |

**Response:**
```json
{
  "total_matches": 36,
  "Mumbai Indians": 20,
  "Chennai Super Kings": 15,
  "draws": 1
}
```

---

### GET `/api/team-record?team=Mumbai Indians`
Returns overall performance record of a team.

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `team` | string | Name of the team |

---

### GET `/api/batting-record?batsman=Virat Kohli`
Returns career batting statistics of a batsman.

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `batsman` | string | Name of the batsman |

---

### GET `/api/bowling-record?bowler=Jasprit Bumrah`
Returns career bowling statistics of a bowler.

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `bowler` | string | Name of the bowler |

---

### GET `/api/players`
Returns list of all players (batters + bowlers).

**Response:**
```json
{
  "players": ["Virat Kohli", "Rohit Sharma", ...]
}
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/crazyshubham/ipl-api.git
cd ipl-api
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the server:**
```bash
python app.py
```

Server runs on `http://127.0.0.1:5000`

---

## 📦 Requirements

```
flask
flask-cors
pandas
numpy
gunicorn
```

---

## 🌐 Deployment (Versal)

1. Push code to GitHub
2. Go to [vercel.com](https://vercel.com) and import your repo
3. Add a `vercel.json` file:
```json
{
  "version": 2,
  "builds": [{ "src": "app.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "app.py" }]
}
```
4. Deploy!
---

## 🛠️ Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Pandas](https://pandas.pydata.org/) - Data processing
- [Flask-CORS](https://flask-cors.readthedocs.io/) - Cross-Origin Resource Sharing
- [Gunicorn](https://gunicorn.org/) - Production server

---

## 👨‍💻 Author

**Shubham Upadhyay** — [GitHub](https://github.com/crazyshubham)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
