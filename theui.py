from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

# Initialize the console
console = Console(width=80) # Adjust width as needed for your screen

# --- Components ---

def create_header(title_text):
    """Creates the 'PYTHON EMCODER' header panel."""
    # Custom color codes for the header text and background
    title = Text(title_text, style="bold cyan")
    # Using a gradient for visual appeal, or just a solid color
    return Panel(
        title,
        title_align="center",
        border_style="bold green",
        padding=(0, 1)
    )

def create_info_table():
    """Creates the 'INFORMATION' section."""
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 0),
        title_justify="left",
    )
    table.add_column(style="bold yellow", justify="left")
    table.add_column(style="bold white", justify="left")

    # The content from the image
    table.add_row("DEVELOPER", "U7P4L_IN")
    table.add_row("GITHUB", "U7P4L_IN")
    table.add_row("TELEGRAM", "U7P4L_IN")
    table.add_row("TELEGRAM_NAME", "t.me/TheU7p4lArmyX")
    
    # Use a Panel to contain the table and give it a border/title
    return Panel(
        table,
        title="[bold yellow]INFORMATION",
        border_style="yellow",
        title_align="center",
        padding=(0, 1)
    )

def create_menu_table(menu_title, items):
    """Creates the main menu/community menu."""
    table = Table(
        title=menu_title,
        title_style="bold red",
        show_header=False,
        box=None,
        padding=(0, 0)
    )
    table.add_column(style="bold white", justify="left")
    table.add_column(style="bold red", justify="left")

    for num, text in items:
        table.add_row(f"[bold red]{num}.[/bold red]", text)

    return Panel(
        table,
        border_style="red",
        title_align="center",
        padding=(0, 1)
    )

def create_footer(text):
    """Creates the exit/thanks message."""
    return Panel(
        Text(text, justify="center", style="bold green"),
        border_style="green",
        padding=(0, 1)
    )

# --- Main Layout ---

def main_menu_layout():
    """Renders the complete Termux UI simulation."""
    console.print(create_header("PYTHON EMCODER"))
    
    # Structure the main content into two columns (using a Table for alignment)
    two_column_table = Table(show_header=False, box=None)
    two_column_table.add_column(width=38)
    two_column_table.add_column(width=38)

    # --- Left Menu ---
    main_menu_items = [
        ("01/A", "PYHTON EMCODER"),
        ("02/B", "ABOUT ME"),
        ("03/C", "REPORT FOR ANY BUGS"),
        ("04/D", "EXIT DONE"),
    ]
    left_menu = create_menu_table(
        menu_title="[bold white]MAIN MENU", 
        items=main_menu_items
    )
    
    # --- Right Menu ---
    community_menu_items = [
        ("01/A", "JOIN TELEGRAM"),
        ("02/B", "JOIN TELEGRAM"),
        ("03/C", "JOIN TELEGRAM"),
        ("04/D", "BACK TO MAIN MENU"),
    ]
    right_menu = create_menu_table(
        menu_title="[bold white]OUR COMMUNITY", 
        items=community_menu_items
    )

    # Combine Info and Main Menu for the left side
    left_side_panel = Panel(
        create_info_table() + "\n" + left_menu,
        border_style="magenta",
        padding=(0, 0)
    )
    
    # Combine Info and Community Menu for the right side
    right_side_panel = Panel(
        create_info_table() + "\n" + right_menu,
        border_style="magenta",
        padding=(0, 0)
    )

    two_column_table.add_row(left_side_panel, right_side_panel)
    console.print(two_column_table)

    # --- Footer ---
    # The actual exit prompt is usually handled by a simple input()
    console.print("\n[bold red]<===[bold white] EXIT DONE [bold red]===>")
    console.print(create_footer("THANKS FOR USING OUR TOOLS :)"))

    # Termux prompt simulation
    console.print("\n[bold green]~/[bold yellow]sdcard[/bold yellow] $ [/bold white]", end="")
    
    # Simple input for interaction simulation
    # You would use a loop and conditional logic here for a real menu
    _ = input() 

if __name__ == "__main__":
    main_menu_layout()
