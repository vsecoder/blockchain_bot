from aiogram import Router

from . import wallet


def get_user_router() -> Router:
    from . import info, start, wallet

    router = Router()
    router.include_router(info.router)
    router.include_router(wallet.router)
    router.include_router(start.router)

    return router
