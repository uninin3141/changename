import discord
import os

# Railwayの環境変数からDiscord Botのトークンを取得
TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# インテントの生成
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')

@client.event
async def on_member_update(before,after):
    # 特定のユーザーのIDを指定
    specific_user_id = 932667896776237057  # 特定のユーザーのIDをここに入力

    # 変更が特定のユーザーに対して行われたか確認
    if after.id == specific_user_id:
        # ニックネームが変更されたか確認
        if before.nick != after.nick:
            try:
                # ニックネームを"abc"に変更
                await after.edit(nick="バタダイ@福山修司の嫁")
                print(f"{after.display_name}の名前を変更しました。")
            except Exception as e:
                print(f"名前の変更に失敗しました: {e}")

# ここにBotのトークンを入力
client.run(TOKEN)
