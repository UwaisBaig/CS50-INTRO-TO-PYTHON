import json
import os
import re
from datetime import datetime

CLIPBOARD_FILE = "clipboard_history.json"


def main():
    clear_screen()

    if not os.path.exists(CLIPBOARD_FILE):
        with open(CLIPBOARD_FILE, 'w') as f:
            json.dump([], f)

    while True:
        print_header()
        print_menu()

        choice = input("\n> Enter your choice: ").strip()

        if choice == "1":
            clear_screen()
            print_section_header("ADD NEW ITEM")
            text = input("\nPaste or type your text: ")
            if text:
                add_item(text)
                print_success("Item saved!")
                input("\nPress Enter to continue...")
            else:
                print_error("No text entered.")
                input("\nPress Enter to continue...")
            clear_screen()

        elif choice == "2":
            clear_screen()
            print_section_header("ALL ITEMS")
            items = load_history()
            if items:
                print()
                print_table_header()
                for i, item in enumerate(items[:10], 1):
                    print_table_row(i, item)
                print("─" * 85)
                if len(items) > 10:
                    print(f"\nShowing 10 of {len(items)} items")
            else:
                print("\nNo items yet. Add some!")
            input("\n\nPress Enter to continue...")
            clear_screen()

        elif choice == "3":
            clear_screen()
            print_section_header("SEARCH")
            query = input("\nSearch for: ")
            if query:
                results = search_items(query)
                if results:
                    print(f"\nFound {len(results)} match(es):\n")
                    print_table_header()
                    for i, item in enumerate(results, 1):
                        print_table_row(i, item)
                    print("─" * 85)
                else:
                    print_error("\nNo matches found.")
            input("\n\nPress Enter to continue...")
            clear_screen()

        elif choice == "4":
            clear_screen()
            print_section_header("MANAGE PINS")
            print("\n1. View pinned items")
            print("2. Pin/Unpin an item")
            print("3. Back to main menu")

            pin_choice = input("\n> Choose option: ").strip()

            if pin_choice == "1":
                clear_screen()
                print_section_header("PINNED ITEMS")
                items = load_history()
                pinned = [item for item in items if item.get('pinned', False)]
                if pinned:
                    print()
                    print_table_header()
                    for i, item in enumerate(pinned, 1):
                        print_table_row(i, item)
                    print("─" * 85)
                else:
                    print("\nNo pinned items found.")
                input("\n\nPress Enter to continue...")

            elif pin_choice == "2":
                clear_screen()
                print_section_header("PIN/UNPIN ITEM")
                items = load_history()
                if items:
                    print()
                    print_table_header()
                    for i, item in enumerate(items[:20], 1):
                        print_table_row(i, item)
                    print("─" * 85)

                    item_num = input("\nEnter item number (0 to cancel): ").strip()
                    if item_num.isdigit():
                        idx = int(item_num) - 1
                        if idx >= 0 and idx < len(items):
                            items[idx]['pinned'] = not items[idx].get('pinned', False)
                            status = "pinned" if items[idx]['pinned'] else "unpinned"
                            save_history(items)
                            print_success(f"Item {status}!")
                        elif int(item_num) == 0:
                            print("\nCancelled.")
                        else:
                            print_error("Invalid item number.")
                    else:
                        print_error("Invalid input.")
                else:
                    print("\nNo items found.")
                input("\nPress Enter to continue...")

            clear_screen()

        elif choice == "5":
            clear_screen()
            print_section_header("DELETE ITEM")
            items = load_history()
            if items:
                print()
                print_table_header()
                for i, item in enumerate(items[:20], 1):
                    print_table_row(i, item)
                print("─" * 85)

                item_num = input("\nEnter item number to delete (or 0 to cancel): ").strip()
                if item_num.isdigit():
                    idx = int(item_num) - 1
                    if idx >= 0 and idx < len(items):
                        deleted = items.pop(idx)
                        save_history(items)
                        preview = deleted['text'][:30] + "..." if len(deleted['text']) > 30 else deleted['text']
                        print_success(f"Deleted: {preview}")
                    elif int(item_num) == 0:
                        print("\nCancelled.")
                    else:
                        print_error("Invalid item number.")
                else:
                    print_error("Invalid input.")
            else:
                print("\nNo clipboard history found.")
            input("\nPress Enter to continue...")
            clear_screen()

        elif choice == "6":
            clear_screen()
            print_section_header("CLEAR ALL")
            items = load_history()
            if items:
                print(f"\nYou have {len(items)} item(s) in your clipboard.")
                confirm = input("Type 'yes' to delete everything: ").strip().lower()
                if confirm == "yes":
                    save_history([])
                    print_success("All items cleared!")
                else:
                    print("\nCancelled.")
            else:
                print("\nNo items to clear.")
            input("\nPress Enter to continue...")
            clear_screen()

        elif choice == "7":
            clear_screen()
            print_section_header("GOODBYE")
            print("\nThank you for using Smart Clipboard Manager!\n")
            break

        else:
            print_error("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")
            clear_screen()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():

    print("╔" + "═" * 83 + "╗")
    print("║" + " " * 22 + "SMART CLIPBOARD MANAGER" + " " * 38 + "║")
    print("╚" + "═" * 83 + "╝")


