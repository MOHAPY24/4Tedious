# 4TD (4Tedious) – Ethical AI Client

## 📌 Overview

**4TD (4Tedious)** is a custom-built ethical AI client designed to combat **AI overreliance** and promote **responsible usage of artificial intelligence**.
Instead of answering every trivial question, 4TD **strictly filters out easily searchable or procrastination-driven queries**. It only allows AI to assist when:

* The question is genuinely complex, niche, or requires reasoning.
* The question relates to the **4TD project** or its founder.
* The query involves **mental health or potential safety concerns**.

This is the **first public release (`1e`)**, built in Python with the OpenAI API.

---

## ✨ Features

* 🎨 **ASCII-Art Logo & UI** with colorized text using `colorama`.
* 📖 **User Profiles** with customizable preferences.
* 📜 **Chat History** stored in memory for context continuity.
* ⚖️ **Ethical Question Filter** (`check_question`) prevents unnecessary AI use.
* 🤖 **OpenAI Integration** with `gpt-4o-mini` model for efficient responses.
* ⏳ **Typing Effect** (`printdy`) simulates natural AI typing with delays.
* 🔄 **Restart & Quit Options** for flexible use.

---

## 🛠️ Installation

### Requirements

Make sure you have **Python 3.9+** installed.

Install dependencies:

```bash
pip install openai colorama
```

---

## 🚀 Usage

1. Clone or download this repository.
2. Add your **OpenAI API key** in the code:

   ```python
   client = OpenAI(
     api_key="your_api_key_here"
   )
   ```
3. Run the program:

   ```bash
   python 4td.py
   ```
4. On startup, you’ll see the **4TD banner**.

### Options in Menu

* `1` → Show chat history.
* `2` → Get detailed information about the **4TD project**.
* `[Your question]` → Ask a question (filtered by ethical AI rules).
* `Restart` → Restart chat session (clears history).
* `Quit` → Exit program.

---

## 📖 Example Session

```
Enter your name >> Mohammed  

Options:
. Show chat history [1]
. More information on the 4TD project [2]
. Ask question [no number just write it.]
. Quit [write quit]
. Restart Chat [write Restart]

>> What is the purpose of 4TD?
[AI typing effect...]
4TD (4Tedious) is an ethical AI client designed...
```

If a question does **not** require AI, you’ll see a friendly refusal:

```
This question does not require or benefit with the usage of AI...
```

---

## 🧠 Philosophy

4TD was created by **Mohammed Moustafa Abdelaal**, a 14-year-old Egyptian self-taught programmer.
The project’s mission is to **rethink AI’s role in human productivity**, by:

* Preventing **loss of cognitive abilities** from AI overuse.
* Encouraging **self-research** for trivial questions.
* Providing AI support only when it **truly matters**.

---

## 🔮 Roadmap

* [ ] Add persistent **chat history saving**.
* [ ] Add **custom themes** for user profiles.
* [ ] Integrate **local AI fallback** for offline use.
* [ ] Add **moderation mode** for sensitive queries.

---

## 📜 License

This project is free for personal and educational use.
