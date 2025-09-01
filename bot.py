import logging
import asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers.callback_handler import handle_callback_query
from handlers.command_handler import restart, default, menu
from config import TOKEN

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def main() -> None:
    # Configure the application with proper concurrency settings
    application = (
        Application.builder()
        .token(TOKEN)
        .concurrent_updates(True)  # Enable concurrent updates processing
        .read_timeout(30)  # Increase read timeout
        .write_timeout(30)  # Increase write timeout
        .connect_timeout(30)  # Increase connection timeout
        .pool_timeout(30)  # Increase pool timeout
        .build()
    )
    
    # Add handlers
    application.add_handler(CommandHandler("start", default))
    application.add_handler(CommandHandler("restart", restart))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default))
    application.add_handler(CallbackQueryHandler(handle_callback_query))

    # Start the Bot
    await application.run_polling(
        allowed_updates=["message", "callback_query"],  # Only process needed updates
        drop_pending_updates=True,  # Drop updates received before bot started
        close_loop=False  # Don't close the event loop on shutdown
    )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # Ignore exception when Ctrl-C is pressed
        print("\n👋 Bot stopped successfully!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise