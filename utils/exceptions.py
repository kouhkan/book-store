from typing import Any
from typing import Dict
from typing import Optional

from fastapi import HTTPException
from fastapi import status


# class DuplicateUser(HTTPException):
#     def __init__(
#             self,
#             headers: Optional[Dict[str, Any]] = None,
#     ) -> None:
#         super().__init__(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=f"",
#             headers=headers
#         )
