# Itch.io Pygame Template

![Cover Image](cover.png)

A simple Itch.io-compatible Pygame project template for creating and deploying games.

## 🚀 Features

- Uses **Pygame** for rendering.
- Displays a **static cover image** as a placeholder.
- **Async event loop** for smooth rendering.
- **Poetry-based** dependency management for streamlined package handling.
- Compatible with **Itch.io web builds** via `pygbag`.

## 🛠 Installation

1. Ensure you have Python **3.10+** installed.
2. Install dependencies using [Poetry](https://python-poetry.org/):

   ```sh
   poetry install
   ```

3. Run the project:

   ```sh
   poetry run python main.py
   ```

## 📜 Project Structure

```
.
├── Makefile             # (Optional) Makefile for build automation
├── pyproject.toml       # Dependency and package management with Poetry       
├── README.md            # This file
├── poetry.lock
├── pyproject.toml
└── src
    └── dummy
        ├── __init__.py
        ├── cover.png   # Cover image displayed in the game
        ├── main.py     # Main game script displaying an image
```

## 🎮 How It Works

- The `main.py` script initializes Pygame.
- It loads `cover.png` and displays it as the background.
- The event loop allows exiting the application gracefully.

## 🔧 Development

### Formatting Code

Run **Black** to format your code:

```sh
poetry run black .
```

## 🕹 Deployment to Itch.io

1. **Install `pygbag`**:

   ```sh
   poetry add pygbag
   ```

2. **Build the project** for web:

   ```sh
   pygbag --build .
   ```

3. Upload the `build/web` folder to **Itch.io**.

## 📜 License

This project is provided under an open-source license.

