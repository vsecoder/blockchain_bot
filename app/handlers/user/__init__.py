from aiogram import Router

from . import wallet


def get_user_router() -> Router:
    from . import info, start, wallet, sponsors, pay

    router = Router()
    router.include_router(info.router)
    router.include_router(wallet.router)
    router.include_router(sponsors.router)
    router.include_router(pay.router)
    router.include_router(start.router)

    return router
