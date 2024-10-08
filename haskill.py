# bot.py
import os, discord

#import discord
from dotenv import load_dotenv
import interactions
import inspect
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
VOTING_ACTIVE = True

bot = interactions.Client(token=TOKEN, intents=interactions.Intents.DEFAULT)

confPAButton = interactions.Button(
    style=interactions.ButtonStyle.SUCCESS,
    label="CONFIRM Personal Action",
    custom_id="CONFIRMPA"
)

confCAButton = interactions.Button(
    style=interactions.ButtonStyle.SUCCESS,
    label="CONFIRM Crisis Action",
    custom_id="CONFIRMCA"
)

cancelButton = interactions.Button(
    style=interactions.ButtonStyle.DANGER,
    label="Start over",
    custom_id="CANCEL"
)

lastButtonRowPA = [confPAButton, cancelButton]

lastButtonRowCA = [confCAButton, cancelButton]

button1 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Personal Action",
    custom_id="PA"
)

button2 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Crisis Action",
    custom_id="CA"
)

paButton4 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Leadership Action",
    custom_id="LA"
)

paButton5 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Guild Action",
    custom_id="GA"
)

buttonRow1 = interactions.ActionRow(
    components=[button1, button2] #button3, button4]
)

paButton1 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Study Magic",
    custom_id="MG"
)

paButton2 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Study Alchemy",
    custom_id="ALCH"
)

paButton3 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Commission a Sloop",
    custom_id="SLP"
)

paButtonRow1 = interactions.ActionRow(
    components=[paButton1, paButton2, paButton3, paButton4]
)

paButtonRow2 = interactions.ActionRow(
    components=[paButton5, cancelButton]
)


clrgButton = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Clergy In the Court",
    custom_id="CLRG"
)

clrg1Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Support a Secular Council",
    custom_id="CLRG1"
)


clrg2Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Include a High Priest",
    custom_id="CLRG2"
)

clrgButtonRow = interactions.ActionRow(
    components=[clrg1Button, clrg2Button, cancelButton]
)

gmrButton = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Golem Making Resurgence",
    custom_id="GMR"
)

gmr1Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Support the acceptance of Golem-Making",
    custom_id="GMR1"
)

gmr2Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Support the Outlawing of Golem-Making",
    custom_id="GMR2"
)

gmrButtonRow = interactions.ActionRow(
    components=[gmr1Button, gmr2Button, cancelButton]
)


rchButton = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="First Royal Court Hosts",
    custom_id="RCH"
)

rch1Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Support City Of Light as the Hosts",
    custom_id="RCH1"
)

rch2Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Support Heptapyrgion as the Hosts",
    custom_id="RCH2"
)

rchButtonRow = interactions.ActionRow(
    components=[rch1Button, rch2Button, cancelButton]
)


bsiButton = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Black Shore Sphere of Influence",
    custom_id="BSI"
)

bsiButton1 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Strengthen the Ties with the Free North",
    custom_id="BSI1"
)

bsiButton2 = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Embrace Aeonian Mercantile League Influence",
    custom_id="BSI2"
)

bsiButtonRow = interactions.ActionRow(
    components=[bsiButton1, bsiButton2, cancelButton]
)

hide1Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Do discreetly",
    custom_id="HID1"
)

hide2Button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Openly Influence",
    custom_id="HID2"
)

hideButtonRow = interactions.ActionRow(
    components=[hide1Button, hide2Button, cancelButton]
)

caButtonRow = interactions.ActionRow(
    components=[clrgButton, gmrButton, rchButton, bsiButton]
)

ca2ButtonRow = interactions.ActionRow(
    components=[bsiButton]
)


openText = open("Choices1", "r").read()

ACTION_ROLE = 1146817577109164105
LEADERSHIP_ROLE = 1147839725906968596
CAPTAIN_ROLE = 1147840058871795772
GM_ROLE = 959153279508574258
RDG_ROLE = 959143816693174363

MAGIC_CHANNEL = 1147847436631552050
LEADERS_CHANNEL = 959140485522411530
GUILD_ID = 958732872762662912
TEST_CHANNEL = 1147179780458954886

RULES_DOCU_LINK = "https://docs.google.com/presentation/d/18Aei8NCq-ZgEdlIHORoLsEFlmzOoGvXQshiG-Zd5OEs/edit#slide=id.g27d6f39b5de_0_1627"
BOT_HOW_LINK = "https://docs.google.com/document/d/1VG8oY0ELrQ0cGq68yXZCmvv9O8tEgY3mwBhjhJjywp0/edit?usp=sharing"
CA_FLUFF_ACTIONS = "https://docs.google.com/document/d/1WucUHVxrl3IC5ZkgENRj_AWChiYTewWRtvq-6LKgpFs/edit?usp=sharing"

