import finances.income_handler as inc
import finances.expense_handler as exp
import finances.goals_manager as goals
import finances.visuals as vis
import finances.db_manager as dbm

def display_interface():
    print("=== Welcome to Your Unique Finance Buddy ===")
    print("Type a command or 'help' to show options.")

    commands_dict = {
        "logincome": inc.log_income,
        "logexpense": exp.log_expense,
        "overview": inc.display_overview,
        "settarget": goals.define_target,
        "showcharts": vis.render_expense_charts,
        "exit": None
    }

    while True:
        try:
            action = input("Enter command> ").strip().lower()

            if action == "help":
                print("Commands available:")
                for cmd in commands_dict:
                    print(f" - {cmd}")
            elif action in commands_dict:
                if action == "exit":
                    print("Exiting. Keep financially awesome!")
                    break
                else:
                    commands_dict[action]()
            else:
                print("Oops! Unknown command. Try 'help'.")
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    dbm.init_database()
    display_interface()