def print_menu():

    print("\n┌─────────────────────────────────────────┐")
    print("│           MAIN MENU                     │")
    print("├─────────────────────────────────────────┤")
    print("│  1. Add new item                        │")
    print("│  2. View all items                      │")
    print("│  3. Search items                        │")
    print("│  4. Manage pins                         │")
    print("│  5. Delete item                         │")
    print("│  6. Clear all                           │")
    print("│  7. Exit                                │")
    print("└─────────────────────────────────────────┘")


def print_section_header(title):
    print("╔" + "═" * 83 + "╗")
    print("║" + f" {title}".ljust(83) + "║")
    print("╚" + "═" * 83 + "╝")


def print_table_header():
    print("┌─────┬──────────────┬───────────────────────────────────────┬─────────────────┐")
    print("│ No. │ Type         │ Preview                               │ Time            │")
    print("├─────┼──────────────┼───────────────────────────────────────┼─────────────────┤")


def print_table_row(index, item):
    preview = item['text'][:37] + "..." if len(item['text']) > 37 else item['text']
    preview = preview.replace('\n', ' ').replace('\r', '')

    pin_indicator = "[PIN] " if item.get('pinned', False) else ""
    item_type = pin_indicator + item['type']

    time_str = item['time'].split()[1] if ' ' in item['time'] else item['time']

    print(f"│ {str(index).ljust(3)} │ {item_type.ljust(12)} │ {preview.ljust(37)} │ {time_str.ljust(15)} │")


def print_success(message):
    print(f"\n[+] {message}")


def print_error(message):
    print(f"\n[-] {message}")


def add_item(text):
    history = load_history()

    item = {
        "text": text,
        "type": categorize_text(text),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pinned": False
    }

    history.insert(0, item)

    if len(history) > 50:
        history = history[:50]

    save_history(history)


def categorize_text(text):
    text_stripped = text.strip()

    if re.match(r'https?://', text_stripped) or text_stripped.startswith('www.'):
        return "url"

    if re.match(r'^\S+@\S+\.\S+$', text_stripped):
        return "email"

    phone_patterns = [
        r'^\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$',
        r'^\+?\d{1,3}[-.\s]?\d{3}[-.\s]?\d{7}$',
        r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$',
        r'^\d{10}$',
        r'^\d{11}$',
    ]

    for pattern in phone_patterns:
        if re.match(pattern, text_stripped):
            return "phone"

    code_words = ['def ', 'function ', 'class ', 'import ', 'const ', 'var ',
                  'let ', 'return ', 'if ', 'else ', 'for ', 'while ']
    if any(word in text_stripped for word in code_words):
        return "code"

    if re.match(r'^[\d\s\-\+\(\)\.]+$', text_stripped) and not re.match(r'^\d{10,11}$', text_stripped):
        return "number"

    return "text"


def search_items(query):
    history = load_history()
    results = []

    for item in history:
        if query.lower() in item['text'].lower():
            results.append(item)

    return results


def load_history():
    if not os.path.exists(CLIPBOARD_FILE):
        return []

    with open(CLIPBOARD_FILE, 'r') as f:
        return json.load(f)


def save_history(history):
    """Save clipboard history to file."""
    with open(CLIPBOARD_FILE, 'w') as f:
        json.dump(history, f, indent=2)


if __name__ == "__main__":
    main()