def crisis2Text(choice):
    if choice == "CLRG1":
        return "is supporting a Secular council"
    elif choice == "CLRG2":
        return "is supporting the inclusion of a High Priest in the Curia Regis"
    elif choice == "GMR1":
        return "is supporting the acceptance of Golem Making"
    elif choice == "GMR2":
        return "is supporting the outlawing of Golem Making"
    elif choice == "RCH1":
        return "is supporting the City of Light as the First Royal Court's Host"
    elif choice == "RCH2":
        return "is supporting Heptapyrgion as the First Royal Court's Host"
    elif choice == "BSI1":
        return "is supporting the strengthening of ties between the Black Shore and the Free North"
    elif choice == "BSI2":
        return "is supporting the embrace of Aeonian Mercantile League influence for the Black Shore"
class Voter:
    def __init__(self, id, name, charName, hasRole, pachoice, cachoice, actionHidden):
        self.id = id
        self.name = name
        self.charName = charName
        self.hasRole = hasRole
        self.pachoice = pachoice
        self.cachoice = cachoice
        self.actionHidden = actionHidden

voters = []

@bot.command(
    name="vote",
    description="Voting action for players with the Action role",
    scope=GUILD_ID,
    options = [
        interactions.Option(
            name="character_name",
            description="For which character is your action",
            type=interactions.OptionType.STRING,
            required=True,
        )
        # interactions.Option(
        #     name="nation_or_guild",
        #     description="Your origin Nation, or guild for which you plan to take a leadership action (if you choose so)",
        #     type=interactions.OptionType.STRING,
        #     required=True,
        # )
    ],
)
async def my_command(ctx: interactions.CommandContext, character_name: str):
    #print(ctx.guild.get_role(1147197203429994638))
    role = await ctx.guild.get_role(ACTION_ROLE)
    gmrole = await ctx.guild.get_role(GM_ROLE) 
    #print(ctx.member)
    #print(ctx.member.roles)
    if VOTING_ACTIVE == False and ctx.member.id != NATHANIEL_ID and ctx.member.id != ESTINIEN_ID and ctx.member.id != NATHANIEL2_ID :
        await ctx.send("Coming soon...", ephemeral=True)
        return 1
    if role.id in ctx.member.roles:
        voter = next((x for x in voters if x.id == ctx.member.id), None)
        if len(voters) and voter != None:
            voters.remove(voter)
        voter = Voter(ctx.member.id, ctx.member.username, character_name, True, "NULL", "NULL", False)
        voters.append(voter)
        await ctx.send(openText, ephemeral=True)
        await ctx.send(f"It is important to consult the document linked above\nYou will also be asked if your character acts openly or discreetly\n(Openly meaning a discord post on the Geopolitics Channel)\nSelect which crisis interests you:", components=caButtonRow, ephemeral=True)
        # await ctx.send("Choose ", components=paButtonRow1, ephemeral=True)
        # await ctx.send("", components=paButtonRow2, ephemeral=True)

    else:
        await ctx.send("You dont have an action!", ephemeral=True)

NATHANIEL_ID = 691734428082372609
NATHANIEL2_ID = 220956485889294336
ESTINIEN_ID = 256517556750385153

@bot.command(
    name="nathaniel_dump",
    description="Nathaniel casts dump",
    scope=GUILD_ID,
    options = [],
)
async def nathaniel_dump(ctx: interactions.CommandContext):
    if ctx.member.id == NATHANIEL_ID or ctx.member.id == NATHANIEL2_ID or ctx.member.id == ESTINIEN_ID:
        fresults = open("results.txt", "r")
        results = fresults.read()
        await ctx.send(results, ephemeral=True)
        fresults.close()
        
    else:
        await ctx.send("Command not available, sorry you are not Nathaniel", ephemeral=True)

 #1147197203429994638

@bot.component("PA")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen a Personal Action,\nChoose one from below:", components=paButtonRow1, ephemeral=True)
    voter.choice = "PA"

@bot.component("MG")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to advance in your magical talents, you will gain two spells or a ritual (if all spells are learnt)\nConfirm your choice", components=lastButtonRowPA, ephemeral=True)
    voter.pachoice = "MG"

@bot.component("ALCH")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to advance in your alchemical knowledge, you will gain a new alchemical recipe\nConfirm your choice", components=lastButtonRowPA, ephemeral=True)
    voter.pachoice = "ALCH"

@bot.component("CA")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send(f"You have chosen to influence one of the crises in the lands of Aeonia\nIt is important to consult the document here {RULES_DOCU_LINK} for each crisis' fluff and outcome you want to push for\nSelect which crisis interests you:", components=caButtonRow, ephemeral=True)
    await ctx.send("Special for Ryu Diguo Characters only Crisis:", components=ca2ButtonRow, ephemeral=True)
    voter.pachoice = "CA"

