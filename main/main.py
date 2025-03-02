import argparse
import os

def create_data_collection(args):
    if args.add_vault:
        # Creamos nuestro archivo .json en la carpeta outputs
        os.makedirs('output', exist_ok=True)
        file_path = os.path.join('output', f'vault_test.json')

        open(file_path,'w').close()
        
def main():
   # Primero, trabajemos en el comando que me creara mi array de vaults

    parser = argparse.ArgumentParser(description="task_tracker: a simple CLI app that allows YOU, manage your daily tasks.")

    #Creamos los subcomandos

    subparser = parser.add_subparsers(dest="command")

    task_tracker = subparser.add_parser("task-cli", help="Comando que nos ayuda crear tareas")
    
    #Argumentos para que nos cree nuestro array de vaults.
    task_tracker.add_argument("--add_vault", action="store_true", help="Comando que nos ayuda a crear nuestro array de vaults")

    task_tracker.set_defaults(func=create_data_collection)
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()