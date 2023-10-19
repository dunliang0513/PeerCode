from motor.motor_asyncio import AsyncIOMotorClient
from config import get_config
from model.question import Question

config = get_config()


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client[config.mongo_peercode_database_name]


# Create new questions
question_1 = Question(
    title="Finding maximum number",
    titleSlug="finding-maximum-number",
    topicTags=["list", "array"],
    hasSolution=True,
    hasVideoSolution=True,
    acRate=0.75,
    difficulty="Medium",
    status="Accepted",
    problem="The problem statement goes here.",
)