@bot.component("GA")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    # await ctx.send(f"You have chosen a Guild Action,\nCharacter: *{voter.charName}* will make a move for Guild: *{voter.nation}*\nConfirm your choice", components=lastButtonRowPA, ephemeral=True)
    voter.pachoice = "GA"

@bot.component("LA")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    # await ctx.send(f"You have chosen a Leadership Action,\nCharacter: *{voter.charName}* will make a move for Nation/Guild: *{voter.nation}*\nConfirm your choice", components=lastButtonRowPA, ephemeral=True)
    voter.pachoice = "LA"

@bot.component("SLP")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    # await ctx.send("You have chosen to Build a Sloop\nYou will be able to move it to an area afterwards,\nConfirm your choice", components=lastButtonRowPA, ephemeral=True)
    voter.pachoice = "SLP"

@bot.component("CLRG")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("Clergy in the Court\nChoose which outcome to Influence:", components=clrgButtonRow, ephemeral=True)
    voter.cachoice = "CLRG"


@bot.component("CLRG1")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support a Secular Royal Court free of Clerical Influence\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "1"

@bot.component("CLRG2")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support the inclusion of a High Priest in the Curia Regis\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "2"

@bot.component("GMR")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("Golem Making Resurgence\nChoose which outcome to Influence:", components=gmrButtonRow, ephemeral=True)
    voter.cachoice = "GMR"

@bot.component("GMR1")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support the acceptance of Golem-Making\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "1"

@bot.component("GMR2")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support the outlawing of Golem-Making\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "2"   

@bot.component("RCH")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("Hosts of The Royal Court\nChoose which outcome to Influence:", components=rchButtonRow, ephemeral=True)
    voter.cachoice = "RCH"   

@bot.component("RCH1")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support the City of Light in Vasiliko as the Host for the first Royal Court\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "1" 

@bot.component("RCH2")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support Heptapyrgion as the Host for the first Royal Court\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "2"
                     

@bot.component("BSI")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("Black Shore Sphere of Influence\nChoose which outcome to Influence:", components=bsiButtonRow, ephemeral=True)
    voter.cachoice = "BSI"
    

@bot.component("BSI1")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support the strengthening of ties with the Free North\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "1"  

@bot.component("BSI2")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("You have chosen to support the embrace of Aeonian Mercantile League influence\nDo you wish for your action to remain hidden?", components=hideButtonRow, ephemeral=True)
    voter.cachoice += "2"   

@bot.component("HID1")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("Your actions will remain hidden\nConfirm your vote", components=lastButtonRowCA, ephemeral=True)
    voter.actionHidden = True  

@bot.component("HID2")
async def button_response(ctx):
    voter = next((x for x in voters if x.id == ctx.member.id))
    await ctx.send("Your actions will be public knowledge\nConfirm your vote", components=lastButtonRowCA, ephemeral=True)
    voter.actionHidden = False           


@bot.component("CANCEL")
async def button_response(ctx):
    await ctx.send(f"You will influence one of the crises in the lands of Aeonia\nIt is important to consult the document here {RULES_DOCU_LINK} for each crisis' fluff and outcome you want to push for\nSelect which crisis interests you:", components=caButtonRow, ephemeral=True)
    #await ctx.send("", components=paButtonRow2, ephemeral=True)
    voter = next((x for x in voters if x.id == ctx.member.id))
    voter.pachoice = "NULL"
    voter.cachoice = "NULL"
    

@bot.component("CONFIRMPA")
async def button_response(ctx):
    role = await ctx.guild.get_role(ACTION_ROLE)
    if role.id in ctx.member.roles:
        voter = next((x for x in voters if x.id == ctx.member.id))
        if voter.pachoice == "MG" or voter.pachoice == "ALCH":
            if voter.pachoice == "MG":
                await ctx.send("You chose to advance your magical studies!\nYou will gain two spells of your choice or a ritual if you know all spells", ephemeral=True)
            else:
                await ctx.send("You chose to advance your magical studies!\nYou will gain a new alchemical Recipe!", ephemeral=True)
        # elif voter.pachoice == "LA":
            # await ctx.send("You chose a leadership action for your Nation/Guild!\nYou will gain access to the appropriate channel with your leadership Role!", ephemeral=True)
        # elif voter.pachoice == "GA":
            # await ctx.send("You chose a leadership action for your Guild!\nYou will gain access to the appropriate channel with your leadership Role!", ephemeral=True)
        # elif voter.pachoice == "SLP":
            # await ctx.send("You have chosen to build a Sloop/Merchant/Transport Ship!\nYou Will be added to the appropriate channel in order to move it with your new role", ephemeral=True)    
        await ctx.send("Continue with your Crisis Support Action", components=caButtonRow, ephemeral=True)
    else:
        ctx.send("It seems you dont have an action...", component=cancelButton, ephemeral=True)

