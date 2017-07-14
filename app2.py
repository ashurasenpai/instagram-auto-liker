import requests

headers = {
    'cookie': 'mid=WSIftgAEAAFwUxeNOyPlB10HXewu; fbm_124024574287414=base_domain=.instagram.com; sessionid=IGSC7b6db1443e83bb57503e0ea5f5add5c8d36ea0af4b41b1a5cf3c2f08398dba99%3A0Pi8T9YktF1MD5F3HiSWGbaL0LP7FE2X%3A%7B%22_token%22%3A%2238344725%3AtjuLqVNVtm1Byh7X2cMrSBjDvHD2zKZi%3Ad3f682f107e09a4c8d337ae996e570468b7b00c0e446112c24b24f1936fa8d1e%22%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_id%22%3A38344725%2C%22_platform%22%3A4%2C%22_auth_user_hash%22%3A%22%22%2C%22last_refreshed%22%3A1500063171.1531600952%2C%22asns%22%3A%7B%22time%22%3A1500063170%2C%2282.46.207.17%22%3A5089%7D%2C%22_token_ver%22%3A2%7D; fbsr_124024574287414=We7jbq9CiEuLbGMIGiXUv-M2rSJmRT8d6uBjmvd6NPU.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUNrUkpoMkZtV2pSVGVPRU1ITFZUSVd2cEVwdzJxT24tSC1FaXZEYlFLdUlzVGFqWVV4YzJ4V0JhZXhSbFlXMFY3T2I1X24yT0liRG5XSWc1cDBNdC1KRWZvalcwRWRRN0MyQlpBbmw4REJrb2V5d1pQYnBXbmxJOXQ1bzVNZFU1YTljaF9wUldhazRHT1dWR0lyUXkxa2hHMlJPUG1MVGc4eHk3Xy1FU19iZjVtMlhPemxla2pNSWxqb2RFeW5XamdhV25nUEdlcU9sU2NPNGcyMmJKRTJIVEFFSkFhX3J1TFc3LXNZMU5EVjNnS005cGxLeWl6N2dUa0JyREc2b1c0Q3JyTnZ5NlZjNGZKYVVmd2QxNDY0RU9OUWhSSmk5bUdGbGtTTWZzV0pVdGU5R2V3UUlFNnpVS1BXNi1zSUk1ZHNsaFN0VlNRUzk1WE1pZnNzTkpPRCIsImlzc3VlZF9hdCI6MTUwMDA2NTkzMCwidXNlcl9pZCI6IjEwNDgxNTM3MTMifQ; ig_pr=1; ig_vw=1844; rur=ATN; csrftoken=5k827c0I8B6Hr1Q71bgqKbg4TBKZhF3R; ds_user_id=38344725',
    'origin': 'https://www.instagram.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6,ro;q=0.4,ru;q=0.2',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrftoken': '5k827c0I8B6Hr1Q71bgqKbg4TBKZhF3R',
    'x-instagram-ajax': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/p/BWikNxblDjI/',
    'authority': 'www.instagram.com',
    'content-length': '0',
}

requests.post('https://www.instagram.com/web/likes/1558967697127258312/like/', headers=headers)
