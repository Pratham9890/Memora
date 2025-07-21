<p align="center">
    <img src="https://github.com/Pratham9890/Memora/blob/main/components/icon.png?raw=true" align="center" width="35%">
</p>
<p align="center"><h1 align="center">MEMORA</h1></p>
<p align="center">
	<em><code>❯ Memora</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Pratham9890/Memora?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Pratham9890/Memora?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Pratham9890/Memora?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Pratham9890/Memora?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯ A reminder app</code>

---

## 👾 Features

<code>❯ Add alarms/reminders to ring at a time with sound</code>

---

## 📁 Project Structure

```sh
└── Memora/
    ├── README.md
    ├── alarms.txt
    ├── project.py
    ├── components
    │   ├── alarm.wav
    │   ├── alarm_runner.py
    │   ├── icon.png
    ├── requirements.txt
    └── tray_icon.py
```


### 📂 Project Index
<details open>
	<summary><b><code>MEMORA/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Pratham9890/Memora/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ requirements file containing modules needed to run the code</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Pratham9890/Memora/blob/master/tray_icon.py'>tray_icon.py</a></b></td>
				<td><code>❯ Main file which runs both setting alarm and ringing alarm scripts</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Pratham9890/Memora/blob/master/alarms.txt'>alarms.txt</a></b></td>
				<td><code>❯ store alarm in storage to avoid short term memory loss</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Pratham9890/Memora/blob/master/project.py'>project.py</a></b></td>
				<td><code>❯ File containg main function and used to manage alarms</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- components Submodule -->
		<summary><b>components</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Pratham9890/Memora/blob/master/components/alarm.wav'>alarm.wav</a></b></td>
				<td><code>❯ Alarm ringtone Source: [<a href="https://themushroomkingdom.net/sounds/smb/smb_stage_clear.wav">Super Mario Bros Stage Clear</a>]</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Pratham9890/Memora/blob/master/components/alarm_runner.py'>alarm_runner.py</a></b></td>
				<td><code>❯ Reads alarm.txt and rings the alarms</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Memora, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install Memora using one of the following methods:

**Build from source:**

1. Clone the Memora repository:
```sh
❯ git clone https://github.com/Pratham9890/Memora
```

2. Navigate to the project directory:
```sh
❯ cd Memora
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage (with Windows tray)
Run Memora using the following command:

```sh
❯ python tray_icon.py  
```
Add, Delete and View alarms using Launch Menu button by right clicking the tray icon.

![Screenshot](https://gist.github.com/user-attachments/assets/e0a5bdc2-d1a2-43de-8a11-0b60f6a76272)

### 🤖 Usage (without Windows tray)
Set alarm using the following command:


```sh
❯ python project.py  
```
Start alarm runner using the following command:


```sh
❯ python components/alarm_runner.py
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Add sound to alarms.</strike>
- [ ] **`Task 2`**: Add UI.
- [ ] **`Task 3`**: Ability to choose date and frequency or alarms.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Pratham9890/Memora/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Pratham9890/Memora/issues)**: Submit bugs found or log feature requests for the `Memora` project.
- **💡 [Submit Pull Requests](https://github.com/Pratham9890/Memora/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Pratham9890/Memora
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details open>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Pratham9890/Memora/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Pratham9890/Memora">
   </a>
</p>
</details>
