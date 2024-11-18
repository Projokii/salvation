import asyncio
from proxy_handler import main

async def main_script():
    try:
        with open('userid.txt', 'r') as f:
            user_id = f.read().strip()  # Membaca user_id dari file
    except FileNotFoundError:
        print("File 'userid.txt' tidak ditemukan.")
        return

    await main('proxy_2.txt', user_id)  # Menggunakan proxy_2.txt untuk skrip 2.py

if __name__ == "__main__":
    asyncio.run(main_script())
