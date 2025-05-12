import logging
import firebase_admin
from firebase_admin import credentials, firestore
from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")

# Initialize Firebase with service account credentials
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Enable logging for debugging and monitoring
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /start command.

    Greets the user and provides basic usage instructions.
    """
    user = update.message.from_user
    logger.info("User %s started the bot.", user.first_name)
    await update.message.reply_text(
        f"Hi {user.first_name}! 👋 I'm your inventory management bot. "
        f"Use /add to add products and /list to view the inventory."
    )

async def add_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /add command.

    Adds a product to the inventory, or updates the quantity if it already exists.
    Usage: /add <name> <quantity> <price>
    """
    if len(context.args) < 3:
        await update.message.reply_text("❌ Correct usage: /add <name> <quantity> <price>")
        return

    name = context.args[0]
    try:
        quantity = int(context.args[1])
        price = float(context.args[2])
    except ValueError:
        await update.message.reply_text("❌ Quantity and price must be valid numbers.")
        return

    try:
        # Check if the product already exists
        existing_products = db.collection('inventario').where('name', '==', name).stream()
        existing_products_list = list(existing_products)

        if existing_products_list:
            # Product exists: check if price matches
            existing_product = existing_products_list[0].to_dict()
            existing_price = existing_product['price']

            if existing_price != price:
                await update.message.reply_text(
                    f"❌ The product '{name}' already exists with a different price (${existing_price}).\n"
                    f"You cannot add it with a new price (${price})."
                )
                return

            # Price matches: update quantity
            product_ref = existing_products_list[0].reference
            current_quantity = existing_product['quantity']
            new_quantity = current_quantity + quantity

            product_ref.update({'quantity': new_quantity})
            await update.message.reply_text(
                f"🔄 Product '{name}' updated.\n"
                f"📦 New quantity: {new_quantity}\n"
                f"💰 Price: ${price}"
            )
        else:
            # Product does not exist: add new document
            db.collection('inventario').add({
                'name': name,
                'quantity': quantity,
                'price': price
            })
            await update.message.reply_text(
                f"✅ Product '{name}' added to inventory.\n"
                f"📦 Quantity: {quantity}\n"
                f"💰 Price: ${price}"
            )

    except Exception as e:
        await update.message.reply_text(f"❌ Error adding product: {e}")

async def list_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /list command.

    Retrieves and displays all products in the inventory.
    """
    try:
        products = db.collection('inventario').stream()
        products_list = list(products)

        if not products_list:
            await update.message.reply_text("📭 Inventory is empty.")
            return

        # Build a readable inventory list
        inventory_list = "📋 **Inventory:**\n\n"
        for product in products_list:
            product_data = product.to_dict()
            inventory_list += (
                f"📦 **Product:** {product_data['name']}\n"
                f"🔢 **Quantity:** {product_data['quantity']}\n"
                f"💰 **Price:** ${product_data['price']}\n"
                "------------------------\n"
            )

        await update.message.reply_text(inventory_list)

    except Exception as e:
        await update.message.reply_text(f"❌ Error listing products: {e}")

async def delete_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /delete command.

    Deletes a product from the inventory by its name.
    Usage: /delete <product_name>
    """
    if len(context.args) < 1:
        await update.message.reply_text("❌ Correct usage: /delete <product_name>")
        return

    name = context.args[0]

    try:
        products = db.collection('inventario').where('name', '==', name).stream()
        deleted = False

        for product in products:
            product.reference.delete()
            deleted = True

        if deleted:
            await update.message.reply_text(f"✅ Product '{name}' deleted from inventory.")
        else:
            await update.message.reply_text(f"❌ Product '{name}' not found.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error deleting product: {e}")

def main():
    """
    Main entry point to initialize and run the Telegram bot.
    """
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_inventory))
    application.add_handler(CommandHandler("list", list_inventory))
    application.add_handler(CommandHandler("delete", delete_inventory))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
