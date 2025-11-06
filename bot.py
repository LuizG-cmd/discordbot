import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def buscar_kabum(modelo: str):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")0
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(f"https://www.kabum.com.br/busca/{modelo}")

        time.sleep(2)  

        produtos = driver.find_elements(By.CLASS_NAME, "productCard")

        for produto in produtos:
            try:
                titulo = produto.find_element(By.CLASS_NAME, "nameCard").text.lower()
                preco = produto.find_element(By.CLASS_NAME, "priceCard").text
                link = produto.find_element(By.TAG_NAME, "a").get_attribute("href")

                if "placa de vídeo" in titulo or "rtx" in titulo or "gtx" in titulo:
                    return titulo.title(), preco, link

            except NoSuchElementException:
                continue

        return None, None, None

    finally:
        driver.quit()

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command(name="preco")
async def preco(ctx, *, modelo: str):
    await ctx.send(f"🔍 Buscando preço para: **{modelo}**...")
    titulo, preco, link = buscar_kabum(modelo)

    if not titulo or not preco:
        await ctx.send("❌ Não encontrei esse produto no Kabum.")
    else:
        await ctx.send(f"**{titulo}**\n💰 Preço: {preco}\n🔗 [Ver no Kabum]({link})")


bot.run(TOKEN)