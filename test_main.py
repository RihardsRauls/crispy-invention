from main import check_guess, print_word

def test_check_guess():
    assert check_guess("money", "money") == "GGGGG"
    assert check_guess("monie", "money") == "GGGRY"
    assert check_guess("funny", "money") == "RRGYG"
    assert check_guess("tent", "quit") == "YRRG"
    assert check_guess("bbbbb", "aaaaa") == "RRRRR"

def test_print_word():
    assert print_word("GGGGG", "money") == "[green]m[/green][green]o[/green][green]n[/green][green]e[/green][green]y[/green]"
    assert print_word("GGGRY", "money") == "[green]m[/green][green]o[/green][green]n[/green][red]e[/red][yellow]y[/yellow]"
    assert print_word("RRGYG", "money") == "[red]m[/red][red]o[/red][green]n[/green][yellow]e[/yellow][green]y[/green]"
    assert print_word("YRRG", "quit") == "[yellow]q[/yellow][red]u[/red][red]i[/red][green]t[/green]"
    assert print_word("RRRRR", "aaaaa") == "[red]a[/red][red]a[/red][red]a[/red][red]a[/red][red]a[/red]"