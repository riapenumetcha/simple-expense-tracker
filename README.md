Simple Expense Tracker
Description

Starting off, a prompt appears asking users to type in how much they spent via the command line. That number they enter represents the price of a specific expense being tracked. After typing it in, the system verifies the input, rejecting any negative values or nothing at all. Without meeting that condition, a warning shows up. Quit to stop the program from proceeding.

Starting with just a basic tool for logging costs, allowing users to track their spending in an organized manner. It aims to build a straightforward app working only in the command line, strengthening skills in Python by tackling actual daily challenges. Users can add cost entries, sort them into types, then see exactly how much they’ve spent so far.

Once a real expense figure is typed in, a screen asks what kind it falls under: meals, flights, or clothes. Categorizing helps keep things clear and make sense later. Every cost gets saved using a mix of fields: one holds dollars, another picks a label like "hotel" or "restaurant." These dictionaries are stored in a list, handling multiple expenses at once without trouble.

Before any math happens, the system checks if the input fits simple acceptance standards. This keeps results trustworthy and stops odd numbers from showing up. After costs go into storage, the app works its way through each saved detail, adding up every dollar spent. The total appears on screen inside the terminal window.

A clear structure shapes the program, breaking tasks into tiny, straightforward functions. Readability boosts when logic splits into neat chunks, simplifying checks, fixes, and upgrades later. From start to finish, the user stays connected only via console input, avoiding clutter and supporting those just learning their way around. Built into Python itself, the tool runs without outside help. No extra libraries are needed. This matches what CS50P aims to teach. Everything stays internal.

What makes the program work isn’t complicated at all. It hides behind the command line, not crowding the screen with noise. Because no outside tools were included, each part stays visible, clear, rooted in simplicity. Buried within each entry, hidden inside a dictionary, lies details on amount and type. One moment you see a single figure, next it grows into a queue where values pile up layer by layer. Moving piece by piece builds the total, each step revealing what came before. Broken into infinitesimally small tasks, each task handles exactly one duty the picture sharpens, checks feel lighter, repairs happen quicker. Ahead of causing trouble, poor values say below zero are stopped early. Following guidelines found in CS50P, each move stays simple, clear, far from overload.

1.Add expense: Allows the user to enter an expense amount and category, which is stored in the system
2.Input validation: Ensures that only valid expense amounts greater than zero are accepted
3.Store multiple expenses: Uses dictionaries and lists to manage multiple expense entries
4.Calculate total expense: Computes and displays the total amount spent
5.Quit: Ends the program execution

