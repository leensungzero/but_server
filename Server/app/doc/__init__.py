def parameter(name: str, description: str, in_: str='json', type_: str='str', required: bool=True) -> dict:
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type_,
        'required': required
    }


SAMPLE_ACCESS_TOKEN = 'ffu9w32ilruhav9e8f72034712hgbifdyoavy023462r'
SAMPLE_REFRESH_TOKEN = 'jfoiuvfyhv8937qfy23o487fyweo8v7twegvowye3b2o8'

JWT_ACCESS_TOKEN = {
    'name': 'Authorization',
    'description': 'jwt access token',
    'in': 'header',
    'type': 'str',
    'required': 'true'
}