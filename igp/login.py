"""Login functionality for IGP Manager."""

from typing import Dict
import requests

from .config import base_url, headers


def login(username: str, password: str, remember: bool = False) -> Dict:
    """Attempt to log in to IGP Manager.

    Parameters
    ----------
    username : str
        Account username.
    password : str
        Account password.
    remember : bool, optional
        Whether to set the 'remember me' flag, by default False.

    Returns
    -------
    Dict
        The JSON response from the login attempt.
    """

    payload = {
        'loginUsername': username,
        'loginPassword': password,
        'loginRemember': int(remember),
    }

    params = {
        'action': 'send',
        'addon': 'igp',
        'type': 'login',
        'jsReply': 'login',
        'ajax': 1,
    }

    response = requests.post(base_url, headers=headers, params=params, data=payload)
    response.raise_for_status()
    return response.json()
