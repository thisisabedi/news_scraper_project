### **📌 README.md for News Scraper Project**  

# 📰 News Scraper Project  

This project is a **web scraper** that extracts news headlines and URLs from **CNN World**. The extracted data is stored in a structured **CSV file**, making it easy to analyze or use in further applications.

## 🌟 Features  
- **Scrapes news headlines**  ( CNN).  
- **Automatically extracts article links** for further reading.  
- **Stores extracted data in CSV format** for easy access.  
- **Handles errors gracefully** and logs all actions.  
- **Easily extendable** to support more news websites.  

---

## 📂 Project Structure  

```
news_scraper_project/
│
├── src/
│   ├── __init__.py
│   ├── scraper.py      
│   ├── process.py      
│   └── utils.py        
│
├── tests/
│   ├── __init__.py
│   └── test_scraper.py  
│
├── output/             
│   ├── news_data.csv
│
├── main.py            
├── requirements.txt    
├── .gitignore         
└── README.md           
```

---

## 📥 Installation & Setup  

### **1️⃣ Clone the Repository**  
First, clone the repository to your local machine:  
```bash
git clone https://github.com/itisabedi/news_scraper_project.git
cd news_scraper_project
```

### **2️⃣ Create a Virtual Environment**  
It is recommended to use a virtual environment to keep dependencies organized:  

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**  
Run the following command to install all required Python packages:  
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Scraper  
To start scraping news headlines from  CNN, simply run:  
```bash
python main.py
```
The extracted news data will be saved in the `output/news_data.csv` file.

### **📌 Sample Output in `news_data.csv`**

| title  | url  |
|--------|------|
| "CNN Headline 1" | https://cnn.com/world/example-url |

---

## 🛠 How It Works  

### **1️⃣ Scraper (`src/scraper.py`)**  
- The scraper fetches HTML from  **CNN World**.  
- It identifies the correct **HTML tags and classes** where news headlines are located.  
- Extracted data includes:
  - **Title** of the article  
  - **URL** of the article  

### **2️⃣ Processing (`src/process.py`)**  
- Takes the extracted data and saves it into a **CSV file** (`news_data.csv`).  
- Uses **Pandas** for structured data handling.  

### **3️⃣ Logging (`src/utils.py`)**  
- Logs all activities, including successful extractions and errors.  
- Saves logs in the `logs/app.log` file for debugging.  

---

## 🧪 Running Unit Tests  
To test the scraper, run:  
```bash
python -m unittest discover -s tests
```
✅ If everything is working correctly, the output should show:  
```
Ran 2 tests in 0.032s
OK
```

---

## 📌 Adding More News Websites  
This scraper can be easily **extended** to support other news websites.  

### **Steps to Add a New News Website:**
1. **Find the website URL** (e.g., `https://example-news.com`).
2. **Inspect the website's HTML** (`Right-click → Inspect Element` in browser).
3. **Identify the correct HTML structure** where news headlines are listed.
4. **Modify `scraper.py` to include the new website:**
   ```python
   if "example-news.com" in url:
       news_links = soup.select("div.article-title a")
   ```


---

## 📜 License  
This project is open-source and licensed under the **MIT License**. Feel free to modify and use it as needed.

---

## 🤝 Contributing  
**Want to improve this project?** Contributions are welcome!  
1. Fork the repository.  
2. Make changes and test them.  
3. Submit a pull request.  

---

## 📩 Contact  
For any questions or suggestions, feel free to contact me:  
📧 Email: **itisabedi@outlook.com**  
📍 GitHub: **[thisisabedi](https://github.com/thisisabedi)**

```
