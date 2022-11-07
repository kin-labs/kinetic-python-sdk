from models.transaction_type import TransactionType
from models.kin_memo import KinMemo


def create_kin_memo(app_index: int, type: TransactionType = TransactionType.NONE):
    data = bytes()
    kin_memo = KinMemo.new(1, type, app_index, data)
    return kin_memo
