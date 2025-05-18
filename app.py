import os
import re
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#Importing all Api-keys from .env:
os.environ["langchain_api_key"] = os.getenv("langchain_api_key")
os.environ["langchain_project"] = os.getenv("langchain_project")
os.environ["langchain_Tracing_v2"] = "true"

groq_api_key = os.getenv("groq_api_key")


#Defining model structure and prompt engineering.
def setup_llm_chain(topic = "Cyber Security"):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an AI cyber security expert, give concise, precise and structured explain about the user's query"),
            ("user", f"give short note on topic: {topic}")
        ]
    )
    
    llm = ChatGroq(
        model = "deepseek-r1-distill-llama-70b",
        groq_api_key = groq_api_key)
    
    return prompt|llm|StrOutputParser()

#Defining about particular tasks.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("HI!, Mention me with a topic to clearify your query, like (@CyberTech_bot Malware)")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Just mention me with a topic, like: CyberTech_bot Ransomware")
    
async def generate_response(update: Update, context: ContextTypes.DEFAULT_TYPE, topic: str):
    await update.message.reply_text(f"Generating about : {topic}")
    response = setup_llm_chain(topic).invoke({}).strip()
    print(f"Message length: {len(response)}") #Degub line
    await send_long_message(update, context, response)
 
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    bot_username = context.bot.username
    
    if f'@{bot_username}' in msg:
        match = re.search(f'@{bot_username}\\s+(.*)', msg)
        
        if match and match.group(1).strip():
            await generate_response(update, context, match.group(1).strip())
        else:
            await update.message.reply_text("please mention a topic after my name.")
    else:
        await update.message.reply_text("To get help, tag me with a topic. Example: CyberTech_bot Phishing")       

async def send_long_message(update, context, text):
    max_length = 4096
    for i in range(0, len(text), max_length):
        await update.message.reply_text(text[i:i+max_length])        

def main():
    token = os.getenv("telegram_api_key")
    
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(allowed_updates=Update.ALL_TYPES)
    
if __name__ == "__main__":
    main()

            
