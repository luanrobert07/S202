from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
## db.resetDatabase()

tipos = ["Grass", "Poison"]
tipoGrassAndPoison = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })

writeAJson(tipoGrassAndPoison, "tipoGrassAndPoison")

fraquezas = ["Psychic", "Ice"]
tipoPsychicAndIce = db.collection.find({"weaknesses": {"$all": fraquezas}})

writeAJson(tipoPsychicAndIce, "tipoPsychicAndIce")

pokemonsOneWeaknesses = db.collection.find({"weaknesses": {"$size": 1}})

writeAJson(pokemonsOneWeaknesses, "pokemonsOneWeaknesses")

pokemonsNoneMultipliers = db.collection.find({"multipliers": None})

writeAJson(pokemonsNoneMultipliers, "pokemonsNoneMultipliers")

Allpokemons = db.collection.find()

writeAJson(Allpokemons, "Allpokemons")