@bot.component("CONFIRMCA")
async def button_response(ctx):
    role = await ctx.guild.get_role(ACTION_ROLE)
    if role.id in ctx.member.roles:
        voter = next((x for x in voters if x.id == ctx.member.id))

        await ctx.send(f"Thank you for your participation.", ephemeral=True)
        #Magic/Alchemy Personal Action
        if voter.pachoice == "MG":
            channel = await interactions.get(bot, interactions.Channel, object_id=MAGIC_CHANNEL)
            await channel.send(f"<@&{GM_ROLE}> Mage {voter.charName} (<@{voter.id}> {voter.name}) is expanding their magical knowledge...")
        elif voter.pachoice == "ALCH":
            channel = await interactions.get(bot, interactions.Channel, object_id=MAGIC_CHANNEL)
            await channel.send(f"<@&{GM_ROLE}> Alchemist {voter.charName} (<@{voter.id}> {voter.name}) is advancing in their alchemical studies...")
        
        #Nation/Guild Leadership
        elif voter.pachoice == "LA" or voter.pachoice == "GA":
            await ctx.member.add_role(LEADERSHIP_ROLE)
            channel = await interactions.get(bot, interactions.Channel, object_id=LEADERS_CHANNEL)#LEADERS_CHANNEL)
            # await channel.send(f"<@&{GM_ROLE}> {voter.charName} (<@{voter.id}> {voter.name}) is taking a leadership action for {voter.nation} ")
        
        elif voter.pachoice == "SLP":
            await ctx.member.add_role(CAPTAIN_ROLE)
            # getting the timestamp
            channel = await interactions.get(bot, interactions.Channel, object_id=LEADERS_CHANNEL)#LEADERS_CHANNEL)
            await channel.send(f"Avast! {voter.charName} (<@{voter.id}>) commands a ship!")

        #getting the timestamp
        ts = datetime.now()
        f = open("results.txt", "a")
        f.write(f"{voter.name}, {voter.charName}, {voter.pachoice}, {voter.cachoice}, {voter.actionHidden}, {ts}\n")
        f.close()
        if voter.actionHidden == False:
            channel = await interactions.get(bot, interactions.Channel, object_id=LEADERS_CHANNEL)#LEADERS_CHANNEL)
            await channel.send(f"{voter.charName} (<@{voter.id}>) {crisis2Text(voter.cachoice)}")  
        #comment the line below to stop role removal
        await ctx.member.remove_role(ACTION_ROLE)
        voter.hasRole = False
        voters.remove(voter)


            # VOTER FINALE!
            # voter.hasRole = False
            # await ctx.member.remove_role(ACTION_ROLE)
            # # getting the timestamp
            # ts = datetime.now()                   
            # f = open("results.txt", "a")
            # f.write(f"{voter.name}, {voter.charName}, {voter.nation}, {voter.choice}, {ts}\n")
            # f.close()
            # voters.remove(voter)
            # #await ctx.send()    

            # FINALE MG ALCH
            # channel = await interactions.get(bot, interactions.Channel, object_id=MAGIC_CHANNEL)
            # if voter.choice == "MG":
            #     await channel.send(f"<@&{GM_ROLE}> Mage {voter.charName} (<@{voter.id}> {voter.name}) is expanding their magical knowledge...")
            # else:
            #     await channel.send(f"<@&{GM_ROLE}> Alchemist {voter.charName} (<@{voter.id}> {voter.name}) is advancing in their alchemical studies...")

            # FINALE LA And GA
            # await ctx.member.remove_role(ACTION_ROLE)
            # await ctx.member.add_role(LEADERSHIP_ROLE)
            # channel = await interactions.get(bot, interactions.Channel, object_id=LEADERS_CHANNEL)
            # await channel.send(f"<@&{GM_ROLE}> {voter.charName} (<@{voter.id}> {voter.name}) is taking a leadership action for {voter.nation} ")

            # FINALE SHIP
            # await ctx.member.remove_role(ACTION_ROLE)
            # await ctx.member.add_role(CAPTAIN_ROLE)
            # # getting the timestamp
            # ts = datetime.now()
            # f = open("results.txt", "a")
            # f.write(f"{voter.name}, {voter.charName}, {voter.nation}, {voter.choice}, {ts}\n")
            # f.close()
            # channel = await interactions.get(bot, interactions.Channel, object_id=LEADERS_CHANNEL)
            # await channel.send(f"Avast! {voter.charName} (<@{voter.id}>) is now the proud owner of a ship!")
            # voters.remove(voter)

bot.start()

