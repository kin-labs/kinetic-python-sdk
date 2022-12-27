# pylint: disable=missing-module-docstring,invalid-name
from typing import Optional

from kinetic_sdk.models.transaction_type import TransactionType

MAGIC_BYTE = 0x1

# The highest Kinetic memo version supported by this implementation.
HIGHEST_VERSION = 1


class KinMemo:
    """Implements the Kinetic memo specification
    :param val: the raw memo bytearray.
    """

    def __init__(self, val: bytearray):
        if len(val) > 32:
            raise ValueError(f"invalid memo length {len(val)}")

        self.val = val

    def __eq__(self, other):
        if not isinstance(other, KinMemo):
            return False

        return self.val == other.val

    def __repr__(self):
        return f"{self.__class__.__name__}(" f"val={self.val})"

    @classmethod
    def new(
        cls, version: int, tx_type: TransactionType, app_index: int, foreign_key: Optional[bytes] = b""
    ) -> "KinMemo":
        """Returns a Kinetic memo containing the provided properties.
        :param version: The memo encoding version
        :param tx_type: The :class:`TransactionType <Kinetic.model.transaction_type.TransactionType>` of the transaction
        :param app_index: The index of the app the transaction relates to
        :param foreign_key: An identifier in an auxiliary service that contains additional data about what the
            transaction was for
        :return: an :class:`KinMemo <KinMemo>` object
        """
        if version < 0 or version > 7:
            raise ValueError("invalid version")

        if tx_type < 0 or tx_type > 2**5 - 1:
            raise ValueError("invalid transaction type")

        if app_index < 0 or app_index > 2**16 - 1:
            raise ValueError("invalid app index")

        if len(foreign_key) > 29:
            raise ValueError(f"invalid foreign key length {len(foreign_key)}")

        v = version & 0xFF
        t = tx_type & 0xFF

        val = bytearray(32)
        val[0] = MAGIC_BYTE
        val[0] |= v << 2
        val[0] |= (t & 0x7) << 5

        val[1] = (t & 0x18) >> 3
        val[1] |= (app_index & 0x3F) << 2

        val[2] = (app_index & 0x3FC0) >> 6

        val[3] = (app_index & 0xC000) >> 14

        if len(foreign_key) > 0:
            val[3] |= (foreign_key[0] & 0x3F) << 2

            # Insert the rest of the fk. Since each loop references fk[n] and
            # fk[n+1], the upper bound is offset by 3 instead of 4.
            for i in range(4, 3 + len(foreign_key)):
                # apply last 2-bits of current byte
                val[i] = (foreign_key[i - 4] >> 6) & 0x3
                # apply first 6-bits of next byte
                val[i] |= (foreign_key[i - 3] & 0x3F) << 2

            # if the foreign key is less than 29 bytes, the last 2 bits of the
            # FK can be included in the memo
            if len(foreign_key) < 29:
                val[len(foreign_key) + 3] = (foreign_key[len(foreign_key) - 1] >> 6) & 0x3

        return cls(val)
