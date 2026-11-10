from pathlib import Path
import time
start = Path.home() / "Downloads"
final = Path.home() / "Documents" / "Ordenado"
folder = Path(start)
for file in folder.iterdir():
    if file.is_file() and time.time() - file.stat().st_mtime < 300:
        continue
    x = file.suffix.lower()
    if x in [".crdownload", ".part", ".partial", ".opdownload", ".download",
           ".tmp", ".brave-download", ".aria2", ".!qb", ".!ut", ".bc!"]:
        continue
    elif file.name.lower() == ("desktop.ini", "settings.bin"):
        continue
    elif file.is_dir():
        folder_name = "folders"
    elif x in [".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg"]:
        folder_name = "images"
    elif x in [".mp4", ".avi", ".mov", ".mpeg"]:
        folder_name = "videos"
    elif x in [".mp3", ".wav", ".flac", ".ogg"]:
        folder_name = "audio"
    elif x in [".txt", ".docx", ".pdf"]:
        folder_name = "documents"
    elif x in [".zip", ".rar", ".tar", ".gz"]:
        folder_name = "compressed"
    elif x in [".exe", ".msi", "7z"]:
        folder_name = "executables"
    elif x in [".html", ".css", ".js", ".torrent", ".apk", ".jar", ".safetensors"]:
        folder_name = "web"
    elif x in [".py", ".java", ".c", ".cpp"]:
        folder_name = "source_code"
    elif x in [".csv", ".xlsx", ".json"]:
        folder_name = "data"
    else:
        continue
    destino = Path(final) / folder_name
    # destino.mkdir(parents=True, exist_ok=True)
    nuevo = destino / file.name 
    n = 1
    while nuevo.exists():
        nuevo = destino / f"{file.stem}_{n}{file.suffix}"
        n = n + 1
    try:
       # file.rename(nuevo)
        print(f"{file.name} -> {folder_name}")
    except PermissionError:
        print(f"No pude mover {file.name}, está en uso")