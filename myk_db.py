import csv
import json
from pathlib import Path

class MangaYouKnowDB:
    def __init__(self):
        self.database = Path('database/data.csv')
        self.config = Path('database/config.json')

    def create_database(self):
        if not self.database.exists():
            self.database.touch()
            with open(self.database, mode='w') as file:
                writer_csv = csv.writer(file, lineterminator='\n')
                writer_csv.writerow([
                    'id_manga',
                    'name_manga',
                    'last_read',
                    'type',
                    'manga_path'
                ])

    def get_database(self) -> list:
        self.create_database()
        with open(self.database, mode='r', encoding='utf-8') as file:
            leitor_csv = csv.reader(file)
            database = []
            for linha in leitor_csv:
                database.append(linha)
        del[database[0]]
        return database

    def create_config(self):
        if not self.config.exists():
            self.config.touch()
            with open(self.config, mode='w') as file:
                json.dump({
                    'config': {
                    'reader-type':'pass-n',
                    'theme-color':'blue'
                    }
                }, file)

    def get_config(self) -> dict:
        self.create_config()
        with open(self.config, mode='r', encoding='utf-8') as file:
            config = json.load(file)
        return config

    def add_manga(self, manga:list):
        self.create_database()
        with open(self.database, mode='a') as file:
            writer_csv = csv.writer(file, lineterminator='\n')
            writer_csv.writerow(manga)
    
    def add_data_chapters_txt(self,chapters_list:list, manga_name:str):
        manga_data_path = Path(f'Mangas/{manga_name}/data/')
        manga_data_path.mkdir(parents=True, exist_ok=True)
        data_file = Path(f'{manga_data_path}/{manga_name}.txt')
        data_file.touch(exist_ok=True)
        with open(data_file, mode='a+', encoding='utf-8') as file:
            file.write(str(chapters_list))
        # for chapter in chapters_list:
        #     with open(data_file, mode='a+', encoding='utf-8') as file:
        #         file.write(f'{chapter} ')

    def delete_manga(self, manga_id:str):
        manga_id = str(manga_id)
        with open(self.database, "r") as file:
            leitor_csv = csv.reader(file)
            lista_csv = list(leitor_csv)
        for linha in lista_csv:
            if manga_id in linha:
                lista_csv.remove(linha)
        with open(self.database, "w", newline="") as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerows(lista_csv)


