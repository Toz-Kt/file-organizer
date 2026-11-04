from pathlib import Path

folder = Path("test_folder_exit")

for file in folder.iterdir():
    print(file.suffix)

    x = file.suffix.lower()

    if file.is_dir():
        continue
        print(f"{file.name} is a folder")
        destino = Path("enter") / "carpetas"
        destino.mkdir(parents=True, exist_ok=True)
        nuevo = destino / file.name
        n = 1
        while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)

    elif x in [".png", ".jpg", ".jpeg"]:
        print(f"{file.name} is this a image")
        destino = Path("enter") / "imagenes"
        destino.mkdir(parents=True, exist_ok=True)
        nuevo = destino / file.name 
        n = 1
        while nuevo.exists():
            nuevo = destino / f"{file.stem}_{n}{file.suffix}"
            n = n + 1
        file.rename(nuevo)
  
    elif x in [".mp4", ".avi", ".mov", ".mpeg"]:
        print(f"{file.name} is this a video")
        destino = Path("enter") / "videos"
        destino.mkdir(parents=True, exist_ok=True)
        nuevo = destino / file.name 
        n = 1
        while nuevo.exists():
            nuevo = destino / f"{file.stem}_{n}{file.suffix}"
            n = n + 1
        file.rename(nuevo)
        

    elif x in [".mp3", ".wav", ".flac"]:
            print(f"{file.name} is this a audio")
            destino = Path("enter") / "audios"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name 
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)

    elif x in [".txt", ".docx", ".pdf"]:
            print(f"{file.name} is this a document")
            destino = Path("enter") / "documentos"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)

    elif x in [".zip", ".rar", ".tar"]:
            print(f"{file.name} is this a compressed file")
            destino = Path("enter") / "comprimidos"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)

    elif x in [".exe", ".msi"]:
            print(f"{file.name} is this a executable file")
            destino = Path("enter") / "executables"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)

    elif x in [".html", ".css", ".js"]:
            print(f"{file.name} is this a web file")
            destino = Path("enter") / "web"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)
    elif x in [".py", ".java", ".c", ".cpp"]:
            print(f"{file.name} is this a source code file")
            destino = Path("enter") / "source_code"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)

    elif x in [".csv", ".xlsx", ".json"]:
            print(f"{file.name} is this a data file")
            destino = Path("enter") / "data"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)

    else:
            print(f"{file.name} is this a unknown file type")
            destino = Path("enter") / "unknown"
            destino.mkdir(parents=True, exist_ok=True)
            nuevo = destino / file.name
            n = 1
            while nuevo.exists():
                nuevo = destino / f"{file.stem}_{n}{file.suffix}"
                n = n + 1
                file.rename(nuevo)
