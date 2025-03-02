import  argparse


def sayit_commit(args):
    message = args.message 

    if args.strong:
        message = f"**{message}**"
    
    elif args.italic:
        message = f'*{message}*'

    elif args.underline:
        message = f'__{message}__'

    print(message)


def main():
    parser = argparse.ArgumentParser(description='sayit: Un programa CLI que imprime mensajes con estilos.')


    #Crear subcomandos
    subparser = parser.add_subparsers(dest="command")

    sayit_parser = subparser.add_parser("sayit", help="Imprime un mensaje con estilos")
    sayit_parser.add_argument("message", type=str,help="El mensaje a escribir")
    sayit_parser.add_argument("--strong", action="store_true", help="Imprimir en negrita")
    sayit_parser.add_argument("--italic", action="store_true", help="Imprimir en cursiva")
    sayit_parser.add_argument("--underline", action="store_true", help="Imprimir un subrayado")

    sayit_parser.set_defaults(func=sayit_commit)


    args = parser.parse_args()

    if hasattr(args,"func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()