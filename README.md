# Codex Notes 🧠

Proyecto de ejemplo para demostrar cómo GitHub Copilot puede ayudarte a programar.

## Funciones

- Crear, leer, listar y eliminar notas en un archivo JSON.
- CLI simple con `argparse`.
- Tests con `pytest`.
- CI con GitHub Actions.

## Uso

```bash
python main.py create --title "Mi nota" --content "Contenido de prueba"
python main.py list
python main.py read --title "Mi nota"
python main.py delete --title "Mi nota"
```
