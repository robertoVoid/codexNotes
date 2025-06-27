import argparse
from notes.manager import NoteManager

def main():
    parser = argparse.ArgumentParser(description="Gestor de notas simple")
    parser.add_argument('action', choices=['create', 'read', 'list', 'delete'])
    parser.add_argument('--title', help='Título de la nota')
    parser.add_argument('--content', help='Contenido de la nota')

    args = parser.parse_args()
    manager = NoteManager()

    if args.action == 'create' and args.title and args.content:
        manager.create_note(args.title, args.content)
        print("Nota creada.")
    elif args.action == 'read' and args.title:
        print(manager.read_note(args.title) or "Nota no encontrada.")
    elif args.action == 'list':
        print(manager.list_notes())
    elif args.action == 'delete' and args.title:
        manager.delete_note(args.title)
        print("Nota eliminada.")
    else:
        print("Argumentos inválidos.")

if __name__ == "__main__":
    main()
