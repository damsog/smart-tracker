from prisma import Prisma
from ..libs.logger import Logger

# Database configuration
database = Prisma(auto_register=True)
