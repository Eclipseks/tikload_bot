from aiogram import executor

from config import dp

import app

def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()
