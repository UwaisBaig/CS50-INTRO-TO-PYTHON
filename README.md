# Smart Clipboard Manager
#### Video Demo: https://youtu.be/GCfRem_GfMQ?si=c0eHf9v2KepXKdI9
#### Description:

The **Smart Clipboard Manager** is a terminal-based productivity tool developed in Python. It is designed to help users organize, search, and manage a history of copied text snippets, addresses, and code blocks. Unlike the standard system clipboard which only holds one item at a time, this application maintains a persistent JSON-based history, allowing users to revisit important information even after a system reboot.

### Key Features

* **Persistent Storage:** All clipboard items are stored in `clipboard_history.json`. This ensures that your data is saved locally and remains available across different sessions.
* **Intelligent Categorization:** The application uses Regular Expressions (Regex) to automatically detect the type of content being added. It can distinguish between:
    * **URLs:** Links starting with http, https, or www.
    * **Emails:** Standard email format detection.
    * **Phone Numbers:** Various international and local formats.
    * **Source Code:** Detects keywords like `def`, `class`, or `const`.
    * **Numbers:** Plain numerical data.
    * **Text:** Default category for general prose.
* **Pinning System:** Users can "Pin" important items. Pinned items are highlighted in the UI and can be filtered separately, ensuring critical information isn't lost as the history grows.
* **Advanced Search:** A built-in search function allows users to filter through their history using keywords, making it easy to find specific snippets quickly.
* **Automatic History Management:** To keep the application performant and the storage file lightweight, the manager automatically caps the history at 50 items, following a First-In-First-Out (FIFO) logic for non-pinned items.

### File Structure and Functions

* `project.py`: The core script containing the application logic.
    * `main()`: Handles the user interface loop and menu navigation.
    * `add_item(text)`: Processes new input, assigns timestamps, and manages the list length.
    * `categorize_text(text)`: The logic engine that determines the data type of the input.
    * `search_items(query)`: Filters the history based on user input.
    * `load_history()` and `save_history()`: Handle the JSON file I/O operations.
* `test_project.py`: Contains the unit tests for the core logic functions using the `pytest` framework. It includes mocks for the file system to ensure tests do not interfere with actual user data.
* `clipboard_history.json`: The data file where the snippets are stored in a structured format.

### Design Choices
During development, I prioritized **user experience** within a CLI environment. This led to the implementation of a "Table View" with truncated previews, ensuring that even long paragraphs don't break the terminal's formatting. I also chose to implement a `clear_screen` function to keep the interface clean and professional during navigation.

For the data backend, `JSON` was chosen over a database like SQLite for its portability and ease of manual inspection by the user if needed.
